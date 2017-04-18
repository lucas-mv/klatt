"""
Modulo para geracao de som com o sintetizador
"""

import synth.forma_onda as forma_onda
import synth.filtros as filtros
import synth.fontes as fontes
import synth.utils as utils


def sintetizar(nome_arquivo, vogal):
    som = forma_onda.Som(nome_arquivo)
    utils.plotar(som.valores, 'PULSOS INICIAIS', 'AMOSTRAS', 'INTENSIDADE')

    filtro_nasal = filtros.FiltroNasal(vogal)
    # utils.bode_numerador_denominador(filtro_nasal.numerador, filtro_nasal.denominador, 'NASAL')
    filtro_formantes = filtros.FiltroFormantes(vogal)
    # utils.bode_numerador_denominador(filtro_formantes.numerador, filtro_formantes.denominador, 'FORMANTES')
    filtro_radiacao = filtros.FiltroRadiacao()
    # utils.bode_numerador_denominador(filtro_radiacao.numerador, filtro_radiacao.denominador, 'RADIAÇÃO')

    # filtro_ruido = filtros.FiltroRuido()
    # utils.bode_numerador_denominador(filtro_ruido.numerador, filtro_ruido.denominador, 'RUÍDO')
    # ruido = filtro_ruido.filtrar(fontes.ruido_gaussiano())
    # ruido = utils.normalizar(ruido)
    # ruido = utils.modular_amplitude(ruido, fontes.onda_quadrada())
    # utils.plotar(ruido, 'RUIDO', 'AMOSTRAS', 'INTENSIDADE')
    # som.somarruido(ruido, -6.0)

    som.valores = filtro_nasal.filtrar(som.valores)
    utils.plotar(som.valores, 'PULSOS FILTRO NASAL', 'AMOSTRAS', 'INTENSIDADE')
    som.valores = filtro_formantes.filtrar(som.valores)
    utils.plotar(som.valores, 'PULSOS FILTRO FORMANTES', 'AMOSTRAS', 'INTENSIDADE')
    som.valores = filtro_radiacao.filtrar(som.valores)
    utils.plotar(som.valores, 'PULSOS FILTRO RADIACAO', 'AMOSTRAS', 'INTENSIDADE')

    som.normalizar()
    som.modular(fontes.modulantesenoidal(len(som.valores)))

    som.salvararquivo()
    return som
