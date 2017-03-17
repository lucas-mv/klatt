"""
Modulo para testes do sintetizador
"""

from klattPython.src.synth import utils
import klattPython.src.synth.sintetizador as sintetizador

def main():
    som = sintetizador.sintetizar('audios/f0=100-modSin','a')
    utils.plotar_formaonda(som)
    utils.mostrar_plots()

if __name__ == "__main__":
    main()