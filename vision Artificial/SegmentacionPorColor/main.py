import pandas as pd
import numpy as np
import cv2
import kmeans

def main():
    
    #intentemos crear un dataframe de 3 dimensiones, ya que lo vamos a requerir para las capas RGB de la imagen
    datos = {'columna1':[1,2,3], 'columna2':[4,5,6], 'columna3': [7,8,9]}
    df = pd.DataFrame(data=datos)
    print(df)

    #cargamos la imagen
    imagen = cv2.imread("../src/paisaje_resized.jpg")

    r = imagen[:,:,2]
    g = imagen[:,:,1]
    b = imagen[:,:,0]

    #guardamos todos los pixeles en un arreglo unidimencional POR CAPA!!!
    r_uni = []
    g_uni = []
    b_uni = []
    filas = []
    columnas =[]
    #print(r.shape[0])
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            r_uni.append(r[i,j])
            g_uni.append(g[i,j])
            b_uni.append(b[i,j])
            filas.append(i)
            columnas.append(j)
    
    #print(coordenadas[0][:])

    #ahora si vamos a hacer el dataframe
    datos = {'R':r_uni, 'G':g_uni, 'B':b_uni, 'rows':filas, 'columns':columnas}
    df = pd.DataFrame(data=datos)
    print(df)

    #imagenBN = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #<- probablemente no se vaya a ocupar
    #print(imagenBN[:3,:3])
    #cv2.imshow("capa r", r)
    #cv2.waitKey(0)
    #guardamos la imagen en formato csv
    #np.savetxt("./imagen.csv", r, delimiter=',')
    #np.savetxt("./imagen.csv", g, delimiter=',')
    #np.savetxt("./imagen.csv", b, delimiter=',')

    #ahora obtenemos el dataset a partir de la lectura del archivo csv

    #df = pd.read_csv("./imagen.csv", sep=',', engine='python')

    #Le tiramos todo el dataFrame al KNN para que clusterize XD
    dfClusters = kmeans.knn(df, 5)
    print(dfClusters)
    np.savetxt("./imagenClusterizada.csv", df, delimiter=',')
    #np.savetxt("./dfClusters.csv", dfClusters, delimiter=',')

    #recuperamos los clusters
    clusters = df['centroid'].values

    print (clusters)

    return 0

if __name__ == "__main__":
    main()