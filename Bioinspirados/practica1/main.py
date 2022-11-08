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
    hijosFX = []

    arregloAleatorio = []

    for i in range(len(padres[0][0])):
        arregloAleatorio.append(uniform(0,1))

    print ("\n\n",arregloAleatorio, "\n\n")

    for i in range(len(padres[0][0])):
        if arregloAleatorio[i] <= umbral:
            hijos[0].append(padres[0][0][i])
            hijos[1].append(padres[1][0][i])
        else:
            hijos[1].append(padres[0][0][i])
            hijos[0].append(padres[1][0][i])
    
    #calculamos y asignamos la funcion objetivo de los hijos
    for i in range(len(hijos)):
        objetivo = fx(hijos[i])
        hijosFX.append([hijos[i], objetivo])

    return hijosFX


def selPadresRuleta(poblacion):
    t = []
    T = []
    objetivo = []
    objetivoTotal = 0
    aleatorio = 0
    padres = []

    #evalucacion de individuos
    for i in range (len(poblacion)):
        objetivo.append(poblacion[i][1])
    
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

    print("frecuencia acumulada", T)
    for i in range(len(poblacion)):
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

def mutar(individuo, pm):
    #creamos la variable aleatoria
    aleatoria = []
    objetivo = 0

    for i in range(len(individuo[0])):
        aleatoria.append(uniform(0,1))

    print ("\n\n",aleatoria, "\n\n")
    #comparar individuo con la variable aleatoria
    for i in range(len(individuo)):
        if aleatoria[i] <= pm:
            if individuo[0][i] == 0:
                individuo[0][i] = 1
            else:
                individuo[0][i] = 0
    
    #calculamos la nueva funcion objetivo para el individuo mutado
    objetivo = fx(individuo[0])
    individuo[1] = objetivo
    #no requiere retorno ya que se está modificando desde la memoria

def remplazoDePadresMasDebiles(competidores):

    print("los competidores: ", competidores)

    campeon = []
    subcampeon = []
    bandera = False
    copiaCompetidores = []

    for i in range(len(competidores)):
        copiaCompetidores.append(competidores[i])
    

    for i in range(len(competidores)):
        
        if(bandera == False):

            gladiador = copiaCompetidores.pop(0)
            print ("el gladiador del momento:", gladiador)
            
            for j in range(len(copiaCompetidores)):
                if gladiador[1] < copiaCompetidores[j][1]:
                    break
                else:
                    bandera = True
        else:
            break

    if bandera == True:
        campeon = gladiador
        competidores.remove(gladiador)
    
    print("Este es el gladiador ganador",gladiador)

    #elegimos al segundo mejor
    bandera = False
    copiaCompetidores.clear()
    for i in range(len(competidores)):
        copiaCompetidores.append(competidores[i])
    
    
    print("los competidores que quedan: ", copiaCompetidores)

    for i in range(len(competidores)):
    
        if(bandera == False):

            gladiador = copiaCompetidores.pop(0)
            print ("el gladiador del momento:", gladiador)
            
            for j in range(len(copiaCompetidores)):
                if gladiador[1] < copiaCompetidores[j][1]:
                    break
                else:
                    bandera = True
        else:
            break
            
    
    if bandera == True:
        subcampeon = gladiador

    return [campeon, subcampeon]

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
        generado = generarIndividuo(4)
        objetivo = fx(generado)
        poblacion.append([generado, objetivo])
    
    print("poblacion: \n",np.matrix(poblacion))

    #observemos la funcion objetivo con nuestra poblacion inicial
    #for i in range(len(poblacion)):
    #    poblacion[i].append(fx(poblacion[i]))
    #print("\n\n\n",np.matrix(poblacion))
    
    #periodo de cruza
    if uniform(0,1) < pc:
        #seleccion de padres
        padres = selPadresRuleta(poblacion)
        print("los padres son:\n ", np.matrix(padres))    

        hijos = cruzaUniforme(padres)
        print("Los hijos son:\n", np.matrix(hijos))

        #mutamos a los hijos resultantes
        print ('hijos sin mutar: ', np.matrix(hijos))
        for i in range(len(hijos)):
            mutar(hijos[i], pm)
        print('hijos mutados: ', np.matrix(hijos))

        #aplicamos la seleccion de padres mas debiles
        for i in range(len (hijos)):
            padres.append(hijos[i])
        ganadores = remplazoDePadresMasDebiles(padres)
        print("los ganadores : ", ganadores)
        
if __name__ == "__main__":
    main()