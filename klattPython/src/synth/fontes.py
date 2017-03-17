"""
Modulo para geracao das fontes de ruido e de sonorizacao
"""

import src.synth.constantes as ctes
import random as rnd
import numpy as np
import pandas as pd
import src.synth.utils as utils

def gerar_trem_impulsos():
    trem_impulsos = []
    frequencia_discreta = ctes.Amostragem.TEMPO_AMOSTRAGEM * ctes.ParametrosConstantes.F0
    tempo_discreto = int(1/frequencia_discreta)
    for i in range(ctes.Amostragem.TOTAL_AMOSTRAS):
        trem_impulsos.append(0.0)
    for i in range(0, ctes.Amostragem.TOTAL_AMOSTRAS, tempo_discreto):
        trem_impulsos[i] = 1.0
    return trem_impulsos

def gerar_ruido_branco():
    ruido_branco = []
    for i in range(ctes.Amostragem.TOTAL_AMOSTRAS):
        ruido_branco.append(rnd.uniform(0.0, 1.0))
    return ruido_branco

def gerar_ruido_gaussiano():
    ruido = list(np.random.normal(ctes.Gerais.CENTRO_RUIDO, ctes.Gerais.DESVIO_PADRAO_RUIDO, ctes.Amostragem.TOTAL_AMOSTRAS))
    ruido = utils.normalizar_01(ruido)
    return ruido

def gerar_ruido_rosa():
    """
    Implementado de acordo com a descricao em https://www.dsprelated.com/showarticle/908.php
    """
    array = np.empty((ctes.Amostragem.TOTAL_AMOSTRAS, ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA))
    array.fill(np.nan)
    array[0, :] = np.random.random(ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA)
    array[:, 0] = np.random.random(ctes.Amostragem.TOTAL_AMOSTRAS)

    n = ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA
    cols = np.random.geometric(0.5, n)
    cols[cols >= ctes.Gerais.NUMERO_FONTES_RUIDO_ROSA] = 0
    rows = np.random.randint(ctes.Amostragem.TOTAL_AMOSTRAS, size=n)
    array[rows, cols] = np.random.random(n)

    df = pd.DataFrame(array)
    df.fillna(method='ffill', axis=0, inplace=True)
    ruido_rosa = df.sum(axis=1).values
    return ruido_rosa

def gerar_modulantesenoidal():
    mod = []
    transicao = int(ctes.Gerais.PORCENTAGEM_MODULACAO_SENOIDAL * ctes.Amostragem.TOTAL_AMOSTRAS / 2)
    for i in range(transicao):
        angulo = (np.pi/2)*i/transicao
        mod.append(np.sin(angulo))
    for i in range(int(ctes.Amostragem.TOTAL_AMOSTRAS-2*transicao)):
        mod.append((1.0))
    for i in range(transicao):
        angulo = (np.pi / 2) * i / transicao
        mod.append(np.cos(angulo))
    return mod
