from scipy import signal
import matplotlib.pyplot as plt
import klattPython.src.synth.constantes as ctes
import numpy as np

def bode_numerador_denominador(num, den, titulo):
    filtro = signal.TransferFunction(num, den, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
    plotar_bode(filtro, titulo)

def plotar_bode(funcao_transferencia, titulo):
    w, mag, phase = funcao_transferencia.bode()
    for i in range(len(w)):
        w[i] = w[i]/(2*np.pi*1000)
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].semilogx(w, mag)
    axarr[0].set_title('BODE - MAGNITUDE: ' + titulo)
    axarr[0].set_ylabel('dB')
    axarr[1].semilogx(w, phase)
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

def maximo_absoluto(vetor):
    maximo = 0
    for i in range(len(vetor)):
        if(abs(vetor[i]) > maximo):
            maximo = abs(vetor[i])
    return maximo

def normalizar_01(serie):
    norm = []
    maximo = maximo_absoluto(serie)
    for i in range(len(serie)):
        norm[i] = (serie[i] / maximo) + 1.0
    maximo = maximo_absoluto(norm)
    for i in range(len(norm)):
        norm[i] = norm[i] / maximo
    return norm

def plotar_histograma(serie):
    count, bins, ignored = plt.hist(serie, 30, normed=True)
    mu, sigma = ctes.Gerais.CENTRO_RUIDO, ctes.Gerais.DESVIO_PADRAO_RUIDO
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')