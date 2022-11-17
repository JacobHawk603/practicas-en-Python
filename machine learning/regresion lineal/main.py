import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import train_test_split


def F(w, X, y):
	return sum((w * x - y)**2 for x, y in zip(X, y))/len(y)


def dF(w, X, y):
	return sum(2*(w * x - y) * x for x, y in zip(X, y))/len(y)


def print_line(points, w, iteration, line_color = None, line_style = 'dotted'):
	list_x = []
	list_y = []
	for index, tuple in enumerate(points):
		x = tuple[0]
		y = x * w
		list_x.append(x)
		list_y.append(y)
	ax1.text(x,y, iteration, horizontalalignment='right')
	ax1.plot(list_x, list_y, color = line_color, linestyle= line_style)

if __name__=='__main__':

    #cargamos el dataset

    archivo = open("./dataset_ejercicio_I_regresion_lineal.csv", "r", encoding="utf8")
    dataset = archivo.readlines()
    archivo.close()

    arrAux = []
    X = []
    y = []

    header = dataset.pop(0)

    
    #random.shuffle(dataset)  

    for element in dataset:
        arrAux.append(element.replace("\n", "").split(","))

    for i in range(len(arrAux)):
        X.append(int(arrAux[i][0]))
        y.append(float(arrAux[i][1]))

    #generamos los conjuntos de entrenamiento y prueba

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=.1, random_state=0, shuffle=True)


    #print(X)
    #print(y)

    #X = [1, 2, 3, 4, 5, 6]
    #y = [1, 2.5, 2, 4, 4.5, 6.3]

    #reemplazamos los elementos x y Y para aplicar el metodo en nuestro dataset

    list_error = []
    list_w = []	
    iterations = int(sys.argv[1])

    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title("Linear regression")
    ax1.set(xlabel="size", ylabel="price")
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title("Loss function")
    ax2.set(xlabel="weight", ylabel="error")

    ax1.scatter(X_train, Y_train)

    w= 0
    alpha = 0.000001
    # ~ alpha = 0.05 #Efecto similar al de no sacar el promedio
    #aplicamos el proceso a los conjuntos de entrenamiento
    for t in range(iterations):
        error = F(w, X_train, Y_train)
        gradient = dF(w, X_train, Y_train)
        print ('gradient = {}'.format(gradient))
        ax2.scatter(w, error)
        ax2.text(w, error, t, horizontalalignment='right')
        list_w.append(w)
        list_error.append(error)
        
        w = w - alpha * gradient
        print ('iteration {}: w = {}, F(w) = {}'.format(t, w, error))
        print_line(zip(X_train, Y_train), w, t)
            
    print_line(zip(X_train, Y_train), w, t, 'red', 'solid')
    ax2.plot(list_w, list_error, color = 'red', linestyle = 'solid')

    plt.show()
