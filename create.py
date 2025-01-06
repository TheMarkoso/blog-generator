import os
import argparse
from datetime import datetime

# Directorio donde se guarda los post
DIRECTORIO_MD = './posts'

# Crealo si no existe
if not os.path.exists(DIRECTORIO_MD):
    os.makedirs(DIRECTORIO_MD)

def format_title(filename):
    title = os.path.splitext(filename)[0]
    return title.replace('-', ' ')

# Configuracion de argparse
parser = argparse.ArgumentParser(description="Crear un archivo Markdown en el directorio 'post'.")
parser.add_argument('action', choices=['new'], help="Accion a realizar: 'new' para crear un archivo nuevo.")
parser.add_argument('filename', help="Nombre del Archivo.")

# Parsear los argumentos
args = parser.parse_args()

# Accion para crear un nuevo archivo Markdown
if args.action == 'new':
    # Obten el nombre del archivo
    filename = args.filename
    # Asegurate de que el nombre no termine en .md 
    if not filename.endswith('.md'):
        filename += '.md'

    # Formate el titulo
    title = format_title(filename)

    # Crea la ruta completa del archivo
    file_path = os.path.join(DIRECTORIO_MD, filename)


    # Verifica si el archivo existe
    if os.path.exists(file_path):
        print(f"Error: El archivo '{filename}' ya existe en el directorio '{DIRECTORIO_MD}'.")
    else:
        #Crear la cabecera YAML con metadatos
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #Fecha y hora actual

        yaml_header = f"""---
title: {title}
date: {current_time}
---
"""


        # Crea y escribe un contenido basico en el archivo Markdown
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(yaml_header)
            file.write(f"# {title}\n")
        print(f"Archivo '{filename}' creado exitosamente en '{DIRECTORIO_MD}'.")


