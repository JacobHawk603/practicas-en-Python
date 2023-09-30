from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd


def entropia(clases):
    '''Clases -> np.ndarray que contiene los elementos por clase con los que se va a calcular la entropia'''
    i = 0   #<- Entropia, no un contador de for
    m = 0

    #calculamos el total de los elementos de cada clase
    for clase in clases:
        m+=clase

    #calculamos la entropía
    for clase in clases:
        # print("m del error: ", m)
        if clase != 0:
            i+=(-(clase/m) * np.log2(clase/m))  #<- Importante, debe de ser logaritmo de base 2 para que de el resultado visto en clase

    return i

def entropia_de_Atributo(ramas):
    '''ramas -> np.ndarray que contiene los elementos por cada decicion posible del algoritmo con los que se va a calcular la entropia'''
    i = 0
    m = 0

    for rama in ramas:
        m +=rama[0] + rama[1]

    for rama in ramas:
        print(rama)
        i += ((rama[0] + rama[1])/m) * entropia(rama)

    return i

def ganancia(entropia_general, entropia_atributo):
    return entropia_general - entropia_atributo

def ejemplo_quinlan():
    #primero realicemos una prueba de id3 con el ejemplo de quinlan para ver si vamos por buen camino

    df = pd.read_excel("./ejemplo_quinlan.ods")
    print(df)

    #separamos el corpus en X y target (y)

    X = df.drop('Decision', axis=1)
    y = df['Decision']

    print(X)
    print("\n\n", y)

    #obteniendo la entropia de la muestra
    y_pos = 0
    y_neg = 0

    print(y.values)

    for element in y.values:
        if(element == 'Yes'):
            y_pos += 1
        else:
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

if __name__ == "__main__":

    # Vamos a comenzar por importar el dataset directamente desde python
  
    # # fetch dataset 
    # credit_approval = fetch_ucirepo(id=27) 
    
    # # data (as pandas dataframes) 
    # X = credit_approval.data.features 
    # y = credit_approval.data.targets 
    
    # # metadata 
    # print(credit_approval.metadata) 
    
    # # variable information 
    # print(credit_approval.variables) 

    ejemplo_quinlan()