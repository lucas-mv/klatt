"""
Modulo para testes do sintetizador
"""

import src.synth.filtros as fr
from src.synth import utils
import src.synth.sintetizador as sintetizador

def main():
    sintetizador.sintetizar('teste0001.wav')

if __name__ == "__main__":
    main()