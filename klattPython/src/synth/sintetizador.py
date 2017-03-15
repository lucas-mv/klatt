"""
Modulo para geracao de som com o sintetizador
"""

import src.synth.forma_onda as forma_onda
import src.synth.constantes as ctes
import src.synth.filtros as filtros
import src.synth.fontes as fontes

def sintetizar(nome_arquivo, vogal):
    som = forma_onda.Som(nome_arquivo)

    filtro_fontes = filtros.FiltroFontes(vogal, 60, 0)
    filtro_nasal = filtros.FiltroNasal(vogal)
    filtro_formantes = filtros.FiltroFormantes(vogal)
    filtro_radiacao = filtros.FiltroRadiacao()

    som._valores = filtro_fontes.filtrar(som._valores)
    som.inverter()
    som._valores = filtro_nasal.filtrar(som._valores)
    som._valores = filtro_formantes.filtrar(som._valores)
    som._valores = filtro_radiacao.filtrar(som._valores)
    som.normalizar()

    som.salvararquivo()
    return som