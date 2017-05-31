"""
Modulo para guardar os dados da forma de onda gerada e quando possivel adiciona-lo ao arquivo final .wav
"""

import scipy.io.wavfile as wave
import synth.constantes as ctes
import synth.fontes as fontes
import synth.utils as utils
import numpy as np


class Som:

    _arquivo = None
    _valores = None

    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._valores = fontes.trem_pulsos_gloticos()

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, value):
        self._valores = value

    def salvararquivo(self):
        wave.write(self._arquivo + '.wav', ctes.Amostragem.TAXA_AMOSTRAGEM, np.asarray(self._valores))

    def modular(self, multiplicador):
        for indice in range(len(self._valores)):
            self._valores[indice] = self._valores[indice] * multiplicador[indice]

    def inverter(self):
        self._valores = list(reversed(self._valores))

    def normalizar(self):
        self.valores = utils.normalizar(self.valores)

    def somarruido(self, ruido, ganho_ruido):
        """
        Soma ruido aos valores
        :param ruido: list
        :param ganho_ruido: escalar em dB
        """
        ganho = 10.0**(ganho_ruido/20.0)
        for i in range(len(self._valores)):
            self._valores[i] += (ruido[i] * ganho)

