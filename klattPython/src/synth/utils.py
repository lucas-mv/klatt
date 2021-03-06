from scipy import signal
import matplotlib.pyplot as plt
import synth.constantes as ctes
import numpy as np


def bode_numerador_denominador(num, den, titulo):
    filtro = signal.TransferFunction(num, den, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
    plotar_bode(filtro, titulo)


def plotar_bode(funcao_transferencia, titulo):
    w, mag, phase = funcao_transferencia.bode()
    for i in range(len(w)):
        w[i] /= np.pi * 2000
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
    plt.plot(som.valores)
    plt.title('ONDA SONORA OBTIDA')
    plt.xlabel('AMOSTRAS')
    plt.ylabel('INTENSIDADE')


def plotar(amostras, titulo='', xlabel='', ylabel='', tipo='lin'):
    plt.figure()
    if tipo == 'lin':
        plt.plot(range(len(amostras)), amostras)
    elif tipo == 'sctr':
        plt.scatter(range(len(amostras)), amostras)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def mostrar_plots():
    plt.show()


def maximo_absoluto(vetor):
    maximo = 0
    for i in range(len(vetor)):
        if abs(vetor[i]) > maximo:
            maximo = abs(vetor[i])
    return maximo


def normalizar(serie):
    norm = []
    maximo = maximo_absoluto(serie)
    for i in range(len(serie)):
        norm.append(serie[i] / maximo)
    return norm


def plotar_histograma(serie):
    count, bins, ignored = plt.hist(serie, 30, normed=True)
    mu, sigma = ctes.Gerais.CENTRO_RUIDO, ctes.Gerais.DESVIO_PADRAO_RUIDO
    plt.plot(bins, 1 (sigma * np.sqrt(2 * np.pi))*np.exp(- (bins - mu)**2/(2 * sigma ** 2)), linewidth=2, color='r')


def modular_amplitude(sinal, modulante):
    mod = []
    for i in range(len(sinal)):
        mod.append(sinal[i]*modulante[i])
    return mod


def modular_escalar(sinal, escalar):
    mod = []
    for valor in sinal:
        mod.append(valor*escalar)
    return mod
