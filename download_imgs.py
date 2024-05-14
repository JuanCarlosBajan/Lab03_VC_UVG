import requests
import os

def descargar_imagenes_github(url, ruta_destino):
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
    
    # Obtener la lista de archivos en el directorio del repositorio
    respuesta = requests.get(url)
    archivos = respuesta.json()  # La respuesta es una lista de diccionarios

    # Descargar cada archivo
    for archivo in archivos:
        if archivo['type'] == 'file' and archivo['name'].endswith(('.jpg', '.png')):
            download_url = archivo['download_url']  # URL directa para descargar el archivo
            respuesta_imagen = requests.get(download_url)
            nombre_archivo = archivo['name']
            with open(os.path.join(ruta_destino, nombre_archivo), 'wb') as f:
                f.write(respuesta_imagen.content)

# URL de la API de GitHub para listar archivos en un directorio
url_api = "https://api.github.com/repos/BIDS/BSDS500/contents/BSDS500/data/images/test?ref=master"
ruta_destino = './Descargas_BSDS500/imgs'

descargar_imagenes_github(url_api, ruta_destino)
