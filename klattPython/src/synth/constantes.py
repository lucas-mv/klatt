"""
Constantes de uso geral no módulo sintetizador. Os ganhos descritos estão em dB e as frequencias em Hz.
"""


class Gerais:
    NUMERO_FONTES_RUIDO_ROSA = 1
    TEMPO_SIMULACAO = 2  # s
    PORCENTAGEM_MODULACAO_SENOIDAL = 0.2
    DESVIO_PADRAO_RUIDO = 0.1
    CENTRO_RUIDO = 0.0
    VARIACAO_F0 = 0.05
    VARIACAO_K = 0.5
    GANHO_RUIDO = 0.5


class Amostragem:
    TAXA_AMOSTRAGEM = 10000  # Hz
    TEMPO_AMOSTRAGEM = 1/TAXA_AMOSTRAGEM  # s
    TOTAL_AMOSTRAS = TAXA_AMOSTRAGEM * Gerais.TEMPO_SIMULACAO


class ParametrosConstantes:
    AN = 0
    A1 = 0
    F6 = 4900
    B4 = 250
    B5 = 200
    B6 = 1000
    FGP = 0
    BGP = 100
    FGZ = 1500
    BGZ = 600
    FNP = 250
    BNP = 100
    BNZ = 100
    FGS = 0
    BGS = 200
    F0 = 220


class VogalA:
    F1 = 620
    F2 = 1220
    F3 = 2550
    B1 = 80
    B2 = 50
    B3 = 140

