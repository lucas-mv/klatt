from scipy import signal
import matplotlib.pyplot as plt
import src.synth.constantes as ctes

def bode_numerador_denominador(num, den):
    filtro = signal.TransferFunction(num, den, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
    plotar_bode(filtro)

def plotar_bode(funcao_transferencia):
    w, mag, phase = funcao_transferencia.bode()
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(w, mag)
    axarr[0].set_title('BODE - MAGNITUDE')
    axarr[0].set_ylabel('dB')
    axarr[1].plot(w, phase)
    axarr[1].set_title('BODE - FASE')
    axarr[1].set_xlabel('Hz')
    axarr[1].set_ylabel('Graus')

def plotar_formaonda(som):
    plt.figure()
    plt.plot(som._wav)
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