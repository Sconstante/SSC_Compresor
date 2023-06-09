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

with open("comprimido.elmejorprofesor", 'rb') as archivo:
    contenido = archivo.read()

Inicio=time.time()

contenido_hex=contenido.hex()
indice_hex=contenido_hex[0:2]
indice=int(indice_hex, 16)+1
contenido_bin=bin(int(contenido_hex, 16))[2:].zfill(len(contenido_hex)*4)
tabla=contenido_hex[4:(indice+2)*2]
n=bits_necesarios(indice)
lista_tabla = [tabla[i:i+2] for i in range(0, len(tabla), 2)]
resultado=contenido_bin[8*(indice+2):]
ceros=int(contenido_hex[2:4], 16)
resultado=resultado[ceros:]

n=n-1
unos = "1"*n
i = 0
descomprimido = ""

while i < len(resultado):
    if resultado[i:i+len(unos)] == unos:
        lectura = 2*n+1
        posbin=(resultado[i+n:i+lectura])
        pos=int(posbin, 2) + (2**(n)-1)
        descomprimido+= lista_tabla[pos]

    else:
        lectura = n
        posbin=(resultado[i:i+lectura])
        pos=int(posbin, 2)
        descomprimido+= lista_tabla[pos]
    i += lectura

bytes_data = bytes.fromhex(descomprimido)

Fin=time.time()
print("Tiempo de descompresión:",(Fin-Inicio))

# Escribir los bytes en el archivo binario
with open("descomprimido-elmejorprofesor.txt", "wb") as file:
    file.write(bytes_data)