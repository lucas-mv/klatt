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

def trem_pulsos_gloticos(porcentagem_glotal, k):
    pulsos = []
    periodo_discreto = int(1.0 / (ctes.Amostragem.TEMPO_AMOSTRAGEM * ctes.ParametrosConstantes.F0))
    num_pulsos = int(ctes.Amostragem.TOTAL_AMOSTRAS/periodo_discreto)
    for pulso in range(num_pulsos):
        pulso_glot = pulso_glotico(porcentagem_glotal, k)
        for amostra in range(len(pulso_glot)):
            pulsos.append(pulso_glot[amostra])
    return pulsos


def pulso_glotico(porcentagem_glotal, k):
    """
    Implementado segundo FANT, 1979, Vocal source analysis - a progress report
    :param porcentagem_glotal: porcentagem do periodo fundamental que forma o periodo do pulso glotico
    :param k: parametro do metodo descrito, nos da a queda do pulso
    :return: list
    """
    pulso = []
    tempo_discreto = int(1.0 / (ctes.Amostragem.TEMPO_AMOSTRAGEM * ctes.ParametrosConstantes.F0))
    wg = ctes.ParametrosConstantes.F0 * 2.0 * np.pi / porcentagem_glotal
    t_subida = int(np.pi * ctes.Amostragem.TAXA_AMOSTRAGEM / wg)
    t_descida = int(((1.0/wg) * np.arccos((k - 1.0) / k)) * ctes.Amostragem.TAXA_AMOSTRAGEM)
    t_vazio = int(tempo_discreto - t_subida - t_descida)
    for i in range(t_subida):
        u = 0.5 * (1.0 - np.cos(wg * i / ctes.Amostragem.TAXA_AMOSTRAGEM))
        pulso.append(u)
    for i in range(t_descida):
        u = (k * np.cos(wg * i / ctes.Amostragem.TAXA_AMOSTRAGEM) - k + 1.0)
        pulso.append(u)
    ruido = ruido_gaussiano(t_vazio)
    for i in range(t_vazio):
        pulso.append(ruido[i])
    return pulso

def ruido_branco():
    noise = []
    for i in range(ctes.Amostragem.TOTAL_AMOSTRAS):
        ruido_branco.append(rnd.uniform(0.0, 1.0))
    return noise


def ruido_gaussiano(numero_amostras):
    ruido = list(np.random.normal(ctes.Gerais.CENTRO_RUIDO, ctes.Gerais.DESVIO_PADRAO_RUIDO, numero_amostras))
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

