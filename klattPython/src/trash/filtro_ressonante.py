import numpy as np
import argparse
from scipy import signal, special
import matplotlib.pyplot as plt
import math

def main():
    fs = 10000
    f = 1000
    sample = 200

    x_senoide = np.arange(sample)
    y_senoide = np.sin(2 * np.pi * f * x_senoide / fs)

    BW = 50
    F = 1000
    T = 0.0001
    C = -1*math.exp(-2*np.pi*BW*T)
    B = 2*math.exp(-1*np.pi*BW*T)*math.cos(2*np.pi*T*F)
    A = 1 -B -C

    filtrar_discreto_ressonante(A, B, C, y_senoide, T)

def filtrar_continuo(numerador, denominador, tempo_discreto, data):
    filtro = signal.TransferFunction(numerador, denominador)
    t_out, y, x = signal.lsim(filtro, data, tempo_discreto)

    return t_out, y

def filtrar_discreto_ressonante(A, B, C, data, tempo_amostragem):
    filtro = signal.TransferFunction([A, 0, 0], [1, -1*B, -1*C], dt=tempo_amostragem)

    w, mag, phase = filtro.bode()
    plt.figure()
    plt.semilogx(w, mag)
    plt.title('Bode magnitude plot')

    plt.figure()
    plt.semilogx(w, phase)
    plt.title('Bode phase plot')

    t_out, y = signal.dlsim(filtro, data)

    plt.figure()
    plt.plot(t_out, y)
    plt.title('saida do filtro')

    plt.figure()
    plt.plot(data)
    plt.title('dados de entrada')

    plt.show()

if __name__ == "__main__":
    main()