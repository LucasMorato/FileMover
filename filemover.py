import os

# creating list of files extensions
extensions = []

# looking for to all files inside the script folder
for filename in os.listdir():
    # separating the file name from the extension
    name, ext = os.path.splitext(filename)
    # adding extension to the list if it doesn't already exist
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
