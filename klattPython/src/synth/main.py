"""
Modulo para testes do sintetizador
"""

import src.synth.filtros as filtros
from src.synth import utils
import src.synth.sintetizador as sintetizador

def main():
    som = sintetizador.sintetizar('teste-todos-av-avs-fontemelhorada-controleintensidade')
    utils.plotar_formaonda(som)
    filtro = filtros.Filtro('a', 60, 0)
    utils.bode_numerador_denominador(filtro._numerador, filtro._denominador)
    utils.mostrar_plots()

if __name__ == "__main__":
    main()