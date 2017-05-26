"""
Modulo para testes do sintetizador
"""

from synth import utils
import synth.sintetizador as sintetizador
import  synth.parametros as params
import synth.constantes as ctes

def main():
    params.zerar_variacao_f0()
    params.zerar_variacao_k()
    for f0 in range(150, 220, 10):
        for ganhoRuido in range(0,100,5):
            params.setar_ganho_ruido(ganhoRuido/100)
            params.setar_f0(f0)
            filename = 'audios/variacaoApenasRuido/f0='+ str(ctes.ParametrosConstantes.F0) +'-varNoiseOnly-noiseGain='\
                       + str(ctes.Gerais.GANHO_RUIDO)
            sintetizador.sintetizar(filename, 'a')

    params.setar_variacao_f0(0.05)
    for f0 in range(150, 220, 10):
        for ganhoRuido in range(0, 100, 5):
            params.setar_ganho_ruido(ganhoRuido / 100)
            params.setar_f0(f0)
            filename = 'audios/variacaoF0/f0=' + str(ctes.ParametrosConstantes.F0) + '-varf0-noiseGain=' \
                       + str(ctes.Gerais.GANHO_RUIDO) + '-varF0=' + str(ctes.Gerais.VARIACAO_F0)
            sintetizador.sintetizar(filename, 'a')

    params.zerar_variacao_f0()
    params.setar_variacao_k(0.5)
    for f0 in range(150, 220, 10):
        for ganhoRuido in range(0, 100, 5):
            params.setar_ganho_ruido(ganhoRuido / 100)
            params.setar_f0(f0)
            filename = 'audios/variacaoK/f0=' + str(ctes.ParametrosConstantes.F0) + '-varK-noiseGain=' \
                       + str(ctes.Gerais.GANHO_RUIDO) + '-varK=' + str(ctes.Gerais.VARIACAO_K)
            sintetizador.sintetizar(filename, 'a')

if __name__ == "__main__":
    main()
