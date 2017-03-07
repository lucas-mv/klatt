"""
Definicoes de parametros do sintetizador, geral e generico para varios tipo de vozes.
Os ganhos descritos estão em dB e as frequencias em Hz.
"""

import src.synth.constantes as ctes

class ParametrosSintetizador:
    _av = 0
    _af = 0
    _ah = 0
    _avs = 0
    _fnz = 250
    _f0 = 80
    _f1 = 450
    _f2 = 1450
    _f3 = 2450
    _f4 = 3300
    _f5 = 3750
    _a2 = 0
    _a3 = 0
    _a4 = 0
    _a5 = 0
    _a6 = 0
    _ab = 0
    _b1 = 50
    _b2 = 70
    _b3 = 110

    def __init__(self, vogal, f0, av):
        if(vogal=='a'):
            parametros = ctes.VogalA
            self._b1 = parametros.B1
            self._b2 = parametros.B2
            self._b3 = parametros.B3
            self._f1 = parametros.F1
            self._f2 = parametros.F2
            self._f3 = parametros.F3
        self._f0 = f0
        self._av = av
