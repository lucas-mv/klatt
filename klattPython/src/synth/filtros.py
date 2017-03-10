"""
Conjunto de codigos que definem o funcionamento dos filtros ressonantes do sintetizador.
"""

import src.synth.parametros as params
import src.synth.constantes as ctes
import src.synth.forma_onda as forma_onda
import math
import numpy as np
from scipy import signal

class Filtro:
    _numerador = None
    _denominador = None

    def __init__(self, vogal, av, avs):
        self._numerador, self._denominador = self.montarfiltros(vogal, av, avs)

    # <editor-fold desc="Funcoes matematicas de calculos dos parametros">

    def calcularabc(self, bw, f):
        t = ctes.Amostragem.TEMPO_AMOSTRAGEM
        c = -1 * math.exp(-2 * np.pi * bw * t)
        b = 2 * math.exp(-1 * np.pi * bw * t) * math.cos(2 * np.pi * t * f)
        a = 1 - b - c
        return a, b, c

    def montar_numden(self, bw, f):
        a, b, c = self.calcularabc(bw, f)
        num = [a, 0, 0]
        den = [1, -1*b, -1*c]
        return num, den

    def montar_numden_antiressonante(self, bw, f):
        a, b, c = self.calcularabc(bw, f)
        a_anti = 1/a
        b_anti = -1*b/a
        c_anti = -1*c*a
        num = [a_anti, b_anti, c_anti]
        den = [1, 0, 0]
        return num, den

    # </editor-fold>

    # <editor-fold desc="Definicoes dos blocos do sintetizador">

    def bloco_fonte(self, parametros):
        num_rgp, den_rgp = self.montar_numden(ctes.ParametrosConstantes.BGP, ctes.ParametrosConstantes.FGP)
        num_rgs, den_rgs = self.montar_numden(ctes.ParametrosConstantes.BGS, ctes.ParametrosConstantes.FGS)
        num_rgz, den_rgz = self.montar_numden_antiressonante(ctes.ParametrosConstantes.BGZ, ctes.ParametrosConstantes.FGZ)
        for indice in range(len(num_rgs)):
            num_rgs[indice] = num_rgs[indice] * parametros.av
        for indice in range(len(num_rgz)):
            num_rgz[indice] = num_rgz[indice] * parametros.avs
        num_paralelo = [num_rgs[0] + num_rgz[0], num_rgz[1], num_rgz[2]]
        den_paralelo = [den_rgz[0] + den_rgs[0], den_rgs[1], den_rgs[2]]
        num_fonte = np.convolve(num_rgp, num_paralelo)
        den_fonte = np.convolve(den_rgp, den_paralelo)
        return num_fonte, den_fonte

    def bloco_nasal(self, parametros):
        num_rnp, den_rnp = self.montar_numden(ctes.ParametrosConstantes.BNP, ctes.ParametrosConstantes.FNP)
        num_rnz, den_rnz = self.montar_numden_antiressonante(ctes.ParametrosConstantes.BNZ, parametros.fnz)
        num_nasal = np.convolve(num_rnp, num_rnz)
        den_nasal = np.convolve(den_rnp, den_rnz)
        return num_nasal, den_nasal

    def bloco_formantes(self, parametros):
        num_1, den_1 = self.montar_numden(parametros.b1, parametros.f1)
        num_2, den_2 = self.montar_numden(parametros.b2, parametros.f2)
        num_3, den_3 = self.montar_numden(parametros.b3, parametros.f3)
        num_4, den_4 = self.montar_numden(parametros.b4, parametros.f4)
        num_5, den_5 = self.montar_numden(parametros.b5, parametros.f5)
        num = np.convolve(num_1, num_2)
        den = np.convolve(den_1, den_2)
        num = np.convolve(num, num_3)
        den = np.convolve(den, den_3)
        num = np.convolve(num, num_4)
        den = np.convolve(den, den_4)
        num = np.convolve(num, num_5)
        den = np.convolve(den, den_5)
        return num, den

    def bloco_radiacao(self):
        num = [1, 0]
        den = [1, 1]
        return num, den

    # </editor-fold>

    def filtrar(self, frame):
        funcao_transferencia = signal.TransferFunction(self._numerador, self._denominador, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
        x, y = signal.dlsim(funcao_transferencia, frame._valores)
        return forma_onda.Frame(y)

    def montarfiltros(self, vogal, av, avs):
        parametros = params.ParametrosCascata(vogal, av, avs)

        num_fonte, den_fonte = self.bloco_fonte(parametros)
        num_form, den_form = self.bloco_formantes(parametros)
        num_rad, den_rad = self.bloco_radiacao()
        num_nasal, den_nasal = self.bloco_nasal(parametros)

        num = np.convolve(num_nasal, num_form)
        den = np.convolve(den_nasal, den_form)
        num = np.convolve(num_fonte, num)
        den = np.convolve(den_fonte, den)
        num = np.convolve(num, num_rad)
        den = np.convolve(den, den_rad)

        return num, den

