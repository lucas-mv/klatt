"""
Modulo para testes do sintetizador
"""

import src.synth.filtros as filtros
from src.synth import utils
import src.synth.fontes as fontes
import src.synth.sintetizador as sintetizador

def main():
    utils.plotar_amostras(fontes.gerar_trem_impulsos())
    som = sintetizador.sintetizar('teste-todos-av-avs-fontemelhorada-controleintensidade-002')
    utils.plotar_formaonda(som)
    filtro = filtros.Filtro('a', 60, 0)
    utils.bode_numerador_denominador(filtro._numerador, filtro._denominador)
    # filtro_formantes = filtros.FiltroFormantes()
    # utils.plotar_amostras(filtro_formantes.degrau())
    utils.mostrar_plots()

if __name__ == "__main__":
    main()