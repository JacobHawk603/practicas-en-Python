import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def main():

    #cargamos el dataset
    dataframe = pd.read_csv("./src/heart.csv", delimiter=',', engine="python")

    print(dataframe)

    #separamos el corpus y el target
    corpus = dataframe.drop('target', axis=1).values
    target = dataframe['target'].values

    #mezclamos los datos y creamos el conjunto de datos
    X_train, X_test, y_train, y_test = train_test_split(corpus, target, train_size=0.7, shuffle=True, random_state=0)

    #con sklearn.svc--------------------------------------------------------------------------------------------

    #con svm vamos a clasificar
    clf = svm.SVC()
    clf.fit(X_train, y_train)

    #ahora vamos a obtener la prediccion

    print("y_test: \n", y_test)

    print("prediccion con scikit-learn: ", clf.predict(X_test))

    #-----------------------------------------------------------------------------------------------------------

    #de una manera mas manual

    print(X_train)

    centroides = [[],[]] #<- [c-, c+]

    for i in range(len(X_train[0])):
        dimensionCmenos = 0
        dimensionCmas = 0

        for j in range(len(X_train)):
            
            if(y_train[j] == 0):
                #logica para el c-
                dimensionCmenos += X_train[j][i]
            else:
                #logica para c+
                dimensionCmas += X_train[j][i]
        
        centroides[0].append(dimensionCmenos/(len(X_train)/2))
        centroides[1].append(dimensionCmas/(len(X_train)/2))

    #obtuvimos los vectores c+ y c-

    print(centroides)

    #obteniendo c
    media1 = 0
    media2 = 0

    c = []
    for i in range(len(centroides[0])):

        c.append(centroides[0][i] + centroides[1][i])

    cMedios = []
    cNorma2 = 0

    for dimension in c:
        cMedios.append(dimension/2)

    for dimension in cMedios:
        cNorma2 += dimension**2

    
    print("vector c:\n\n", c)

    #obtuvimos c!!!

    #realizamos las proyecciones para realizar las predicciones

    predicciones = []

    for vector in X_test:
        #print(vector)

        if((np.dot(vector, cMedios)/np.sqrt(cNorma2)) < np.sqrt(cNorma2)):
            predicciones.append(0)
        else:
            predicciones.append(1)
            #print(np.dot(vector, cMedios)/np.sqrt(cNorma2))
    
    #print("norma: ", np.sqrt(cNorma2))

    print("predicciones manuales: \n\n", predicciones)


    #realizamos la matriz de confusion
    target_names = [0, 1]

    cm = confusion_matrix(y_test, predicciones, labels=target_names)
    print (cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
    disp.plot()
    plt.show()

    return 0





if __name__ == "__main__":
    main()