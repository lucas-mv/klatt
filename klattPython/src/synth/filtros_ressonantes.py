"""
Conjunto de codigos que definem o funcionamento dos filtros ressonantes do sintetizador.
"""

import src.synth.parametros as params
import src.synth.constantes as ctes
import math
import numpy as np
from scipy import signal

def calcular_abc(bw, f):
    t = ctes.Amostragem.TEMPO_AMOSTRAGEM
    c = -1 * math.exp(-2 * np.pi * bw * t)
    b = 2 * math.exp(-1 * np.pi * bw * t) * math.cos(2 * np.pi * t * f)
    a = 1 - b - c
    return a, b, c

def montar_num_den(bw, f):
    a, b, c = calcular_abc(bw, f)
    num = [a, 0, 0]
    den = [1, -1*b, -1*c]
    return num, den

def montar_num_den_antiressonante(bw, f):
    a, b, c = calcular_abc(bw, f)
    a_anti = 1/a
    b_anti= -1*b/a
    c_anti = -1*c*a
    num = [a_anti, b_anti, c_anti]
    den = [1, 0, 0]
    return num, den

def montar_filtros(vogal, f0, av):
    parametros = params.ParametrosCascata(vogal, f0, av)
    num_1, den_1 = montar_num_den(parametros.b1, parametros.f1)
    num_2, den_2 = montar_num_den(parametros.b2, parametros.f2)
    num_3, den_3 = montar_num_den(parametros.b3, parametros.f3)
    num_4, den_4 = montar_num_den(parametros.b4, parametros.f4)
    num_5, den_5 = montar_num_den(parametros.b5, parametros.f5)

    num = np.convolve(num_1, num_2)
    den = np.convolve(den_1, den_2)
    num = np.convolve(num, num_3)
    den = np.convolve(den, den_3)
    num = np.convolve(num, num_4)
    den = np.convolve(den, den_4)
    num = np.convolve(num, num_5)
    den = np.convolve(den, den_5)

    # num_rnp, den_rnp = montar_num_den(ctes.ParametrosConstantes.BNP, ctes.ParametrosConstantes.FNP)
    # num_rnz, den_rnz = montar_num_den(ctes.ParametrosConstantes.BNZ, parametros.fnz)
    # num_nasal = np.convolve(num_rnp, num_rnz)
    # den_nasal = np.convolve(den_rnp, den_rnz)
    # num = np.convolve(num_nasal, num)
    # den = np.convolve(den_nasal, den)

    return num, den

