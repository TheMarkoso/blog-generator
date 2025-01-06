import os
import markdown

#Define el directorio de salida

output_dir = 'posts'

#Crear e directorio si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Obtener todos los archivos del directorio actual
for element in os.listdir():
    #verifica si son markdown
    if element.endswith('.md'):
        #lee el archivo 
        with open(element, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        #convierte el contenio md a hmtl
        htlm_content = markdown.markdown(md_content)

        #Creael nombre del archivo html a partir del markdown
        html_filename = os.path.join(output_dir, os.path.splitext(element)[0] + '.html')

        # Guarda el archivo html en el directorio de salida
        with open(html_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(htlm_content)

        print(f"Archivo convertido: {element} -> {html_filename}")

print("Conversion completa")
