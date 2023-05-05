import sys
import time

def bits_necesarios(numero):
    numero = numero - 1
    if numero == 0:
        return 1
    else:
        bits = 0
        while numero > 0:
            numero = numero // 2
            bits += 1
        return bits

def buscar_posicion(diccionario, texto):
    return list(diccionario.keys()).index(texto)

def binary_list(m, n):
    result = []
    for i in range(m):
        bin_num = bin(i)[2:].zfill(n)
        result.append(bin_num)
    return result

def binary_list2(m, n):
    result = []
    for i in range(m):
        bin_num = bin(i)[2:].zfill(n)
        result.append("1"*(n-1)+bin_num)
    return result

# Verificamos que se haya proporcionado al menos un argumento
if len(sys.argv) < 2:
    print("Se requiere un archivo como argumento.")
    sys.exit()

# El primer argumento es el nombre del archivo de script
archivo = sys.argv[1]

with open(archivo, 'rb') as f:
    contenido = f.read()

Inicio=time.time()

contenido_hex=contenido.hex()
hex_counts = {hex(byte)[2:].zfill(2): contenido.count(byte) for byte in set(contenido)}
hex_counts = dict(sorted(hex_counts.items(), key=lambda item: item[1], reverse=True))

indice = format(len(hex_counts)-1, '08b')
indice = indice.zfill(8)
tabla = ''.join(hex_counts.keys())
n=bits_necesarios(len(hex_counts))
binarioList_1=binary_list((2**(n-1))-1,n-1)
binarioList_2=binary_list2(len(hex_counts)-(2**(n-1))+1,n)

cons=(2**(n-1))-1
hex_index = {v: k for k, v in enumerate(hex_counts.keys())}

resultado = ''.join([binarioList_1[hex_index.get(contenido_hex[i:i+2])] if hex_index.get(contenido_hex[i:i+2]) < cons else binarioList_2[hex_index.get(contenido_hex[i:i+2]) - cons] for i in range(0, len(contenido_hex), 2)])

ceros=8-(len(resultado)%8)
resultado=("0"*ceros)+resultado
ceros = bin(ceros)[2:].zfill(8)
   
tablanueva = bin(int(tabla, 16))[2:].zfill(len(tabla)*4)
comprimido = indice+ceros+tablanueva+resultado

Fin=time.time()
print("Tiempo de compresión:",(Fin-Inicio))

with open("comprimido.elmejorprofesor", "wb") as archivo:
    archivo.write(bytes(int(comprimido[i:i+8], 2) for i in range(0, len(comprimido), 8)))

