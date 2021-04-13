import os
import shutil

oriPath = os.path.dirname(os.path.abspath(__file__))
newPath = input('\tNew Path: ')
ext = input('\n\text of files: ')

try:
    os.mkdir(newPath)
except FileExistsError as error:
    print(f'Path {newPath} exists!')

for root, dirs, files in os.walk(oriPath):
    for file in files:
        old_FilePath = os.path.join(root, file)
        new_FilePath = os.path.join(newPath, file)

        if ext in file:
            # move, copy or os.remove
            shutil.copy(old_FilePath, new_FilePath)
            print(f'File {file} was copied with success!')


# 'r'  -> Usado somente para ler algo
# 'w'  -> usado somente para escrever algo
# 'w+'  -> usado para ler e escrever arquivo
# 'r+' -> Usado para ler e escrever algo
# 'a+'  -> Usado para acrescentar algo sem apagar

# close file automatically
with open('test.txt', 'w+') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.seek(0,0)
    for line in file:
        print(line, end='')
    os.remove('test.txt')

# finally:
#    file.close()

import json

print('SAVE JSON FILE')
# json file
d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)

with open ('test.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)

#### read json ####
print('READ JSON FILE')
with open ('test.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
    print()