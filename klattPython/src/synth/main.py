"""
Modulo para testes do sintetizador
"""

import src.synth.filtros as filtros
from src.synth import utils
import src.synth.sintetizador as sintetizador

def main():
    sintetizador.sintetizar('teste-todos-av-avs')
    filtro = filtros.Filtro('a', 60, 0)
    utils.bode_numerador_denominador(filtro._numerador, filtro._denominador)

if __name__ == "__main__":
    main()