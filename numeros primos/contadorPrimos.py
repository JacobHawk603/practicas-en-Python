import matplotlib.pyplot as plt
import numpy as np

primos = []
primosBin = []
arregloContadoresBinarios = []
m = int(input("inserte el numero maximo de primos: "))

def encontrarPrimo(primos, numero):
    bandera = True
    for i in range(len(primos)):
        if numero % primos[i] == 0:
            bandera = False
            break
    return bandera

def convertirACadena(primos):
    cadenaArr = []
    for i in range(len(primos)):
        cadenaArr.append(bin(primos[i])[2:])
    
    print(cadenaArr)
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

i = 2
while(len(primos) < m):

    if encontrarPrimo(primos, i):
        primos.append(i)
        #print(primos)
    
    i+=1
print(primos)
primosBin = convertirACadena(primos)
arregloContadoresBinarios = contarUnos(primosBin)
print(arregloContadoresBinarios)

#ploteo de la grafica---------------------------------------------------------------------------------------------------

# make the data
np.random.seed(3)
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

plt.show()