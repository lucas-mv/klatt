from scipy import signal
import matplotlib.pyplot as plt
import src.synth.constantes as ctes

def bode_numerador_denominador(num, den):
    filtro = signal.TransferFunction(num, den, dt=ctes.Amostragem.TEMPO_AMOSTRAGEM)
    plotar_bode(filtro)

def plotar_bode(funcao_transferencia):
    w, mag, phase = funcao_transferencia.bode()
    plt.figure()
    plt.semilogx(w, mag)
    plt.title('Bode magnitude plot')

    plt.figure()
    plt.semilogx(w, phase)
    plt.title('Bode phase plot')

    plt.show()
