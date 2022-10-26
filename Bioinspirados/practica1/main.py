from random import randint
from random import uniform
import numpy as np


def generarIndividuo(tamanoGenotipo):
    individuo = []

    for i in range(tamanoGenotipo):
        individuo.append(randint(0,1))
    
    return individuo

def cruza(padres):
    punto = 2 #<- entero para indicar en que posicion del arreglo se va a fraccionar el cromosoma
    hijos = np.array(2)

    hijos[0] = []
    hijos[1] = []

    for i in range(punto):
        hijos[0].append(padres[0][i])
        hijos[1].append(padres[1][i])
    
    for j in range(punto, len(hijos)):
        hijos[0].append(padres[1][j])
        hijos[1].append(padres[0][j])

    return hijos

def cruzaUniforme(padres):
    umbral = 0.5
    hijos = [[],[]]

    arregloAleatorio = []

    for i in range(len(padres[0])):
        arregloAleatorio.append(uniform(0,1))

    for i in range(len(padres[0])):
        if arregloAleatorio[i] <= umbral:
            hijos[0].append(padres[0][i])
            hijos[1].append(padres[1][i])
        else:
            hijos[1].append(padres[0][i])
            hijos[0].append(padres[1][i])
    
    return hijos


def selPadresRuleta(poblacion):
    t = []
    T = []
    objetivo = []
    objetivoTotal = 0
    aleatorio = 0
    padres = []

    #evalucacion de individuos
    for individuo in poblacion:
        objetivo.append(fx(individuo))
    
    #Obtencion de frecuencias relativas
    objetivoTotal = np.sum(objetivo)

    for element in objetivo:
        t.append(element / objetivoTotal)
        
    #obtencion de frecuencia absoluta
    acumulada = 0
    for frecuencia in t:
        print("frecuencia relativa: ", frecuencia)
        acumulada += frecuencia
        T.append(acumulada)
    
    #Seleccion del primer padre
    aleatorio = uniform(0,1)
    for i in range(len(poblacion)):
        print("frecuencia acumulada", T)
        if T[i] < aleatorio and T[i+1] > aleatorio:
            padres.append(poblacion[i+1])
            break
    
    #Seleccion del segundo padre
    aleatorio = uniform(0,1)
    for i in range(len(poblacion)):
        if T[i] < aleatorio and T[i+1] > aleatorio:
            padres.append(poblacion[i+1])
            break


    return padres

def fx(genotipo):
    fenotipo = 0
    for i in range (len(genotipo)):
        fenotipo += genotipo[i] * 2**i
    
    funcionX = abs((fenotipo-5)/(2+np.sin(fenotipo)))

    return funcionX

def main():
    #generamos la problación inicial
    poblacion = []

    pc = 0.85
    pm = 0.1
    
    for i in range (10):
        poblacion.append(generarIndividuo(4))
    
    print("poblacion: \n",np.matrix(poblacion))

    #observemos la funcion objetivo con nuestra poblacion inicial
    for individuo in poblacion:
        print(fx(individuo))
    
    #periodo de cruza
    if uniform(0,1) < pc:
        #seleccion de padres
        padres = selPadresRuleta(poblacion)
        print("los padres son:\n ", np.matrix(padres))    

        hijos = cruzaUniforme(padres)
        print("Los hijos son:\n", np.matrix(hijos))
        
if __name__ == "__main__":
    main()