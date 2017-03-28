"""
Modulo para testes do sintetizador
"""

from synth import utils
import synth.sintetizador as sintetizador
import synth.fontes as fontes


def main():
    utils.plotar(fontes.trem_pulsos_gloticos(0.8, 1.0))
    som = sintetizador.sintetizar('audios/f0=100-modSin-noise', 'a')
    utils.plotar_formaonda(som)
    utils.mostrar_plots()

if __name__ == "__main__":
    main()
