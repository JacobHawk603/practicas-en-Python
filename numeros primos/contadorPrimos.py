import matplotlib.pyplot as plt
import numpy as np
import vispy.plot as vp
import math


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

def convertirACadena(primos):
    cadenaArr = []
    for i in range(len(primos)):
        cadenaArr.append(bin(primos[i])[2:])
    
    #print(cadenaArr)
    return cadenaArr

def contarUnos(arregloPrimosBinario):
    arregloContadores = []
    for i in range(len(arregloPrimosBinario)):
        contador = 0
        for j in range(len(arregloPrimosBinario[i])):
            if arregloPrimosBinario[i][j] == '1':
                contador += 1
        arregloContadores.append(contador)
    return arregloContadores

def main():

    primos = []
    primosBin = []
    arregloContadoresBinarios = []
    m = int(input("calcular primos hasta: "))
    k = 0
    cadenaContadores = ""
    cadenaBinarios = ""
    cadenaPrimos = ""
    cantidadPrimos = 0

    #creamos el token para facilitar el trabajo a la maquina

    try:
        token = open("./token.txt", "r")
        tokens = token.read().split(",")
        k = int(tokens[0])
        cantidadPrimos = int(tokens[1])
        token.close()
    except:
        k = 2
        print("no hay token, k = 2")

    #creamos el txt con todos los primos que hemos calculado hasta el momento

    try:
        primos = open("./primos.txt", "r").read().split(",")
        primos.pop()

        for i in range(len(primos)):
            primos[i] = int(primos[i])    

        print("el arreglo de primos no esta vacio")
    except:
        print("el arreglo de numeros primos comienza vacío")

    i = k
    while(i < m):

        if encontrarPrimo(primos, i):
            primos.append(i)
            #print(primos)
        
        if i%2==0:
            i+=1
        else:
            i+=2
    #print(primos)
    primosBin = convertirACadena(primos)
    arregloContadoresBinarios = contarUnos(primosBin)
    #print(arregloContadoresBinarios)

    #guardamos los arreglos con los elementos que ya tenemos guardados
    token = open("./token.txt", "w")
    token.write(str(i) + "," + str(len(primos))) #anteriormente le dimos a i el valor de k que es el token inicial, así que i es el token final
    token.close()

    for j in range(cantidadPrimos, len(primos)): #Tenemos que corregir esta parte, esto queda pendiente
        cadenaPrimos += str(primos[j]) + ","

    archivoPrimos = open("./primos.txt", "a")
    archivoPrimos.write(cadenaPrimos)
    archivoPrimos.close()

    for j in range (cantidadPrimos, len(primos)):
        cadenaBinarios += primosBin[j] + ","

    archivoPrimosBinario = open("./primosBin.txt", "a")
    archivoPrimosBinario.write(cadenaBinarios)
    archivoPrimosBinario.close()

    for j in range (cantidadPrimos, len(primos)):
        cadenaContadores += str(arregloContadoresBinarios[j]) + ","

    archivoContadores = open("./contadoresPrimos.txt", "a")
    archivoContadores.write(cadenaContadores)
    archivoContadores.close()



    #antes de plotear, obtenemos el total de los primos que tenemos en el archivo-------------------------------------------

    #ploteo de la grafica

    graficar("./contadoresPrimos.txt")

    logaritmo2("./contadoresPrimos.txt")
    logaritmo10("./contadoresPrimos.txt")

    graficar("./logaritmo2.txt")
    graficar("./logaritmo10.txt")


def logaritmo10(archivo):

    dataset = open(archivo, "r")

    datos = dataset.read()
    dataset.close()

    nuevCadena = ""

    datosArr = datos.split(",")
    datosArr.pop()

    for element in datosArr:
        nuevCadena += str(math.log10(int(element)))
        nuevCadena +=","


    crearArchivoDeunos(nuevCadena, "./listaLogaritmo64.txt")

    nuevoArchivo = open("logaritmo10.txt", "w")
    nuevoArchivo.write(nuevCadena)
    nuevoArchivo.close

def logaritmo2(archivo):

    dataset = open(archivo, "r")

    datos = dataset.read()
    dataset.close()

    nuevCadena = ""

    datosArr = datos.split(",")

    datosArr.pop()

    for element in datosArr:
        nuevCadena += str(math.log2(int(element)))
        nuevCadena +=","


    crearArchivoDeunos(nuevCadena, "./listaLogaritmo64.txt")

    nuevoArchivo = open("logaritmo2.txt", "w")
    nuevoArchivo.write(nuevCadena)
    nuevoArchivo.close


def crearArchivoDeunos(cadena, archivoDestino):

    #Creamos el archivo txt que contiene la información de los unos que tiene cada elemento del conjunto potencia

    conjuntoPotencia = cadena.replace("}", "")
    conjuntoPotencia = conjuntoPotencia.replace("{", "")
    conjuntoPotencia = conjuntoPotencia.replace(",,", ",")

    arregloBinarios = conjuntoPotencia.split(",")
    arregloContadores = contarUnos(arregloBinarios)
    
    cadenaContadores = ""

    for i in range(len(arregloContadores)-1):
        
        cadenaContadores += str(arregloContadores[i]) + ","

    listaUnos = open(archivoDestino, "a")
    listaUnos.write(cadenaContadores)
    listaUnos.close()


def graficar(archivo):
    #Aquí se puede poner el algoritmo para plotear con vispy los unos totales.

    listaUnos = open(archivo, "r")
    arregloContadores = listaUnos.read().split(",")

    for i in range(len((arregloContadores))-1):
        arregloContadores[i] = float(arregloContadores[i])

    arregloContadores.pop()
    #hora de realizar el plot--------------------------------------------------------

    color = (0.3, 0.5, 0.8)
    n_bins = 100

    fig = vp.Fig(show=False)
    line = fig[0:4, 0:4].plot(arregloContadores, symbol='o', width=0,
                            face_color=color + (1,), edge_color=None,
                            marker_size=4)
    line.set_gl_state(depth_test=False)
    fig.show(run=True)

    #fin del plot--------------------------------------------------------------------

if __name__ == "__main__":

    bandera = "y"

    while(bandera == "y"):
        main()
        bandera = input("calcular otro valor de n [n/y]")