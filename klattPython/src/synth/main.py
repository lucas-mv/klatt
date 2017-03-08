"""
Modulo para testes do sintetizador
"""
from mpmath.libmp.libmpf import fone

import src.synth.filtros_ressonantes as fr
from src.synth import utils
import src.synth.fontes as fontes

def main():
    trem_impulsos = fontes.Frame('imp')
    ruido_branco = fontes.Frame('rnd')
    ruido_rosa = fontes.Frame('pnk')

    # f0 = 100
    # av = 1
    # vogal = 'a'
    # num, den = fr.montar_filtros(vogal, f0, av)
    # utils.bode_numerador_denominador(num, den)

    # bw = 50
    # f = 1000
    # num, den = fr.montar_num_den(bw, f)
    # utils.bode_numerador_denominador(num, den)
    #
    # num_anti, den_anti = fr.montar_num_den_antiressonante(bw, f)
    # utils.bode_numerador_denominador(num_anti, den_anti)

if __name__ == "__main__":
    main()