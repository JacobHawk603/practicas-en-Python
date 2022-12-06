import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

np.random.seed(123)

def circulo(num_datos = 100,R = 1, minimo = 0,maximo= 1, center_x = 0 , center_y = 0):
    pi = math.pi
    r = R * np.sqrt(np.random.uniform(minimo, maximo, size = num_datos)) 
    theta = np.random.uniform(minimo, maximo, size= num_datos) * 2 * pi

    x = center_x + np.cos(theta) * r
    y = center_y + np.sin(theta) * r

    x = np.round(x,3)
    y = np.round(y,3)

    df = np.column_stack([x,y])
    df = pd.DataFrame(df)
    df.columns = ['x','y']

    return(df)

def initialize_centroids(k, data):

    n_dims = data.shape[1]
    centroid_min = data.min().min()
    centroid_max = data.max().max()
    centroids = []

    for centroid in range(k):
        centroid = np.random.uniform(centroid_min, centroid_max, n_dims)
        centroids.append(centroid)

    centroids = pd.DataFrame(centroids, columns = data.columns)

    return centroids

def calculate_error(a,b):
    '''
    Given two Numpy Arrays, calculates the root of the sum of squared errores.
    '''
    error = np.square(np.sum((a-b)**2))

    return error    

def main():

    # Create data
    datos_1 = circulo(num_datos = 20,R = 10, center_x = 5, center_y = 30)
    datos_2 = circulo(num_datos = 20,R = 10, center_x = 20, center_y = 10)
    datos_3 = circulo(num_datos = 20,R = 10, center_x = 50, center_y = 50)

    data = datos_1.append(datos_2).append(datos_3)
    data.head()

    print (datos_1)

    plt.scatter(datos_1['x'], datos_1['y'], c = 'b')
    plt.scatter(datos_2['x'], datos_2['y'], c = 'r')
    plt.scatter(datos_3['x'], datos_3['y'], c = 'g')
    plt.show()

    #inicializamos los k centroides de forma aleatoria
    centroids = initialize_centroids(3, data)

    errors = np.array([])
    for centroid in range(centroids.shape[0]):
        error = calculate_error(centroids.iloc[centroid, :2], data.iloc[0,:2])
        errors = np.append(errors, error)

    print(errors)

    #comprobamos las posiciones de los centroides
    plt.scatter(data.iloc[1:,0], data.iloc[1:,1],  marker = 'o', alpha = 0.2)
    plt.scatter(centroids.iloc[:,0], centroids.iloc[:,1],  marker = 'o', c = 'r')
    plt.scatter(data.iloc[0,0], data.iloc[0,1],  marker = 'o', c = 'g')
    for i in range(centroids.shape[0]):
        plt.text(centroids.iloc[i,0]+1, centroids.iloc[i,1]+1, s = centroids.index[i], c = 'r')

    plt.show()
    # calculamos la suma  de desviaciones al cuadrado

    #Asignamos un centroide a cada una de las observaciones

    #Calculamos el error total y comparamos con la suma en la anterior iteracion.

    #si disminuye el error, recalculamos los centroides y repetimos el proceso
    
if __name__ == "__main__":
    main()