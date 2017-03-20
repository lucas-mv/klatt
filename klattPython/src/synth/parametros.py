"""
Definicoes de parametros do sintetizador, geral e generico para varios tipo de vozes.
Os ganhos descritos estão em dB e as frequencias em Hz.
"""

import synth.constantes as ctes


class ParametrosCascata:

    # <editor-fold desc="Propriedades">

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

    @property
    def av(self):
        return self._av

    @property
    def af(self):
        return self._af

    @property
    def ah(self):
        return self._ah

    @property
    def avs(self):
        return self._avs

    @property
    def fnz(self):
        return self._fnz

    @property
    def f0(self):
        return self._f0

    @property
    def f1(self):
        return self._f1

    @property
    def f2(self):
        return self._f2

    @property
    def f3(self):
        return self._f3

    @property
    def f4(self):
        return self._f4

    @property
    def f5(self):
        return self._f5

    @property
    def f6(self):
        return ctes.ParametrosConstantes.F6

    @property
    def a2(self):
        return self._a2

    @property
    def a3(self):
        return self._a3

    @property
    def a4(self):
        return self._a4

    @property
    def a5(self):
        return self._a5

    @property
    def a6(self):
        return self._a6

    @property
    def ab(self):
        return self._ab

    @property
    def b1(self):
        return self._b1

    @property
    def b2(self):
        return self._b2

    @property
    def b3(self):
        return self._b3

    @property
    def b4(self):
        return ctes.ParametrosConstantes.B4

    @property
    def b5(self):
        return ctes.ParametrosConstantes.B5

    @property
    def b6(self):
        return ctes.ParametrosConstantes.B6

    # </editor-fold>

    def __init__(self, vogal, av=None, avs=None):
        if vogal == 'a':
            parametros = ctes.VogalA
            self._b1 = parametros.B1
            self._b2 = parametros.B2
            self._b3 = parametros.B3
            self._f1 = parametros.F1
            self._f2 = parametros.F2
            self._f3 = parametros.F3
        self._f0 = ctes.ParametrosConstantes.F0
        self._av = av
        self._avs = avs
