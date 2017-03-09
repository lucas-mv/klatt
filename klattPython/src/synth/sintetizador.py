"""
Modulo para geracao de som com o sintetizador
"""

import src.synth.forma_onda as forma_onda
import src.synth.constantes as ctes
import src.synth.filtros as filtros

def sintetizar(nome_arquivo):
    numero_frames = int((ctes.Gerais.TEMPO_SIMULACAO/ctes.Amostragem.TEMPO_AMOSTRAGEM)/ctes.Amostragem.AMOSTRAS_FRAME)
    som = forma_onda.Som(nome_arquivo)
    for indice_frame in range(numero_frames):
        trem_impulso = forma_onda.Frame('imp')
        filtro = filtros.Filtro('a', 60, 0)
        frame_filtrado = filtro.filtrar(trem_impulso)
        som.adicionarframe(frame_filtrado)
    som.salvararquivo()