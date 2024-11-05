# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:44:56 2024

@author: McRIIIcK
"""

import pandas as pd

def matching(query_fingerprints, db_csv='fingerprints.csv'):
    # Cargar la base de datos
    db_fingerprints = pd.read_csv(db_csv)
    matches = []
    
    # Fuerza bruta para encontrar coincidencias de hashes
    for q_hash, q_time, _, _ in query_fingerprints:
        match = db_fingerprints[db_fingerprints['Hash'] == q_hash]
        if not match.empty:
            matches.append((q_hash, q_time, match['Tiempo'].values[0]))
    
    # Evaluación del match basado en el número de coincidencias
    threshold = 10  
    return len(matches) >= threshold

from fingerprint import generar_fingerprint, guardar_fingerprints
from espectrograma import generar_espectrograma

if __name__ == "__main__":
    espectrograma, f, t = generar_espectrograma("C:/Users/mc18m/Downloads/Aunque yo tenga gata.wav")
    fingerprints = generar_fingerprint(espectrograma, f, t, "Aunque yo tenga gata")
    guardar_fingerprints(fingerprints)
    print("Coincidencia:", matching(fingerprints))
