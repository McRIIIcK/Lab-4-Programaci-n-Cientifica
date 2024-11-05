# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:41:20 2024

@author: McRIIIcK
"""

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generar_espectrograma(audio_path, window_size=2048, hop_size=1024):
    # Cargar el archivo de audio
    sr, audio = wavfile.read(audio_path)

    # Verificar que audio no sea mono y convertirlo si es necesario
    if len(audio.shape) > 1:
        audio = audio[:, 0]

    # Calcular el espectrograma utilizando la STFT
    f, t, Zxx = scipy.signal.stft(audio, fs=sr, nperseg=window_size, noverlap=window_size - hop_size)

    # Convertir magnitud en dB y mostrar espectrograma
    espectrograma = np.abs(Zxx)
    plt.imshow(10 * np.log10(espectrograma + 1e-10), origin='lower', aspect='auto', extent=[t.min(), t.max(), f.min(), f.max()])
    plt.title("Espectrograma")
    plt.xlabel("Tiempo")
    plt.ylabel("Frecuencia")
    plt.colorbar(label="Amplitud (dB)")
    plt.show()

    return espectrograma, f, t

if __name__ == "__main__":
    generar_espectrograma("C:/Users/mc18m/Downloads/Aunque yo tenga gata.wav")#ruta de la cancion .wav
