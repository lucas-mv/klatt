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

    def __init__(self, vogal, av):
        self._numerador, self._denominador = self.montarfiltros(vogal, ctes.ParametrosConstantes.F0, av)

    def filtrar(self, frame):
        funcao_transferencia = signal.TransferFunction(self._numerador, self._denominador, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
        x, y = signal.dlsim(funcao_transferencia, frame._valores)
        return forma_onda.Frame(y)

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
        a, b, c = self.calcularabc(self, bw, f)
        a_anti = 1/a
        b_anti= -1*b/a
        c_anti = -1*c*a
        num = [a_anti, b_anti, c_anti]
        den = [1, 0, 0]
        return num, den

    def montarfiltros(self, vogal, f0, av):
        parametros = params.ParametrosCascata(vogal, f0, av)

        num_rgp, den_rgp = self.montar_numden(ctes.ParametrosConstantes.BGP, ctes.ParametrosConstantes.FGP)
        num_rgs, den_rgs = self.montar_numden(ctes.ParametrosConstantes.BGS, ctes.ParametrosConstantes.FGZ)
        num_rgz, den_rgz = self.montar_numden(ctes.ParametrosConstantes.BGZ, ctes.ParametrosConstantes.FGZ)
        num_fonte = np.convolve(num_rgp, num_rgs)
        num_fonte = np.convolve(num_fonte, num_rgz)
        den_fonte = np.convolve(den_rgp, den_rgs)
        den_fonte = np.convolve(den_fonte, den_rgz)

        num_rnp, den_rnp = self.montar_numden(ctes.ParametrosConstantes.BNP, ctes.ParametrosConstantes.FNP)
        num_rnz, den_rnz = self.montar_numden(ctes.ParametrosConstantes.BNZ, parametros.fnz)
        num_nasal = np.convolve(num_rnp, num_rnz)
        den_nasal = np.convolve(den_rnp, den_rnz)

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
        num = np.convolve(num_nasal, num)
        den = np.convolve(den_nasal, den)
        num = np.convolve(num_fonte, num)
        den = np.convolve(den_fonte, den)

        return num, den

