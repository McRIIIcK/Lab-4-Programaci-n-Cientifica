# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:43:20 2024

@author: McRIIIcK
"""

import pandas as pd
import hashlib
from skimage.feature import peak_local_max

def generar_fingerprint(espectrograma, f, t, nombre_cancion):
    # Encontrar picos locales en el espectrograma
    coordinates = peak_local_max(espectrograma, min_distance=10, threshold_abs=20)
    
    fingerprints = []
    for i in range(len(coordinates) - 1):
        freq1 = f[coordinates[i][0]]
        time1 = t[coordinates[i][1]]
        
        for j in range(i + 1, min(i + 5, len(coordinates))):
            freq2 = f[coordinates[j][0]]
            time2 = t[coordinates[j][1]]
            
            # Crear un hash único para cada par de puntos
            hash_input = f"{int(freq1)}|{int(freq2)}|{int(time2 - time1)}"
            hash_value = hashlib.sha1(hash_input.encode('utf-8')).hexdigest()[:10]
            
            # Añadir el nombre de la canción
            fingerprints.append((hash_value, time1, freq1, nombre_cancion))
    
    return fingerprints

def guardar_fingerprints(fingerprints, output_csv='fingerprints.csv'):
    # Convertir a DataFrame y guardar en CSV
    df = pd.DataFrame(fingerprints, columns=['Hash', 'Tiempo', 'Frecuencia 1', 'Canción'])
    df.to_csv(output_csv, mode='a', header=not pd.io.common.file_exists(output_csv), index=False)

from espectrograma import generar_espectrograma

if __name__ == "__main__":
    espectrograma, f, t = generar_espectrograma("C:/Users/mc18m/Downloads/Aunque yo tenga gata.wav")#ruta cancion .wav
    fingerprints = generar_fingerprint(espectrograma, f, t, "Aunque yo tenga gata")#cancion
    guardar_fingerprints(fingerprints)
