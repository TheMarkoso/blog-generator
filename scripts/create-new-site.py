import os
import shutil
import argparse


def create_directory_structure(base_directory, subdirectories, files_to_copy, folder_to_copy, source_path):
    try:
        # Crea el directorio base
        os.makedirs(base_directory, exist_ok=True)
        print(f"Directorio '{base_directory}' creado exitosamente.")

        # Crear subdirectorios
        for subdir in subdirectories:
            subdir_path = os.path.join(base_directory, subdir)
            os.makedirs(subdir_path, exist_ok=True)
            print(f"Sudirectorio '{subdir_path}' creado.")

        # Copiar archivos individuales
        for file in files_to_copy:
            src_file_path = os.path.join(source_path,file)
            dest_file_path = os.path.join(base_directory, file)
            shutil.copy(src_file_path, dest_file_path)
            print(f"Archivo '{file}' copiado a '{dest_file_path}'.")

        # Copiar una carpeta completa
        if folder_to_copy:
            src_folder_path = os.path.join(source_path, folder_to_copy)
            dest_folder_path = os.path.join(base_directory, folder_to_copy)
            shutil.copy(src_folder_path, dest_folder_path)
            print(f"Archivo '{folder_to_copy}' copiado a '{dest_folder_path}'.")


    except Exception as e:
        print(f"Ocurrio un Error: {e}")


def main():
    # Configuracion de argparse
    parser = argparse.ArgumentParser(description="Crea el directorio de tu sitio web")
    parser.add_argument('command', choices=['new-site'], help="Crea un nuevo sitio.")
    parser.add_argument('site_name', help="Nombre del nuevo sitio(carpeta) a crear.")

    # Parsear los agumentos
    args = parser.parse_args()

    if args.command == 'new-site':
        home_directory = os.environ['HOME']
        base_directory = os.path.join(home_directory, args.site_name)

        # Rutas definidas
        source_path = "/home/markoso17/Code/projects/blog-generator/templates"
        files_to_copy = ['about.html', 'index.html', 'posts-list.html']
        folder_to_copy = None

        # Subdirectorios a crear
        subdirectories = ['posts']

        # Crea la estructura de directorios y copia los archivos
        create_directory_structure(base_directory, subdirectories, files_to_copy, folder_to_copy, source_path)


if __name__ == '__main__':
    main()
