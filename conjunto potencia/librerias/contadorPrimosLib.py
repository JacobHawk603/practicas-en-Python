import matplotlib.pyplot as plt
import numpy as np
import vispy.plot as vp


def encontrarPrimo(primos, numero):
    bandera = True

    if numero < 3:
        return bandera
    else:
        for i in range(round(np.sqrt(numero))-1):
            if numero % primos[i] == 0:
                bandera = False
                break
        return bandera

def convertirACadena(arregloNumeros):
    cadenaArr = []
    for i in range(len(arregloNumeros)):
        cadenaArr.append(bin(arregloNumeros[i])[2:])
    
    #print(cadenaArr)
    return cadenaArr

def contarUnos(arregloBinarios):
    arregloContadores = []
    for i in range(len(arregloBinarios)):
        contador = 0
        for j in range(len(arregloBinarios[i])):
            if arregloBinarios[i][j] == '1':
                contador += 1
        arregloContadores.append(contador)
    return arregloContadores
