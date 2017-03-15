"""
Modulo para geracao das fontes de ruido e de sonorizacao
"""

import src.synth.constantes as ctes
import random as rnd
import numpy as np
import pandas as pd

def gerar_trem_impulsos():
    trem_impulsos = []
    frequencia_discreta = ctes.Amostragem.TEMPO_AMOSTRAGEM * ctes.ParametrosConstantes.F0
    tempo_discreto = int(1/frequencia_discreta)
    for i in range(ctes.Amostragem.AMOSTRAS_FRAME):
        trem_impulsos.append(0.0)
    for i in range(0, ctes.Amostragem.AMOSTRAS_FRAME, tempo_discreto):
        trem_impulsos[i] = 1.0
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
    array = np.empty((ctes.Amostragem.AMOSTRAS_FRAME, ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA))
    array.fill(np.nan)
    array[0, :] = np.random.random(ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA)
    array[:, 0] = np.random.random(ctes.Amostragem.AMOSTRAS_FRAME)

    n = ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA
    cols = np.random.geometric(0.5, n)
    cols[cols >= ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA] = 0
    rows = np.random.randint(ctes.Amostragem.AMOSTRAS_FRAME, size=n)
    array[rows, cols] = np.random.random(n)

    df = pd.DataFrame(array)
    df.fillna(method='ffill', axis=0, inplace=True)
    ruido_rosa = df.sum(axis=1).values
    return ruido_rosa

def gerar_trapezio(valor_maximo, total_amostras, amostras_transicao):
    trapezio = []
    passo_transicao = valor_maximo/amostras_transicao
    amostras_completas = total_amostras - 2*amostras_transicao
    for indice in range(amostras_transicao):
        trapezio.append(indice*passo_transicao)
    for indice in range(amostras_completas):
        trapezio.append(valor_maximo)
    for indice in range(amostras_transicao):
        trapezio.append(valor_maximo - indice*passo_transicao)
    return trapezio
