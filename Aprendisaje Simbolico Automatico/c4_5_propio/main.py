from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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


def ejemplo_quinlan():
    #primero realicemos una prueba de id3 con el ejemplo de quinlan para ver si vamos por buen camino

    df = pd.read_excel("./ejemplo_quinlan_faltantes.ods")
    print(df)

    # preprocesamos para limpiar datos nulos

    df = df.fillna('missing')

    #separamos el corpus en X y target (y)

    X = df.drop('Decision', axis=1)
    y = df['Decision']

    print(X)
    print("\n\n", y)

    #obteniendo la entropia de la muestra
    y_pos = 0
    y_neg = 0

    print(y.values, X['Outlook'].values)

    for desicion, atribute in zip(y.values, X['Outlook'].values):
        if(desicion == 'Yes' and atribute != 'missing'):
            y_pos += 1
        elif(desicion == 'No' and atribute != 'missing'):
            y_neg +=1

    print(y_pos, y_neg)

    m = entropia([y_pos, y_neg])
    print("entropia de la muestra: ",m)

    # calculemos la entropia de la una de las ramas y con eso tenemos para saber que todo va en orden
    clima_S = [0, 0]
    clima_N = [0, 0]
    clima_LL = [0,0]

    for element, decicion in zip(df['Outlook'], df['Decision']):
        print(element)
        if element == 'Sunny' and decicion == 'Yes':
            clima_S[0] += 1
        elif element == 'Sunny' and decicion == 'No':
            clima_S[1] +=1
        if element == 'Overcast' and decicion == 'Yes':
            clima_N[0] += 1
        elif element == 'Overcast' and decicion == 'No':
            clima_N[1] +=1
        if element == 'Rain' and decicion == 'Yes':
            clima_LL[0] += 1
        elif element == 'Rain' and decicion == 'No':
            clima_LL[1] +=1

    print(clima_S, clima_N, clima_LL)

    entropia_clima = entropia_de_Atributo([clima_S, clima_N, clima_LL])

    print(entropia_clima)

    return 0

def credit_aproval():

    # Vamos a comenzar por importar el dataset directamente desde python

    # fetch dataset
    credit_approval = fetch_ucirepo(id=27)

    # data (as pandas dataframes)
    X = credit_approval.data.features
    y = credit_approval.data.targets

    # Vamos llenar datos faltantes como una cadena "missing"
    X_limpio = X.dropna()
    y_limpio = y.dropna()

    X = X.fillna('missing')
    y = y.fillna('missing')

    # metadata
    print(credit_approval.metadata)

    # variable information
    print(credit_approval.variables)

    print(X, y)

    #comencemos con obtener la entropia del dataset (entropia general o entropia de la muestra)
    contador = 0
    y_pos = 0
    y_neg = 0
    for row, target in zip(X.values, y.values):
        print(row)

        hayFaltantes = False
        for element in row:
            if(element == 'missing'):
                hayFaltantes = True

        if(not hayFaltantes and target != 'missing'):
            contador +=1

            if(target == '+'):
                y_pos += 1
            elif(target == '-'):
                y_neg += 1

    print(contador, y_pos, y_neg)

    M_aparente = entropia([y_pos, y_neg])   #entropia calculada con los elementos sin datos faltantes en toda la muestra

    #calculemos las entropias por cada uno de los atributos de cada una de las clases
    clases = X.columns.values

    #por cada una de las clases vamos a identificar todos los tributos que contienen
    matriz_clases = []
    for i in range(len(clases)):
        matriz_clases.append([clases[i]])
        print("len({})".format(len(matriz_clases)))
        arr_auxiliar = []
        for element in X_limpio[clases[i]]:

            en_la_matriz = False

            for j in range(len(arr_auxiliar)):
                # print(j)
                if(arr_auxiliar[j] == element):
                    en_la_matriz = True

            if(not en_la_matriz):
                arr_auxiliar.append(element)

        matriz_clases[i].append(arr_auxiliar)

    print(clases, "\n\n clases: \n\n", matriz_clases)

    return 0

if __name__ == "__main__":

    credit_aproval()