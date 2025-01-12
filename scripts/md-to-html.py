import markdown

#Abrir el archivo Markdown 
with open('./file.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

#Conventir el contenido Markdown a HTML
html_content = markdown.markdown(md_content)

#Guardar el contenido HTML en un archivo
with open('file.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print("Convension completa")
