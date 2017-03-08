"""
Modulo para geracao das fontes de ruido e de sonorizacao
"""

import src.synth.constantes as ctes
import random as rnd
import numpy as np
import pandas as pd

class Frame:
    valores = []

    def __init__(self, tipo):
        if(tipo == 'imp'):
            self.valores = gerar_trem_impulsos()
        elif(tipo == 'rnd'):
            self.valores = gerar_ruido_branco()
        elif(tipo == 'pnk'):
            self.valores = gerar_ruido_rosa()
        else:
            self.valores = []

def gerar_trem_impulsos():
    trem_impulsos = []
    for i in range(ctes.Amostragem.AMOSTRAS_FRAME):
        trem_impulsos.append(1.0)
    return trem_impulsos

def gerar_ruido_branco():
    ruido_branco = []
    for i in range(ctes.Amostragem.AMOSTRAS_FRAME):
        ruido_branco.append(rnd.uniform(0.0, 1.0))
    return ruido_branco

def gerar_ruido_rosa():
    """
    Implementado de acordo com a descricao em https://www.dsprelated.com/showarticle/908.php
    """
    array = np.empty((ctes.Amostragem.AMOSTRAS_FRAME, ctes.Amostragem.NUMERO_FONTES_RUIDO_ROSA))
    array.fill(np.nan)
    array[0, :] = np.random.random(ctes.Amostragem.NUMERO_FONTES_RUIDO_ROSA)
    array[:, 0] = np.random.random(ctes.Amostragem.AMOSTRAS_FRAME)

    n = ctes.Amostragem.NUMERO_FONTES_RUIDO_ROSA
    cols = np.random.geometric(0.5, n)
    cols[cols >= ctes.Amostragem.NUMERO_FONTES_RUIDO_ROSA] = 0
    rows = np.random.randint(ctes.Amostragem.AMOSTRAS_FRAME, size=n)
    array[rows, cols] = np.random.random(n)

    df = pd.DataFrame(array)
    df.fillna(method='ffill', axis=0, inplace=True)
    ruido_rosa = df.sum(axis=1).values
    return ruido_rosa

def somar_frames(frame_1, frame_2):
    resultado = []
    for i in range(ctes.Amostragem.AMOSTRAS_FRAME):
        resultado.append(frame_1[i] + frame_2[i])
    frame = Frame('')
    frame.valores = resultado
    return frame
