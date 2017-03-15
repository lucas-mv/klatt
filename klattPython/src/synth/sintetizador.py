"""
Modulo para geracao de som com o sintetizador
"""

import src.synth.forma_onda as forma_onda
import src.synth.constantes as ctes
import src.synth.filtros as filtros
import src.synth.fontes as fontes

def sintetizar(nome_arquivo):
    # numero_frames = int((ctes.Gerais.TEMPO_SIMULACAO/ctes.Amostragem.TEMPO_AMOSTRAGEM)/ctes.Amostragem.AMOSTRAS_FRAME)
    som = forma_onda.Som(nome_arquivo)
    # controle_intensidade = fontes.gerar_trapezio(1.0, numero_frames, int(numero_frames*0.1))
    # for indice_frame in range(numero_frames):
    trem_impulso = forma_onda.Frame('imp')
    filtro = filtros.FiltroFontes('a', 60, 0)
    frame_filtrado = filtro.filtrar(trem_impulso)
    # frame_filtrado.modular(controle_intensidade[indice_frame])
    som.adicionarframe(frame_filtrado)
    som.salvararquivo()
    return som