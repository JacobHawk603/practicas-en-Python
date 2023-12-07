import pandas as pd

def copiar_lista(lista:list):

    copia:list = []

    for elemento in lista:
        auxiliar = elemento

        copia.append(auxiliar)
    
    return copia

def list_to_series_conjuntivas(lista:list[str], dataframe:pd.DataFrame):

    sentencia:pd.Series = (dataframe[lista[0]] == 1)

    for i, elemento in enumerate(lista):
        if i == 0:
            continue
        sentencia = sentencia & (dataframe[elemento] == 1)

    return sentencia

def list_to_series_disyuntivas(lista:list[list[str]], dataframe:pd.DataFrame):

    sentencia:pd.Series = list_to_series_conjuntivas(lista[0], dataframe)

    for i, sublista in enumerate(lista):
        
        if i == 0:
            continue
        
        sentencia = sentencia | list_to_series_conjuntivas(sublista, dataframe)

    return sentencia

