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
    
#observacion: hay que encerrar este bloque en un bucle para asegurarnos de que el algoritmo no escoja al mismo individuo como padre
#observacion2 : puede ser tambien en lugar del bucle, ir sacando a los individuos que ya fueron seleccionados, pero hay que asegurarse de que la lista de la poblacion sea una copia de la original para evitar que se pierdan los datos de la poblacion real
    #Seleccion del primer padre
    aleatorio = uniform(0,1)

    print("frecuencia acumulada", T)
    for i in range(len(poblacion)):
        if T[i] > aleatorio:
            padres.append(poblacion[i])
            break
    
    #Seleccion del segundo padre
    aleatorio = uniform(0,1)
    for i in range(len(poblacion)):
        if T[i] > aleatorio:
            padres.append(poblacion[i])
            break
#--------------------------------------------------------------------------------------------------

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

    if len(copiaCompetidores) == 0:
        bandera = True

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
            
    if len(copiaCompetidores) == 0:
        bandera = True

    if bandera == True:
        subcampeon = gladiador

    return [campeon, subcampeon]

def fx(genotipo):
    fenotipo = 0
    for i in range (len(genotipo)):
        fenotipo += genotipo[i] * 2**i
    
    funcionX = abs((fenotipo-5)/(2+np.sin(fenotipo)))

    return funcionX

def remplazoGeneracional(poblacion):

    nuevaGeneracion = []
    contador = 0

    pm = 0.1

    while(contador < 5):
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

        #anadimos los ganadores a la nueva poblacion
        for i in range(len(ganadores)):
            nuevaGeneracion.append([ganadores[i][0], ganadores[i][1]])
        
        contador +=1

    print("La nueva generacion:\n\n", np.matrix(nuevaGeneracion))

    return nuevaGeneracion

def main():
    #generamos la problación inicial
    poblacion = []
    nuevaGeneracion = []
    contador = 0
    generacion = 0

    pc = 0.85
    
    for i in range (10):
        generado = generarIndividuo(4)
        objetivo = fx(generado)
        poblacion.append([generado, objetivo])
    
    print("poblacion: \n",np.matrix(poblacion))

    #observemos la funcion objetivo con nuestra poblacion inicial
    #for i in range(len(poblacion)):
    #    poblacion[i].append(fx(poblacion[i]))
    #print("\n\n\n",np.matrix(poblacion))
    
    for generacion in range(10):

        #periodo de cruza
        if uniform(0,1) < pc:
            poblacion = remplazoGeneracional(poblacion)
        else:
            print("La poblacion pasa a la siguiente generacion") #<- observacion: la generacion no deberia de pasar completa, hay que hacer que pasen tanto hijos, como padres, asi que tenemos que aplicar la probabilidad de cruza por cada par de padres
            poblacion = poblacion
    
    print("Esta es la poblacion que quedo 10 generaciones despues: \n\n", np.matrix(poblacion))
        
if __name__ == "__main__":
    main()