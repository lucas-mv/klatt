"""
Modulo para guardar os dados da forma de onda gerada e quando possivel adiciona-lo ao arquivo final .wav
"""

import scipy.io.wavfile as wave
import src.synth.constantes as ctes
import src.synth.fontes as fontes
import numpy as np

class Som:
    _arquivo = None
    _valores = None

    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._valores = fontes.gerar_trem_impulsos()

    def salvararquivo(self):
        wave.write(self._arquivo + '.wav', ctes.Amostragem.TAXA_AMOSTRAGEM, np.asarray(self._valores))

    def modular(self, multiplicador):
        for indice in range(len(self._valores)):
            self._valores[indice] = self._valores[indice] * multiplicador

    def inverter(self):
        self._valores = list(reversed(self._valores))

    def normalizar(self):
        valor_maximo = 0
        for i in range(len(self._valores)):
            if (abs(self._valores[i]) > valor_maximo):
                valor_maximo = abs(self._valores[i])
        for i in range(len(self._valores)):
            self._valores[i] = self._valores[i]/valor_maximo