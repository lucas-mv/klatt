"""
Modulo para guardar os dados da forma de onda gerada e quando possivel adiciona-lo ao arquivo final .wav
"""

import scipy.io.wavfile as wave
import src.synth.constantes as ctes
import src.synth.fontes as fontes
import numpy as np

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
        wave.write(self._arquivo, ctes.Amostragem.TAXA_AMOSTRAGEM, np.asarray(self._wav))

class Frame:
    _valores = []

    def __init__(self, parametro):
        if (type(parametro) is str):
            if(parametro == 'imp'):
                self._valores = fontes.gerar_trem_impulsos()
            elif(parametro == 'rnd'):
                self._valores = fontes.gerar_ruido_branco()
            elif(parametro == 'pnk'):
                self._valores = fontes.gerar_ruido_rosa()
            else:
                self._valores = []
        else :
            self._valores = parametro


def somar_frames(frame_1, frame_2):
    resultado = []
    for i in range(ctes.Amostragem.AMOSTRAS_FRAME):
        resultado.append(frame_1._valores[i] + frame_2._valores[i])
    frame = Frame('')
    frame._valores = resultado
    return frame