from arbol import arbol, rama
import pandas as pd
import generacion_hipoteis

def formarArbol(mi_rama:rama, dataFrame:pd.DataFrame):

    print("una iteracion\n\n\n")

     #la siguiente parte del codigo sera un bucle para todos los elementos restantes

    #partimos el dataset

    sub_dataframes = []

    if(not mi_rama.atributos[0].isalpha()): #<- si son categoricos originalmente daràn verdadero a esta condicion

        umbral = float(mi_rama.atributos[0].replace("<= ", ''))
        print("el humbral: {}\t{}".format(umbral, type(umbral)))
        
        # for atributo in mi_rama.atributos:

        # print(dataFrame.filter(like=umbral, axis=0))
        sub_dataframes.append(dataFrame[dataFrame[mi_rama.nodo] <= umbral])
        sub_dataframes.append(dataFrame[dataFrame[mi_rama.nodo] > umbral])

    else:

        for atributo in mi_rama.atributos:
            sub_dataframes.append(dataFrame[dataFrame[mi_rama.nodo] == atributo])

    print("hola?:", sub_dataframes)

    for sub_dataframe in sub_dataframes:
        data = sub_dataframe.drop([mi_rama.nodo], axis=1)
        sub_x = data.drop(['A16'], axis=1)
        sub_y = data['A16']

        mi_rama.subramas.append(generacion_hipoteis.generarRama(sub_x, sub_y))

    for sub_rama, sub_dataframe in zip(mi_rama.subramas, sub_dataframes):
        formarArbol(sub_rama, sub_dataframe)
    

if __name__ == "__main__":
    #importamos el dataframe

    dataFrame = pd.read_excel('./src/credit_aproval_dataset.ods')
    dataFrame = dataFrame.drop(['Unnamed: 0'], axis=1)

    X = dataFrame.drop(['A16'], axis=1)
    y = dataFrame['A16']

    print(dataFrame)
    print("\n\n Corpus: \n\n", X)
    print("\n\n target: \n\n", y)

    #construimos el arbol con base en el dataframe que obtuvimos

    mi_rama = generacion_hipoteis.generarRama(X, y)

    print("la rama que obtuvimos es: \n\n")

    mi_rama.mostrarRama()

    # comenzamos a construir el arbol

    hipotesis = arbol(mi_rama)

    formarArbol(mi_rama, dataFrame)