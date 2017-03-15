from scipy import signal
import matplotlib.pyplot as plt
import src.synth.constantes as ctes
import numpy as np

def bode_numerador_denominador(num, den, titulo):
    filtro = signal.TransferFunction(num, den, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
    plotar_bode(filtro, titulo)

def plotar_bode(funcao_transferencia, titulo):
    w, mag, phase = funcao_transferencia.bode()
    for i in range(len(w)):
        w[i] = w[i]/(2*np.pi*1000)
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(w, mag)
    axarr[0].set_title('BODE - MAGNITUDE: ' + titulo)
    axarr[0].set_ylabel('dB')
    axarr[1].plot(w, phase)
    axarr[1].set_title('BODE - FASE')
    axarr[1].set_xlabel('kHz')
    axarr[1].set_ylabel('Graus')

def plotar_formaonda(som):
    plt.figure()
    plt.plot(som._valores)
    plt.title('ONDA SONORA OBTIDA')
    plt.xlabel('AMOSTRAS')
    plt.ylabel('INTENSIDADE')

def plotar_amostras(amostras):
    plt.figure()
    plt.plot(range(len(amostras)), amostras)
    plt.title('AMOSTRAS UTILIZADAS POR FRAME')
    plt.xlabel('AMOSTRAS')
    plt.ylabel('INTENSIDADE')

def mostrar_plots():
    plt.show()