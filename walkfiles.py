import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

key = input('The key of file:\n')
count = 0


def format_size(sizeFile):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if sizeFile < base:
        sizeFile = base
        text = 'B'
    elif sizeFile < kilo:
        sizeFile /= kilo
        text = 'K'
    elif sizeFile < mega:
        sizeFile /= mega
        text = 'M'
    elif sizeFile < giga:
        sizeFile /= giga
        text = 'G'
    elif sizeFile < tera:
        sizeFile /= tera
        text = 'T'
    else:
        sizeFile /= peta
        text = 'P'

    sizeFile = round(sizeFile, 2)
    return f'{sizeFile}{text}'


for root, directory, files in os.walk(ROOT_DIR):
    for file in files:
        if key in file:
            try:
                ROOT = os.path.join(root, file)
                name_File, ext_File = os.path.splitext(file)
                sizeFile = os.path.getsize(ROOT)

                print(f'File: {file}')
                print(f'Path: {ROOT}')
                print(f'Name File: {name_File}')
                print(f'Ext: {ext_File}')
                print(f'Size: {sizeFile}')
                print(f'Formatted Size:', format_size(sizeFile))
                count += 1
            except PermissionError as error:
                print('Not permissions!')
            except FileNotFoundError as error:
                print('File not found!')
            except Exception as error:
                print(error)

print(f'Number of files: {count}')