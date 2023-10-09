import pandas as pd
import random

def extraer_muestra(corpus:pd.DataFrame, target:pd.DataFrame, proporcion:list, tamano_conjunto:int, tamano_muestra:float=0.5):
    '''extrae una muestra lo más significativa posible del conjunto de datos original para su aprendisaje\n\n
        clases: list -> lista de clases totales del conjunto de datos a procesar\n
        corpus: pd.dataframe -> conjunto de datos original\n
        target:pd.dataframe -> conjunto de resultados en función de los datos del corpus
        proporcion: list [clase (str)][proporcion(float)] -> lista que debe sumar 1 en total, y que representa la proporción ideal de la muestra con respecto a sus clases\n
        tamano_muestra : float -> valor entre 0 y 1 que indica que tantos elementos del conjunto original se extraeran en la muestra\n
        tamano_conjunto: int -> total de filas que contiene el conjunto de datos\n\n
        retorna: dataframe -> dataframe con la muestra obtenida del conjunto de datos original

    '''

    elementos_totales_muestra = int(tamano_conjunto * tamano_muestra)

    print(elementos_totales_muestra)

    proporciones_muestra = []

    for element in proporcion:
        proporciones_muestra.append([element[0], int(elementos_totales_muestra*element[1])])

    print(proporciones_muestra)

    muestra_corpus = []
    muestra_target = []
    for element in proporciones_muestra:

        match_datos = []
        match_targets = []

        print(element)

        for x, y in zip(corpus.values, target.values):

            if(element[0] == y):
                match_datos.append(x)
                match_targets.append(y)

        print(len(match_datos), len(match_targets))

        for i in range(element[1]):

            muestra_corpus.append(match_datos.pop(random.randint(0, len(match_datos)-1)))
            muestra_target.append(match_targets.pop(random.randint(0, len(match_targets)-1)))

    muestra_corpus_dataframe = pd.DataFrame(muestra_corpus, columns=corpus.columns)
    muestra_target_dataframe = pd.DataFrame(muestra_target[:])

    # print(muestra_corpus_dataframe)
    # print(muestra_target_dataframe)

    return muestra_corpus_dataframe, muestra_target_dataframe

