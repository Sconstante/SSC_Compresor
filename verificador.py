import sys

archivo = sys.argv[1]

with open(archivo, 'rb') as f1, open('descomprimido-elmejorprofesor.txt', 'rb') as f2:
    content1 = f1.read()
    content2 = f2.read()
    content1 =content1.hex()
    content2 =content2.hex()
    if content1 == content2:
        print('ok')
    else:
        print('nok')
