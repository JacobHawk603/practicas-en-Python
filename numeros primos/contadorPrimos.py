import matplotlib.pyplot as plt
import numpy as np
import vispy.plot as vp


primos = []
primosBin = []
arregloContadoresBinarios = []
m = int(input("inserte el numero maximo de primos: "))
k = 0
cadenaContadores = ""
cadenaBinarios = ""
cadenaPrimos = ""
cantidadPrimos = 0

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
while(len(primos) < m):

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

for j in range(cantidadPrimos, m): #Tenemos que corregir esta parte, esto queda pendiente
    cadenaPrimos += str(primos[j]) + ","

archivoPrimos = open("./primos.txt", "a")
archivoPrimos.write(cadenaPrimos)
archivoPrimos.close()

for j in range (cantidadPrimos, m):
    cadenaBinarios += primosBin[j] + ","

archivoPrimosBinario = open("./primosBin.txt", "a")
archivoPrimosBinario.write(cadenaBinarios)
archivoPrimosBinario.close()

for j in range (cantidadPrimos, m):
    cadenaContadores += str(arregloContadoresBinarios[j]) + ","

archivoContadores = open("./contadoresPrimos.txt", "a")
archivoContadores.write(cadenaContadores)
archivoContadores.close()



#antes de plotear, obtenemos el total de los primos que tenemos en el archivo-------------------------------------------

arregloContadoresBinarios = open("./contadoresPrimos.txt", "r").read().split(",")
arregloContadoresBinarios.pop()


#ploteo de la grafica---------------------------------------------------------------------------------------------------

# make the data
'''np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))

# size and color:
sizes = np.random.uniform(15, 80, len(primos))
colors = np.random.uniform(15, 80, len(arregloContadoresBinarios))

# plot
fig, ax = plt.subplots()

ax.scatter(primos, arregloContadoresBinarios, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=primos,
       ylim=(0, 8), yticks=np.arange(1, 20))

plt.show()'''

#otra forma de pleatar los primos--------------------------------------------------------------------------------------

color = (0.3, 0.5, 0.8)
n_bins = 100

fig = vp.Fig(show=False)
line = fig[0:4, 0:4].plot(arregloContadoresBinarios, symbol='o', width=0,
                          face_color=color + (1,), edge_color=None,
                          marker_size=4)
line.set_gl_state(depth_test=False)
fig.show(run=True)