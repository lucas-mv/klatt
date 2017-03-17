"""
Modulo para geracao de som com o sintetizador
"""

import src.synth.forma_onda as forma_onda
import src.synth.filtros as filtros
import src.synth.fontes as fontes
import src.synth.utils as utils

def sintetizar(nome_arquivo, vogal):
    som = forma_onda.Som(nome_arquivo)

    filtro_fontes = filtros.FiltroFontes(vogal, 60, 0)
    utils.bode_numerador_denominador(filtro_fontes._numerador, filtro_fontes._denominador, 'FONTE')
    filtro_nasal = filtros.FiltroNasal(vogal)
    utils.bode_numerador_denominador(filtro_nasal._numerador, filtro_nasal._denominador, 'NASAL')
    filtro_formantes = filtros.FiltroFormantes(vogal)
    utils.bode_numerador_denominador(filtro_formantes._numerador, filtro_formantes._denominador, 'FORMANTES')
    filtro_radiacao = filtros.FiltroRadiacao()
    utils.bode_numerador_denominador(filtro_radiacao._numerador, filtro_radiacao._denominador, 'RADIAÇÃO')
    filtro_ruido = filtros.FiltroRuido()
    utils.bode_numerador_denominador(filtro_ruido._numerador, filtro_ruido._denominador, 'RUÍDO')


    som._valores = filtro_fontes.filtrar(som._valores)
    som.inverter()
    som._valores = filtro_nasal.filtrar(som._valores)
    som._valores = filtro_formantes.filtrar(som._valores)
    som._valores = filtro_radiacao.filtrar(som._valores)

    som.normalizar()
    som.modular(fontes.gerar_modulantesenoidal())

    som.salvararquivo()
    return som