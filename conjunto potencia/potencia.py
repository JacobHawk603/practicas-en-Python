import numpy as np
import vispy.plot as vp
import librerias.contadorPrimosLib as contador

from asyncore import write

token = open("./token.txt", "r").read()

if len(token) == 0:
    token = open("./token.txt", "w")
    token.write('0')
    token.close()
    token = open("./token.txt", "r").read()

print(token)
k = int(token)
#token.close()

if k >= 9:
    #Aquí se puede poner el algoritmo para plotear con vispy los unos totales.

    listaUnos = open("./listaUnos.txt", "r")
    arregloContadores = listaUnos.read().split(",")

    for i in range(len((arregloContadores))-1):
        arregloContadores[i] = int(arregloContadores[i])

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
    print("se ha alcanzo el total de elementos que queremos del conjunto potencia")
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

    #Creamos el archivo txt que contiene la información de los unos que tiene cada elemento del conjunto potencia

    conjuntoPotencia = cadena.replace("}", "")
    conjuntoPotencia = conjuntoPotencia.replace("{", "")
    conjuntoPotencia = conjuntoPotencia.replace(",,", ",")

    arregloBinarios = conjuntoPotencia.split(",")
    arregloContadores = contador.contarUnos(arregloBinarios)
    
    cadenaContadores = ""

    for i in range(len(arregloContadores)-1):
        
        cadenaContadores += str(arregloContadores[i]) + ","

    listaUnos = open("./listaUnos.txt", "a")
    listaUnos.write(cadenaContadores)
    listaUnos.close()