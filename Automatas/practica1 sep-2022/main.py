from pprint import pprint
from random import randint
import automataParesCerosUnos as filtroPares


def generadorDeCadenas64Bits(cantidad):
    cadenas = ""
    for i in range(cantidad):
        cadena = ""
        for i in range(0,64):
            cadena += str(randint(0,1))
        
        cadenas += cadena + ","
    return cadenas

#Autómata principal

def readyState(bandera):
    if bandera == 1:
        print("conexión exitosa")
        print("generando archivo")

        archivo = open("src/original.txt", "a")
        archivo.write(generadorDeCadenas64Bits(10))
        archivo.close()
        print("archivo generado exitosamente")
        
        print("enviando archivo")
        
        archivo = open("src/original.txt", "r")
        sendingState(archivo)
        
    else:
        exit()

def sendingState(archivo):
    #realicemos primero la funcionalidad, posteriomente revisaremos el timeOut
    pares = ""
    impares = ""

    cadenas = archivo.read().split(",")
    print(cadenas)
    for element in cadenas:
        if filtroPares.estado0(element, 0):
            pares += element + ","
        else:
            impares += element + ","
    
    archivoPares = open("src/pares.txt", "a")
    archivoImpares = open("src/impares.txt", "a")

    archivoPares.write(pares)
    archivoImpares.write(impares)
    return 1


readyState(1)