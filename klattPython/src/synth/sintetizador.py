"""
Modulo para geracao de som com o sintetizador
"""

import synth.forma_onda as forma_onda
import synth.filtros as filtros
import synth.fontes as fontes
import synth.utils as utils


def sintetizar(nome_arquivo, vogal):
    som = forma_onda.Som(nome_arquivo)
    # utils.plotar(som.valores, 'PULSOS INICIAIS', 'AMOSTRAS', 'INTENSIDADE')

    filtro_nasal = filtros.FiltroNasal(vogal)
    filtro_formantes = filtros.FiltroFormantes(vogal)
    filtro_radiacao = filtros.FiltroRadiacao()

    som.valores = filtro_nasal.filtrar(som.valores)
    # utils.plotar(som.valores, 'PULSOS FILTRO NASAL', 'AMOSTRAS', 'INTENSIDADE')
    som.valores = filtro_formantes.filtrar(som.valores)
    # utils.plotar(som.valores, 'PULSOS FILTRO FORMANTES', 'AMOSTRAS', 'INTENSIDADE')
    som.valores = filtro_radiacao.filtrar(som.valores)
    # utils.plotar(som.valores, 'PULSOS FILTRO RADIACAO', 'AMOSTRAS', 'INTENSIDADE')

    som.normalizar()
    som.modular(fontes.modulantesenoidal(len(som.valores)))

    som.salvararquivo()
    return som
