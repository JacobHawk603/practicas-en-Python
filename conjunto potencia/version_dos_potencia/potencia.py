import numpy as np
import vispy.plot as vp
import contadorPrimosLib as contador

from asyncore import write

token = open("version_dos_potencia/token.txt", "r").read()

if len(token) == 0:
    token = open("version_dos_potencia/token.txt", "w")
    token.write('0')
    token.close()
    token = open("version_dos_potencia/token.txt", "r").read()

print(token)
k = int(token)
#token.close()

if k >= 9:
    #Aquí se puede poner el algoritmo para plotear con vispy los unos totales.

    txt = open("version_dos_potencia/conjuntoPotencia.txt", "r")
    conjuntoPotencia = txt.read()
    conjuntoPotencia.replace("}", "")
    conjuntoPotencia.replace("{", "")

    arregloBinarios = conjuntoPotencia.split(",")

    arregloContadores = contador.contarUnos(arregloBinarios)

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
    token = open("version_dos_potencia/token.txt", "w")
    token.write(str(m-1))
    token.close()
    txt = open("version_dos_potencia/conjuntoPotencia.txt",'a')
    txt.write(cadena)
    txt.close()
