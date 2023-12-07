import numpy as np
import pandas as pd
from librerias_caseras.procesamiento_datasets import valores_observados
from librerias_caseras.herramientas_listas import copiar_lista
from Ocat import Selector, Complejo, Cubrimiento

def binarizar_no_categoricos(lista_valores:list[int | float], one_hot:bool = False, num_columna:int = 1):

    binarizacion:list[list[int]] = []

    labels:list[str] = []
    observados = valores_observados(lista_valores)
    observados.sort()

    for i, valor in enumerate(observados):
        labels.append(f"x{num_columna},{i+1}")

    labels.append(f"valor_real {num_columna}")

    for elemento in lista_valores:
        
        auxiliar:list[int] = []

        for observado in observados:
            
            if one_hot:

                if elemento == observado:
                    auxiliar.append(1)
                else:
                    auxiliar.append(0)

            else:
                if elemento >= observado:
                    auxiliar.append(1)
                else:
                    auxiliar.append(0)

        auxiliar.append(elemento)
        
        binarizacion.append(auxiliar)

    
    dataframe = pd.DataFrame(data=binarizacion, columns=labels)

    return dataframe

def binarizar_categoricos(lista_valores:list[str], numero_columna:int = 1):

    conversion_no_categoricos:list[int] = []
    observados = valores_observados(lista_valores)

    copia_lista_valores:list[str] = copiar_lista(lista_valores)

    for i, observado in enumerate(observados):

        # conversion_no_categoricos.append(i)

        for j, valor in enumerate(copia_lista_valores):
            if valor == observado:

                copia_lista_valores[j] = i

    #ahora realizamos el proceso de binarizado no categorico para obtener el data frame

    dataframe = binarizar_no_categoricos(copia_lista_valores, one_hot=True, num_columna=numero_columna)

    #ahora reemplazamos la columna de valor real por los str

    dataframe = dataframe.drop(f"valor_real {numero_columna}", axis=1)
    observados_dataframe = pd.DataFrame(lista_valores, columns=[f"valor_real {numero_columna}"])
    # print(observados_dataframe)
    dataframe = pd.concat([dataframe, observados_dataframe], axis=1)

    return dataframe

def traducir_cobertura(coberturas:list[list[str]], dataset_binario:pd.DataFrame, identificador_cobertura:str):

    lista_complejos:list[complejo] = []

    for i, complejo_binario in enumerate(coberturas):
        
        lista_selectores:list[Selector] = []

        for selector_binario in complejo_binario:
            etiqueta_traducida:str = f"a{selector_binario[1]}"

            valor_traducido = dataset_binario[dataset_binario[selector_binario] == 1][f"valor_real {selector_binario[1]}"].values.tolist()[0]
            
            #creamos el selector
            selector = Selector(etiqueta_traducida, valor_traducido)
            lista_selectores.append(selector)
        
        complejo = Complejo(i, lista_selectores)
        lista_selectores = []
        lista_complejos.append(complejo)

    cobertura = Cubrimiento(identificador_cobertura, lista_complejos)
        

    return cobertura


if __name__ == "__main__":

    prueba:list = [0.25, 0.75, 1.00, 0.50, 0.75, 1.25, 1.75, 0.25, 1.00, 1.50, 0.50, 1.25, 1.50, 2.25, 1.75, 1.25, 2.25, 2.75, 1.25, 1.75, 2.25]
    prueba2:list[str] = ["hola", "rojo", "azul", "verde", "rojo", "amarillo", "amarillo", "rojo", "verde"]

    data = binarizar_no_categoricos(prueba)

    data2 = binarizar_categoricos(prueba2)

    print(data2)