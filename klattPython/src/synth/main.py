"""
Modulo para testes do sintetizador
"""

import src.synth.filtros as filtros
from src.synth import utils
import src.synth.fontes as fontes
import src.synth.sintetizador as sintetizador

def main():
    utils.plotar_amostras(fontes.gerar_trem_impulsos())
    som = sintetizador.sintetizar('audios/fontes')
    utils.plotar_formaonda(som)
    filtro = filtros.FiltroFontes(vogal='a', av=60, avs=0)
    utils.bode_numerador_denominador(filtro._numerador, filtro._denominador)
    utils.mostrar_plots()

if __name__ == "__main__":
    main()