"""
Modulo para geracao de som com o sintetizador
"""

import src.synth.forma_onda as forma_onda
import src.synth.constantes as ctes
import src.synth.filtros as filtros
import src.synth.fontes as fontes

def sintetizar(nome_arquivo, vogal):
    som = forma_onda.Som(nome_arquivo)
    trem_impulso = forma_onda.Frame('imp')

    filtro_fontes = filtros.FiltroFontes(vogal, 60, 0)
    filtro_nasal = filtros.FiltroNasal(vogal)
    filtro_formantes = filtros.FiltroFormantes(vogal)
    filtro_radiacao = filtros.FiltroRadiacao()

    frame_filtrado = filtro_fontes.filtrar(trem_impulso)
    frame_filtrado.inverter()
    frame_filtrado = filtro_nasal.filtrar(frame_filtrado)
    frame_filtrado = filtro_formantes.filtrar(frame_filtrado)
    frame_filtrado = filtro_radiacao.filtrar(frame_filtrado)
    frame_filtrado.normalizar()

    som.adicionarframe(frame_filtrado)
    som.salvararquivo()
    return som