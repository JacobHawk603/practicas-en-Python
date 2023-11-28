import numpy as np
import pandas as pd
from librerias_caseras.procesamiento_datasets import valores_observados

def binarizado_no_categoricos(lista_valores:list[int | float]):

    binarizacion:list[list[int]] = []

    labels:list[str] = []
    observados = valores_observados(lista_valores)
    observados.sort()

    for i, valor in enumerate(observados):
        labels.append(f"x{i}")

    labels.append("valor_real")

    for elemento in lista_valores:
        
        auxiliar:list[int] = []

        for observado in observados:
            
            if elemento >= observado:
                auxiliar.append(1)
            else:
                auxiliar.append(0)

        auxiliar.append(elemento)
        
        binarizacion.append(auxiliar)

    
    dataframe = pd.DataFrame(data=binarizacion, columns=labels)

    return dataframe

if __name__ == "__main__":

    prueba:list = [0.25, 0.75, 1.00, 0.50, 0.75, 1.25, 1.75, 0.25, 1.00, 1.50, 0.50, 1.25, 1.50, 2.25, 1.75, 1.25, 2.25, 2.75, 1.25, 1.75, 2.25]

    data = binarizado_no_categoricos(prueba)

    print(data)