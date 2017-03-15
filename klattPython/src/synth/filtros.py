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

    def filtrar(self, frame):
        funcao_transferencia = signal.TransferFunction(self._numerador, self._denominador, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
        x, y = signal.dlsim(funcao_transferencia, frame)
        return y

class FiltroFormantes(Filtro):

    def __init__(self, vogal):
        Filtro.__init__(self)
        parametros = params.ParametrosCascata(vogal)
        self._numerador, self._denominador = bloco_formantes(parametros)

class FiltroFontes(Filtro):

    def __init__(self, vogal, av, avs):
        Filtro.__init__(self)
        parametros = params.ParametrosCascata(vogal, av, avs)
        self._numerador, self._denominador = bloco_fonte(parametros)

class FiltroNasal(Filtro):

    def __init__(self, vogal):
        Filtro.__init__(self)
        parametros = params.ParametrosCascata(vogal)
        self._numerador, self._denominador = bloco_nasal(parametros)

class FiltroRadiacao(Filtro):

    def __init__(self):
        Filtro.__init__(self)
        self._numerador, self._denominador = bloco_radiacao()

def calcularabc(bw, f):
    t = ctes.Amostragem.TEMPO_AMOSTRAGEM
    c = -1 * math.exp(-2 * np.pi * bw * t)
    b = 2 * math.exp(-1 * np.pi * bw * t) * math.cos(2 * np.pi * t * f)
    a = 1 - b - c
    return a, b, c

def montar_numden(bw, f):
    a, b, c = calcularabc(bw, f)
    num = [a, 0, 0]
    den = [1, -1*b, -1*c]
    return num, den

def montar_numden_antiressonante(bw, f):
    a, b, c = calcularabc(bw, f)
    a_anti = 1/a
    b_anti = -1*b/a
    c_anti = -1*c*a
    num = [a_anti, b_anti, c_anti]
    den = [1, 0, 0]
    return num, den

def bloco_fonte(parametros):
    num_rgp, den_rgp = montar_numden(ctes.ParametrosConstantes.BGP, ctes.ParametrosConstantes.FGP)
    num_rgs, den_rgs = montar_numden(ctes.ParametrosConstantes.BGS, ctes.ParametrosConstantes.FGS)
    num_rgz, den_rgz = montar_numden_antiressonante(ctes.ParametrosConstantes.BGZ, ctes.ParametrosConstantes.FGZ)
    for indice in range(len(num_rgs)):
        num_rgs[indice] = num_rgs[indice] * parametros.av
    for indice in range(len(num_rgz)):
        num_rgz[indice] = num_rgz[indice] * parametros.avs
    num_paralelo = [num_rgs[0] + num_rgz[0], num_rgz[1], num_rgz[2]]
    den_paralelo = [den_rgz[0] + den_rgs[0], den_rgs[1], den_rgs[2]]
    num_fonte = np.convolve(num_rgp, num_paralelo)
    den_fonte = np.convolve(den_rgp, den_paralelo)
    return num_fonte, den_fonte

def bloco_nasal(parametros):
    num_rnp, den_rnp = montar_numden(ctes.ParametrosConstantes.BNP, ctes.ParametrosConstantes.FNP)
    num_rnz, den_rnz = montar_numden_antiressonante(ctes.ParametrosConstantes.BNZ, parametros.fnz)
    num_nasal = np.convolve(num_rnp, num_rnz)
    den_nasal = np.convolve(den_rnp, den_rnz)
    return num_nasal, den_nasal

def bloco_formantes(parametros):
    num_1, den_1 = montar_numden(parametros.b1, parametros.f1)
    num_2, den_2 = montar_numden(parametros.b2, parametros.f2)
    num_3, den_3 = montar_numden(parametros.b3, parametros.f3)
    num_4, den_4 = montar_numden(parametros.b4, parametros.f4)
    num_5, den_5 = montar_numden(parametros.b5, parametros.f5)
    num = np.convolve(num_1, num_2)
    den = np.convolve(den_1, den_2)
    num = np.convolve(num, num_3)
    den = np.convolve(den, den_3)
    num = np.convolve(num, num_4)
    den = np.convolve(den, den_4)
    num = np.convolve(num, num_5)
    den = np.convolve(den, den_5)
    return num, den

def bloco_radiacao():
    num = [1, 0]
    den = [1, 1]
    return num, den