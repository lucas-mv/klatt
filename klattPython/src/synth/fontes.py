"""
Modulo para geracao das fontes de ruido e de sonorizacao
"""

import synth.constantes as ctes
import random as rnd
import numpy as np
import pandas as pd
import synth.utils as utils


def trem_impulsos():
    imp = []
    frequencia_discreta = ctes.Amostragem.TEMPO_AMOSTRAGEM * ctes.ParametrosConstantes.F0
    tempo_discreto = int(1/frequencia_discreta)
    for i in range(ctes.Amostragem.TOTAL_AMOSTRAS):
        imp.append(0.0)
    for i in range(0, ctes.Amostragem.TOTAL_AMOSTRAS, tempo_discreto):
        imp[i] = 1.0
    return imp


def ruido_branco():
    noise = []
    for i in range(ctes.Amostragem.TOTAL_AMOSTRAS):
        ruido_branco.append(rnd.uniform(0.0, 1.0))
    return noise


def ruido_gaussiano():
    ruido = list(np.random.normal(ctes.Gerais.CENTRO_RUIDO, ctes.Gerais.DESVIO_PADRAO_RUIDO, ctes.Amostragem.TOTAL_AMOSTRAS))
    ruido = utils.normalizar(ruido)
    return ruido


def onda_quadrada():
    sqr = []
    for i in range(ctes.Amostragem.TOTAL_AMOSTRAS):
        sqr.append(np.sin(2*np.pi*ctes.ParametrosConstantes.F0*i/ctes.Amostragem.TAXA_AMOSTRAGEM))
        if sqr[i] >= 0.0:
            sqr[i] = 1.0
        else:
            sqr[i] = 0.0
    return sqr


def ruido_rosa():
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
    return df.sum(axis=1).values


def modulantesenoidal():
    mod = []
    transicao = int(ctes.Gerais.PORCENTAGEM_MODULACAO_SENOIDAL * ctes.Amostragem.TOTAL_AMOSTRAS / 2)
    for i in range(transicao):
        angulo = (np.pi/2.0)*i/transicao
        mod.append(np.sin(angulo))
    for i in range(int(ctes.Amostragem.TOTAL_AMOSTRAS-2*transicao)):
        mod.append(1.0)
    for i in range(transicao):
        angulo = (np.pi / 2.0) * i / transicao
        mod.append(np.cos(angulo))
    return mod

