"""
Modulo para guardar os dados da forma de onda gerada e quando possivel adiciona-lo ao arquivo final .wav
"""

import scipy.io.wavfile as wave
import src.synth.constantes as ctes

class Som:
    _arquivo = None
    _wav = None

    def __init__(self, arquivo):
        self._finalizado = True
        self._arquivo = arquivo
        self._wav = []

    def adicionarframe(self, frame):
        for amostra in frame._valores:
            self._wav.append(amostra)

    def salvararquivo(self):
        wave.write(self._arquivo, ctes.Amostragem.TAXA_AMOSTRAGEM, self._wav)
