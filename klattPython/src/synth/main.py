"""
Modulo para testes do sintetizador
"""
import src.synth.filtros_ressonantes as fr
from src.synth import utils

def main():
    f0 = 100
    av = 1
    vogal = 'a'
    filtro = fr.montar_filtros(vogal, f0, av)
    utils.plotar_bode(filtro)

if __name__ == "__main__":
    main()