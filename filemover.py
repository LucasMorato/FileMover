import os

# creating list of files extensions
extensions = []

# looking for to all files inside the script folder
for filename in os.listdir():
    # separando o nome do arquivo da extensão
    name, ext = os.path.splitext(filename)
    # adicionando extensão na lista, caso ela ainda não exista
    if ext not in extensions:
        extensions.append(ext)

# creating folder with the extensions names
for ext in extensions:
    if ext != '':
        os.mkdir(ext)

# moving files to the folder
for filename in os.listdir():
    name, ext = os.path.splitext(filename)
    if ext != '':
        os.rename(filename, ext + '/' + filename)
