# Proyecto de Reconocimiento de Canciones

Este proyecto implementa un sistema de reconocimiento de canciones basado en huellas digitales (fingerprints). Utiliza espectrogramas y hashes para almacenar y comparar características únicas de cada canción.

## Estructura de Archivos
- **espectrograma.py**: Genera espectrogramas a partir de archivos de audio.
- **fingerprint.py**: Crea fingerprints de cada espectrograma.
- **matching.py**: Compara fingerprints para buscar coincidencias en la base de datos.
- **main.py**: Ejecuta el flujo completo: generación, almacenamiento y búsqueda de coincidencias.

## Instrucciones de Uso
1. Sube tus archivos `.wav` al directorio adecuado.
2. Ejecuta `main.py` para procesar las canciones y almacenar los resultados.
3. Consulta el archivo `fingerprints.csv` generado para ver los datos almacenados.

## Mejoras propuestas
Algunas mejoras incluyen la optimización del almacenamiento y la eficiencia en la búsqueda de coincidencias.
