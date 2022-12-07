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


def assign_centroid(data, centroids):
    '''
    Receives a dataframe of data and centroids and returns a list assigning each observation a centroid.
    data: a dataframe with all data that will be used.
    centroids: a dataframe with the centroids. For assignment the index will be used.
    '''

    n_observations = data.shape[0]
    centroid_assign = []
    centroid_errors = []
    k = centroids.shape[0]


    for observation in range(n_observations):

        # Calculate the errror
        errors = np.array([])
        for centroid in range(k):
            error = calculate_error(centroids.iloc[centroid, :2], data.iloc[observation,:2])
            errors = np.append(errors, error)

        # Calculate closest centroid & error 
        closest_centroid =  np.where(errors == np.amin(errors))[0].tolist()[0]
        centroid_error = np.amin(errors)

        # Assign values to lists
        centroid_assign.append(closest_centroid)
        centroid_errors.append(centroid_error)

    return (centroid_assign,centroid_errors)

def knn(data, k):
    '''
    Given a dataset and number of clusters, it clusterizes the data. 
    data: a DataFrame with all information necessary
    k: number of clusters to create
    '''

    # Initialize centroids and error
    centroids = initialize_centroids(k, data)
    error = []
    compr = True
    i = 0

    while(compr):
        # Obtain centroids and error
        data['centroid'], iter_error = assign_centroid(data,centroids)
        error.append(sum(iter_error))
        # Recalculate centroids
        centroids = data.groupby('centroid').agg('mean').reset_index(drop = True)

        # Check if the error has decreased
        if(len(error)<2):
            compr = True
        else:
            if(round(error[i],3) !=  round(error[i-1],3)):
                compr = True
            else:
                compr = False
        i = i + 1 

    data['centroid'], iter_error = assign_centroid(data,centroids)
    centroids = data.groupby('centroid').agg('mean').reset_index(drop = True)

    colors = {0:'red', 1:'blue', 2:'green'}

    figure = plt.figure()
    ax = figure.add_subplot(projection="3d")

    ax.scatter(data.iloc[:,0], data.iloc[:,1], data.iloc[:,2],  marker = 'o', alpha = 0.5) #<- c = data['centroid'].apply(lambda x: colors[x])
    ax.scatter(centroids.iloc[:,0], centroids.iloc[:,1], centroids.iloc[:,2],  marker = 'o', s=300)

    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
    plt.show()

    return (data['centroid'], iter_error, centroids)

def main():

    # Create data
    datos_1 = circulo(num_datos = 20,R = 10, center_x = 5, center_y = 30)
    datos_2 = circulo(num_datos = 20,R = 10, center_x = 20, center_y = 10)
    datos_3 = circulo(num_datos = 20,R = 10, center_x = 50, center_y = 50)

    data = datos_1.append(datos_2).append(datos_3)
    data.head()
    print (data)


    kmeans = knn(data, 3)

    

    '''

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

    #asignamos un centroide a cada una de las observaciones
    data['centroid'], data['error'] = assign_centroid(data.iloc[:,:2] ,centroids)
    data[['centroid', 'error']].head()

    print(data)

    #comprobamos visualmente como ha quedado la asignacion de centroides:
    colors = {0:'red', 1:'blue', 2:'green'}

    plt.scatter(data.iloc[:,0], data.iloc[:,1],  marker = 'o', c = data['centroid'].apply(lambda x: colors[x]), alpha = 0.5)
    plt.scatter(centroids.iloc[:,0], centroids.iloc[:,1],  marker = 'o', s=300, c = centroids.index.map(lambda x: colors[x]))
    plt.show()

    #calculamos la suma de errores
    print(data['error'].sum()) #<- Esto imprime la suma de los errores

    #recalculamos la posicion de los centroides
    data_columns = ['x','y']

    centroids = data.groupby('centroid').agg('mean').loc[:,data_columns].reset_index(drop = True)
    print(centroids) #<- print para ver los centroides

    #volvemos a observar la posicion de los centroides:
    plt.scatter(data.iloc[:,0], data.iloc[:,1],  marker = 'o', c = data['centroid'].apply(lambda x: colors[x]), alpha = 0.5)
    plt.scatter(centroids.iloc[:,0], centroids.iloc[:,1],  marker = 'o', s=300, c = centroids.index.map(lambda x: colors[x]))
    plt.show()

    #si disminuye el error, recalculamos los centroides y repetimos el proceso
    
if __name__ == "__main__":
    main()'''