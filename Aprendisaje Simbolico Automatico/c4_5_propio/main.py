from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import c_4_5


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

    m = c_4_5.entropia([y_pos, y_neg])
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

    entropia_clima = c_4_5.entropia_de_Atributo([clima_S, clima_N, clima_LL])

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

    # X = X.fillna('missing')
    # y = y.fillna('missing')

    # metadata
    print("\n\n dataset: \n\n",credit_approval)

    # variable information
    print(credit_approval.variables)

    print(X, y)
    
    atributos = X.columns

    # pd.DataFrame.to_csv()
    frames = [X, y]

    dataframe = pd.concat(frames, axis=1)
    

    print("\n\n dataframe: \n\n",dataframe)

    pd.DataFrame.to_excel(dataframe, "./src/credit_aproval_dataset.ods")

    exit()

    print(X.columns)
    
    return 0

if __name__ == "__main__":

    credit_aproval()