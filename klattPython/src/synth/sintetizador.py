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
    utils.bode_numerador_denominador(filtro_fontes.numerador, filtro_fontes.denominador, 'FONTE')
    filtro_nasal = filtros.FiltroNasal(vogal)
    utils.bode_numerador_denominador(filtro_nasal.numerador, filtro_nasal.denominador, 'NASAL')
    filtro_formantes = filtros.FiltroFormantes(vogal)
    utils.bode_numerador_denominador(filtro_formantes.numerador, filtro_formantes.denominador, 'FORMANTES')
    filtro_radiacao = filtros.FiltroRadiacao()
    utils.bode_numerador_denominador(filtro_radiacao.numerador, filtro_radiacao.denominador, 'RADIAÇÃO')
    filtro_ruido = filtros.FiltroRuido()
    utils.bode_numerador_denominador(filtro_ruido.numerador, filtro_ruido.denominador, 'RUÍDO')

    som._valores = filtro_fontes.filtrar(som.valores)
    som.inverter()

    ruido = fontes.gerar_ruido_gaussiano()
    ruido_filtrado = filtro_ruido.filtrar(ruido)
    som.somarruido(ruido_filtrado, 0.0)

    som._valores = filtro_nasal.filtrar(som.valores)
    som._valores = filtro_formantes.filtrar(som.valores)
    som._valores = filtro_radiacao.filtrar(som.valores)

    som.normalizar()
    som.modular(fontes.gerar_modulantesenoidal())

    som.salvararquivo()
    return som
