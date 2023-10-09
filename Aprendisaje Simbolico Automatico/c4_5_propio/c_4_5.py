import numpy as np
import pandas as pd

def entropia(clases:np.ndarray, tamano_muestra:int=None):
    '''Clases -> np.ndarray que contiene los elementos por clase con los que se va a calcular la entropia\n
        (opcional) tamano_muestra -> int: tamaño de de la muestra que se proporciona, si no se especifica este atributo, se asume que los
        elementos de las ramas conforman el total de la muestra, y con ese valor se generará la entropia de clase o de la muestra
    '''
    i = 0   #<- Entropia, no un contador de for

    if(tamano_muestra == None):
        m = 0

        #calculamos el total de los elementos de cada clase
        for clase in clases:
            m+=clase
    else:
        m = tamano_muestra


    #calculamos la entropía
    for clase in clases:
        # print("m del error: ", m)
        if clase != 0:
            i+=(-(clase/m) * np.log2(clase/m))  #<- Importante, debe de ser logaritmo de base 2 para que de el resultado visto en clase

    return float(i)

def entropia_de_Atributo(ramas:np.ndarray, tamano_muestra:int=None):
    '''ramas -> np.ndarray que contiene los elementos por cada decicion posible del algoritmo con los que se va a calcular la entropia\n
        (opcional) tamano_muestra -> int: tamaño de de la muestra que se proporciona, si no se especifica este atributo, se asume que los
        elementos de las ramas conforman el total de la muestra, y con ese valor se generará la entropia del atributo
    '''
    i = 0

    if(tamano_muestra == None):
        m = 0

        for rama in ramas:
            m +=rama[0] + rama[1]
    else:
        m = tamano_muestra

    for rama in ramas:
        print(rama)
        i += ((rama[0] + rama[1])/m) * entropia(rama)

    return float(i)

def ganancia(entropia_general, entropia_atributo):
    return entropia_general - entropia_atributo

def ganancia_aparente(entropia_general:float, entropia_atributo:float, total_elementos:int, elementos_sin_faltantes:int):
    return float((elementos_sin_faltantes/total_elementos) * (entropia_general - entropia_atributo))


def proporcion_de_ganancia(gan:float, i:float):
    '''gan -> float64: ganancia del atributo o tambien la ganancia aparente, dependiendo las circunstancias\n
        i -> float64 entropia del atributo\n\n

        retorna: float64 -> proporción de ganancia para el atributo

    '''

    return float(gan/i)

def valores_observados(valores_observados:list):

    '''Permite conocer todos los diferentes valroes que hay en una sola columna del dataset \n\n
        valores_obsetvados -> list: lista que contiene los valures de una columna específica del dataframe\n\n
        Retorna: lista con los diferentes valores observados en la columna estudidada
    '''

    valores = []

    for valor in valores_observados:
        en_valores = False

        if(len(valores) == 0):
            valores.append(valor)

        else:

            for i in range(len(valores)):

                if(valores[i] == valor):
                    en_valores = True
            
            if(not en_valores):
                valores.append(valor)

    return valores

def repeticiones_de_valor(valor, valores_observados:list):
    '''Permite conocer que tantas veces se repite un valor observado dentro de la columna\n\n
        Returna: int -> numero total de repeticiones
    '''

    contador = 0

    for elemento in valores_observados:
        if(valor == elemento):
            contador +=1
    
    return contador

def aptitud(cardinalidad_mas_frecuente:tuple[int, int], cardinalidad_muestra:int):


    return (cardinalidad_mas_frecuente[0]+cardinalidad_mas_frecuente[1])/(2*cardinalidad_muestra)


def intervalo_particion(valores_observados:tuple[str, list[tuple[float, int]]], corpus:np.ndarray, targets:list):

    '''retorna los intervalos en los que se va a particionar el atributo no categorico\n\n
        valores_observados ->tuple[str, list[tuple[float, int]]] : tupla que contiene el atributo, y los valores_observados del atributo, así como sus
        repeticiones de cada uno\n
        corpus -> dataframe con el cual vamos a hacer match de los valores_observados\n
        targets -> dataframe con los valores y del dataframe
    '''

    #ordenamos los valores de menor a mayor

    valores = []

    for tupla in valores_observados[1]:
        valores.append(tupla[0])
            
    valores.sort()

    print(valores)

    #ya estan ordenados los valores, ahora, hay que definir los intervalos, identificando a que clase pertenecen cada uno de ellos

    tupla_valor_clase = []
    corpus_list = corpus.tolist()
    print(corpus_list)

    print("el tipo de dato: ", type(corpus))
    print(corpus_list.index(valores[0]))

    for valor in valores:
        tupla_valor_clase.append([valor, targets[corpus_list.index(valor)]])

    print(tupla_valor_clase)

    # ahora que tenemos la lista de tuplas, vamos a agrupar en dos intervalos, y vamos a identificar la agrupación con mejor aptitud

    la_mejor_particion = []
    razon_de_particion = 0.2
    aptitud_particion = 0

    while(razon_de_particion < 0.9):
    
        particion = particionar(tupla_valor_clase, razon_de_particion)

        print(particion)

        #ahora que obtuvimos la particion evaluamos su aptitud para saber se trata de la mejor o hay una mejor

        es_mejor_particion, aptitud_particion, repeticiones = evaluar_particion(particion, aptitud_particion)

        if(es_mejor_particion):
            la_mejor_particion = particion

        razon_de_particion += 0.1

    #creamos la etiqueta del intervalo de particion
    etiqueta = ['<= {}'.format(la_mejor_particion[0][len(la_mejor_particion[0])-1][0]), '> {}'.format(la_mejor_particion[0][len(la_mejor_particion[0])-1][0])]


    return [etiqueta, la_mejor_particion], repeticiones

def particionar(lista:list[tuple[float, str]], razon_particion:float=0.5):

    clases = [[],[]]
    num_elementos_clase1 = int(len(lista) * razon_particion)-1

    for i in range(num_elementos_clase1):
        clases[0].append(lista[i])
    
    for i in range(num_elementos_clase1, len(lista)):
        clases[1].append(lista[i])
    

    return clases

def evaluar_particion(particion:tuple[list[tuple[float, str]], list[tuple[float, str]]], mejor_aptitud:float):
    
    positivos = []
    negativos = []
    observados = []

    repeticiones_clase1 = []
    repeticiones_clase2 = []

    for tupla in particion[0]:
        observados.append(tupla[1])

    print("linea 200, observados; ",observados)

    #identificamos el total de elementos por clase de la primer particion

    clases = valores_observados(observados)
    print(clases)

    for clase in clases:

        repeticiones_clase1.append(repeticiones_de_valor(clase, observados))

    #limpiamos el arreglo de observados y aplicamos el mismo proceso para la segunda particion
    observados.clear()
    
    for tupla in particion[1]:
        observados.append(tupla[1])
    
    for clase in clases:

        repeticiones_clase2.append(repeticiones_de_valor(clase, observados))

    print("valores por clase de la particion; ", repeticiones_clase1, repeticiones_clase2)

    #seleccionamos la clase màs frecuente
    print("repeticiones de clase1:", repeticiones_clase1)
    print("repeticiones de clase 2: ", repeticiones_clase2)

    if len(repeticiones_clase1) < 2:
        cardinalidad_clase_1 = repeticiones_clase1[0]
    else:
      cardinalidad_clase_1 = repeticiones_clase1[0] + repeticiones_clase1[1]  

    if len(repeticiones_clase2) < 2:
        cardinalidad_clase_2 = repeticiones_clase2[0]
    else:
        cardinalidad_clase_2 = repeticiones_clase2[0] + repeticiones_clase2[1]
    
    

    clase_mayor = []

    if cardinalidad_clase_1 > cardinalidad_clase_2:
        clase_mayor = repeticiones_clase1
    else:
        clase_mayor = repeticiones_clase2

    # ahora que tenemos la clase mas frecuente, evaluamos su aptitud


    aptitud_particion = aptitud(clase_mayor, (cardinalidad_clase_1 + cardinalidad_clase_2))

    print("la clase mas frecuente es: ", clase_mayor)
    print("la aptitud es: ", aptitud_particion)

    if(aptitud_particion > mejor_aptitud):

        print("repeticiones de la actual mejor clase: ", repeticiones_clase1, repeticiones_clase2)

        return True, aptitud_particion, [repeticiones_clase1, repeticiones_clase2]
    
    else:
        return False, mejor_aptitud, [repeticiones_clase1, repeticiones_clase2]