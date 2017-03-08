"""
Constantes de uso geral no módulo sintetizador. Os ganhos descritos estão em dB e as frequencias em Hz.
"""

class Amostragem:
    AMOSTRAS_FRAME = 50
    TAXA_AMOSTRAGEM = 10000  #Hz
    TEMPO_AMOSTRAGEM = 0.0001  #s
    TEMPO_SIMULACAO = 2  #s
    NUMERO_FONTES_RUIDO_ROSA = 1

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
    BGS = 200

class VogalA:
    F1 = 620
    F2 = 1220
    F3 = 2550
    B1 = 80
    B2 = 50
    B3 = 140

