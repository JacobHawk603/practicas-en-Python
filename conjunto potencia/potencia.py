import numpy as np
import vispy.plot as vp
import librerias.contadorPrimosLib as contador
import math

from asyncore import write

def main():
    archivo = "./listaUnos.txt"

    token = open("./token.txt", "r").read()

    if len(token) == 0:
        token = open("./token.txt", "w")
        token.write('0')
        token.close()
        token = open("./token.txt", "r").read()

    print(token)
    k = int(token)
    #token.close()

    if k >= 23:
        graficar(archivo)


        cadenas64Bits("./conjuntoPotencia.txt")
        graficar("./listaUnos64.txt")

        logaritmo("./unos64.txt")
        graficar("./logaritmo.txt")

        exit()

    else:
        
        m = int(input("ingrese el valor de m: "))
        #k = int(input("ingrese el valor de k: "))

        if k == 0:
            cadena = '{e},{0,1},'
        else:
            cadena = ""
        cadenaBin = ''
        for i in range(k, m-1):
            cadena +='{'
            for j in range(2**(i+2)):
                cadenaBin = '' + bin(j)[2:]
                #print(bin(j)[2:])
                aux = '#0' + str(i+4) + 'b'
                cadena+= format(j, aux)[2:] + ','
            cadena+= '},'

        #print(cadena)
        token = open("./token.txt", "w")
        token.write(str(m-1))
        token.close()


        txt = open("./conjuntoPotencia.txt",'a')
        txt.write(cadena)
        txt.close()

        #aqui
        crearArchivoDeunos(cadena, "./listaUnos.txt")

def crearArchivoDeunos(cadena, archivoDestino):

    #Creamos el archivo txt que contiene la información de los unos que tiene cada elemento del conjunto potencia

    conjuntoPotencia = cadena.replace("}", "")
    conjuntoPotencia = conjuntoPotencia.replace("{", "")
    conjuntoPotencia = conjuntoPotencia.replace(",,", ",")

    arregloBinarios = conjuntoPotencia.split(",")
    arregloContadores = contador.contarUnos(arregloBinarios)
    
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
    print("se ha alcanzado el total de elementos que queremos del conjunto potencia")

def cadenas64Bits(archivo):
    dataset = open(archivo, "r")

    cadena = dataset.read()
    dataset.close()

    cadena = cadena.replace("}", "")
    cadena = cadena.replace("{", "")
    cadena = cadena.replace(",", "")
    cadena = cadena.replace("e", "")

    nuevaCadena = ""

    try:
        for i in range(0,len(cadena), 64):
            for j in range(i, i+64):

                nuevaCadena += cadena[j]
            
            nuevaCadena += ","

    except:
        nuevaCadena = nuevaCadena

    crearArchivoDeunos(nuevaCadena, "./listaUnos64.txt")

    nuevoArchivo = open("./unos64.txt", "w")
    nuevoArchivo.write(nuevaCadena)
    nuevoArchivo.close()

def logaritmo(archivo):

    dataset = open(archivo, "r")

    datos = dataset.read()
    dataset.close()

    nuevCadena = ""

    datosArr = datos.split(",")

    for element in datosArr:
        nuevCadena += str(math.log10(int(element)))
        nuevCadena +=","


    crearArchivoDeunos(nuevCadena, "./listaLogaritmo64.txt")

    nuevoArchivo = open("logaritmo.txt", "w")
    nuevoArchivo.write(nuevCadena)
    nuevoArchivo.close
    


if __name__ == "__main__":

    bandera = "y"

    while(bandera == "y"):
        main()
        bandera = input("calcular otro valor de n? [n/y]")