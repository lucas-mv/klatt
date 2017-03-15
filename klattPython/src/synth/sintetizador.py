"""
Modulo para geracao de som com o sintetizador
"""

import src.synth.forma_onda as forma_onda
import src.synth.constantes as ctes
import src.synth.filtros as filtros
import src.synth.fontes as fontes

def sintetizar(nome_arquivo):
    som = forma_onda.Som(nome_arquivo)
    trem_impulso = forma_onda.Frame('imp')
    filtro = filtros.FiltroFontes('a', 60, 0)
    frame_filtrado = filtro.filtrar(trem_impulso)
    som.adicionarframe(frame_filtrado)
    som.salvararquivo()
    return som