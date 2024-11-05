# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:45:23 2024

@author: McRIIIcK
"""

from espectrograma import generar_espectrograma
from fingerprint import generar_fingerprint, guardar_fingerprints
from matching import matching

def procesar_cancion(audio_path, db_csv='fingerprints.csv'):
    # Extraer el nombre de la canción del path
    nombre_cancion = audio_path.split("/")[-1]
    print(f"Procesando la canción: {nombre_cancion}")
    
    # Generar espectrograma y fingerprints
    espectrograma, f, t = generar_espectrograma(audio_path)
    fingerprints = generar_fingerprint(espectrograma, f, t, nombre_cancion)
    
    # Guardar fingerprints en la base de datos
    guardar_fingerprints(fingerprints, output_csv=db_csv)
        
    # Buscar coincidencias
    is_match = matching(fingerprints, db_csv)
    if is_match:
        print("¡Coincidencia de canción encontrada!")
    else:
        print("No se encontró ninguna coincidencia.")

# Ejemplo de uso
procesar_cancion("C:/Users/mc18m/Downloads/Ella y yo.wav")
procesar_cancion("C:/Users/mc18m/Downloads/Aunque yo tenga gata.wav")
