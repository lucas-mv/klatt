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
        wave.write(self._arquivo + '.wav', ctes.Amostragem.TAXA_AMOSTRAGEM, np.asarray(self._wav))

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

def somar_frames(frame_1, frame_2):
    resultado = []
    for i in range(ctes.Amostragem.AMOSTRAS_FRAME):
        resultado.append(frame_1._valores[i] + frame_2._valores[i])
    frame = Frame(resultado)
    return frame