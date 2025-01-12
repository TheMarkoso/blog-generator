import os
import yaml
from datetime import datetime
from markdown import markdown
from jinja2 import Environment, FileSystemLoader


POSTS_PATH = './posts'
POSTS_TEMPLATES_PATH = './templates'
OUTPUT_HTML = 'post.html'

template_loader = FileSystemLoader(searchpath=POSTS_TEMPLATES_PATH)
template_env = Environment(loader=template_loader)

def get_md_files():
    files = []
    for filename in os.listdir(POSTS_PATH):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_PATH, filename)
            files.append(filepath)
    return files


def get_metadata(filepath):
    all_data = []
    for file in filepath:
        with open(file, 'r', encoding='utf-8') as file:
            content= file.read()

            if content.startswith('---'):
                parts = content.split('---',2)
                data = parts[1].strip()
                lines = data.split('\n')
                result = {}
                
                for line in lines:
                    if ': ' in line:
                        key, value = line.split(': ',1)
                        if key == 'date':
                            value = value.split(' ')[0]
                        result[key] = value
                final_result = {k: result[k] for k in ('title','date')}
                
                all_data.append(final_result)
    return all_data


def create_items_post(data):
    template = template_env.get_template('posts.html')
    list_items = []
    rendered_html = ''
    for item in data:
        title = item['title']
        date = item['date']
        list_item = f"\t<li><span> * {date}  --  </span><a>{title}</a></li>"
        list_items.append(list_item)

        content = "\n".join(list_items)

        rendered_html = template.render(content=content)

    return rendered_html


def main():
    #obtenes los archivos .md de un directorio
    files = get_md_files()
    #print(f"Lista de archivos .md del directorio {POSTS_PATH}")
    #print(f"{files}\n")

    # Lee cada archivo y crea una lista con diccionarios con los metadatos de c/u
    metadata = get_metadata(files)
    #print("Metadatos obtenidos de los Archivos markdown")
    #print(f"{metadata}\n")

    sorted_data = sorted(metadata, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
    #print("Lista de metadatos ordenado por fecha")
    #print(f'{sorted_data}\n')


    #print('Lista de post en html')
    post = create_items_post(sorted_data)
    #print(f"{post}\n")

    if os.path.exists(OUTPUT_HTML):
        print(f"El Archivo '{OUTPUT_HTML}' ya esxiste. Sera sobrescrito.")

    # Guarda el contenido de html_content en un archivo
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as output_file:
        output_file.write(post)

    print(f"Archivo '{OUTPUT_HTML}' generado con exito.")



if __name__ == '__main__':
    main()
