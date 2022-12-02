import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import operator
import pandas as pd
from  sklearn import preprocessing
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split, KFold
from librerias import manejo_dataset_weatherAUS as manejoDT

#vamos a traernos las clases para los conjuntos de validacion y de prueba

class validation_set:
	def __init__(self, X_train, y_train, X_test, y_test):
		self.X_train = X_train
		self.y_train = y_train
		self.X_test = X_test
		self.y_test = y_test

class test_set:
	def __init__(self, X_test, y_test):
		self.X_test = X_test
		self.y_test = y_test

class data_set:
	def __init__(self, validation_set, test_set):
		self.validation_set = validation_set
		self.test_set = test_set


mse_list = []
r2_list = []

'''#Generación de los datos
np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)  #genera 20 aleatorios de la distribución normal (Gausiana) con media =-3 y desviación estandar=3 para que los datos no queden muy desbalanceados
print ('x{}\ny{}'.format(x,y))
plt.scatter(x,y, s=10)

#Se agrega una nueva dimensión para que variable sea un arreglo
## ~ x = np.reshape(x, (-1,1))
x = x[:, np.newaxis]
print ('x{}\ny{}'.format(x,y))'''

#carguemos los datos del dataeet en lugar de generarlos de forma aleatoria

archivo = open("./cal_housing.csv", "r", encoding="utf8")
dataset = archivo.readlines()
archivo.close()

x = []
y= []
longitud = []
latitud = []
housingMedianAge = []
CuartosTotales = []
camasTotales = []
poblacion = []
houseHolds = []
gananciaMedia = []

arregloDatos = []

head = dataset.pop(0)

for element in dataset:
    arregloDatos = element.split(",")

    for i in range(len(arregloDatos)):
        arregloDatos[i] = float(arregloDatos[i])
    
    y.append(arregloDatos.pop()) #<- quitamos del arreglo al dato target, para ahora sí, conectarle a x todos los datos de x
    x.append(arregloDatos)






#print("dato 1 de y: ", y[0])

#creamos AX para plotear dimension por dimension
    #fig = plt.figure()

    '''ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title("vs longitud")
    ax1.set(xlabel="longitud", ylabel="costo promedio de la casa")'''

    '''ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title("vs latitud")
    ax2.set(xlabel="latitud", ylabel="costo promedio de la casa")
    
    ax3 = fig.add_subplot(2,1,1)
    ax3.set_title("vs antiguedad romedio")
    ax3.set(xlabel="antiguedad romedio", ylabel="costo promedio de la casa")

    ax4 = fig.add_subplot(2,2,2)
    ax4.set_title("vs habitaciones")
    ax4.set(xlabel="habitaciones", ylabel="costo promedio de la casa")'''

    '''ax5 = fig.add_subplot(2,4,1)
    ax5.set_title("vs camas")
    ax5.set(xlabel="camas", ylabel="costo promedio de la casa")

    ax6 = fig.add_subplot(2,4,2)
    ax6.set_title("vs poblacion")
    ax6.set(xlabel="poblacion", ylabel="costo promedio de la casa")

    ax7 = fig.add_subplot(2,4,3)
    ax7.set_title("vs househods")
    ax7.set(xlabel="households", ylabel="costo promedio de la casa")

    ax8 = fig.add_subplot(2,4,4)
    ax8.set_title("vs ganancia promedio")
    ax8.set(xlabel="ganancia promedio", ylabel="costo promedio de la casa")'''

#Aqui crearemos los conjuntos de entrenamiento y de prueba

#X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=.2, random_state=0, shuffle=True)

#creamos el conjunto de validacion a partir del conjunto de entrenamiento

#print("x_train:\n", X_train)
'''print("y_train:\n",Y_train)
print("x_test:\n",X_test)
print("y_test:\n",Y_test)'''

'''validation_sets = []
kf = KFold(n_splits=10)
c=0

for train_index, test_index in kf.split(X_train):
		c=c+1
		X_train_v, X_test_v = X_train[train_index], X_train[test_index]
		y_train_v, y_test_v = Y_train[train_index], Y_train[test_index]
		#Agrega el pliegue creado a la lista
		validation_sets.append(validation_set(X_train_v, y_train_v, X_test_v, y_test_v))
		print('\n PLIEGUE', c, '\n')
		print('X_train_v', *X_train_v,  '\ny_train_v', *y_train_v,'\n')
		print('X_test_v',  *X_test_v,  '\ny_test_v', *y_test_v)


my_test_set = test_set(X_test, Y_test)

my_data_set = data_set(validation_sets, my_test_set) '''

my_data_set = manejoDT.generate_train_test("./cal_housing.csv", 10)

#print("print de mi dataset de validacion",my_data_set.validation_set[1].X_train)

#guardamos cada una de las diemnsiones del arreglo de x

for dimensiones in my_data_set.test_set.X_test:
    longitud.append(dimensiones[0])
    latitud.append(dimensiones[1])
    housingMedianAge.append(dimensiones[2])
    CuartosTotales.append(dimensiones[3])
    camasTotales.append(dimensiones[4])
    poblacion.append(dimensiones[5])
    houseHolds.append(dimensiones[6])
    gananciaMedia.append(dimensiones[7])

#Guarda el dataset en formato csv
np.savetxt("data_test.csv", my_data_set.test_set.X_test, delimiter=",", fmt="%s",
        header="x")

np.savetxt("target_test.csv", my_data_set.test_set.y_test, delimiter=",", fmt="%s",
        header="y", comments="")


#print("Esto hay en my_data_set:\n", my_data_set)

#realizamos los plots con el conjunto de entrenamiento

plt.scatter(latitud,my_data_set.test_set.y_test)
plt.show()

plt.scatter(housingMedianAge,my_data_set.test_set.y_test)
plt.show()

plt.scatter(CuartosTotales,my_data_set.test_set.y_test)
plt.show()

plt.scatter(camasTotales,my_data_set.test_set.y_test)
plt.show()

plt.scatter(poblacion,my_data_set.test_set.y_test)
plt.show()

plt.scatter(houseHolds,my_data_set.test_set.y_test)
plt.show()

plt.scatter(gananciaMedia,my_data_set.test_set.y_test)
plt.show()

#plt.plot(longitud, y_pred, color='r')

#operaciones con los datos sin escalar del conjunto de validacion:



# ~ ###########     EXPERIMENT 4
#encerraremos este proceso en bucle para obtener todos los conjuntos de validacion de los k pliegues
contador = 0

for val_set in my_data_set.validation_set:

    polynomial_features= PolynomialFeatures(degree=1)
    x_poly = polynomial_features.fit_transform(val_set.X_train)
    x_poly_robust_scaler = preprocessing.StandardScaler().fit_transform(x_poly)
    regr = SGDRegressor(learning_rate = 'constant', eta0 = 0.001, max_iter= 10000)
    regr.fit(x_poly_robust_scaler, val_set.y_train)
    y_poly_pred = regr.predict(x_poly_robust_scaler)
    mse = mean_squared_error(val_set.y_train, y_poly_pred)
    r2 = r2_score(val_set.y_train, y_poly_pred)

    mse_list.append(mse)
    r2_list.append(r2)

    print("pliegue: ", contador)
    contador+=1


# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
#print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
#print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')
print ('Regresión polinomial estocástico grado 1 escalado estandar\nmse: {} r2: {}'.format(mse, r2))

for val_set in my_data_set.validation_set:

    polynomial_features= PolynomialFeatures(degree=2)
    x_poly = polynomial_features.fit_transform(val_set.X_train)
    x_poly_robust_scaler = preprocessing.StandardScaler().fit_transform(x_poly)
    regr = SGDRegressor(learning_rate = 'constant', eta0 = 0.001, max_iter= 10000)
    regr.fit(x_poly_robust_scaler, val_set.y_train)
    y_poly_pred = regr.predict(x_poly_robust_scaler)
    mse = mean_squared_error(val_set.y_train, y_poly_pred)
    r2 = r2_score(val_set.y_train, y_poly_pred)

    mse_list.append(mse)
    r2_list.append(r2)

    print("pliegue: ", contador)
    contador+=1


# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
#print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
#print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')
print ('Regresión polinomial estocástico grado 2 escalado estandar\nmse: {} r2: {}'.format(mse, r2))

for val_set in my_data_set.validation_set:

    polynomial_features= PolynomialFeatures(degree=3)
    x_poly = polynomial_features.fit_transform(val_set.X_train)
    x_poly_robust_scaler = preprocessing.StandardScaler().fit_transform(x_poly)
    regr = SGDRegressor(learning_rate = 'constant', eta0 = 0.001, max_iter= 10000)
    regr.fit(x_poly_robust_scaler, val_set.y_train)
    y_poly_pred = regr.predict(x_poly_robust_scaler)
    mse = mean_squared_error(val_set.y_train, y_poly_pred)
    r2 = r2_score(val_set.y_train, y_poly_pred)

    mse_list.append(mse)
    r2_list.append(r2)

    print("pliegue: ", contador)
    contador+=1


# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
#print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
#print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')
print ('Regresión polinomial estocástico grado 3 escalado estandar\nmse: {} r2: {}'.format(mse, r2))

'''###########     EXPERIMENT 1

#Modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

plt.figure().add_subplot(1, 2, 1).scatter(longitud,y)
#plt.scatter(longitud,y)
#ax2.scatter(latitud,y)
#ax3.scatter(housingMedianAge,y)
#ax4.scatter(CuartosTotales,y)
#ax5.scatter(camasTotales,y)
#ax6.scatter(poblacion,y)
#ax7.scatter(houseHolds,y)
#ax8.scatter(gananciaMedia,y)
#plt.plot(longitud, y_pred, color='r')

#plt.show()

print(pd.DataFrame({'x': longitud, 'Predicted': y_pred}))

#Cálculo del error cuadrado medio y r2
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print ('\n Regresión lineal\nmse: {} r2: {}'.format(mse, r2), '\n')
mse_list.append(mse)
r2_list.append(r2)


###########     EXPERIMENT 2

#Conversión de las variables de la ecuación original a polinomio de grado 2
polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)
print ('\n x_poly', x_poly)

# ~ #Modelo de regresión polinomial
model_poly = LinearRegression()
model_poly.fit(x_poly, y)
y_poly_pred = model_poly.predict(x_poly)
print('y_poly_pred {}'.format(y_poly_pred))

# ~ #Cálculo del error cuadrado medio y r2
mse = mean_squared_error(y, y_poly_pred)
r2 = r2_score(y, y_poly_pred)
mse_list.append(mse)
r2_list.append(r2)

#plt.plot(x, y_poly_pred, color='g')
print(pd.DataFrame({'x': x, 'Predicted': y_poly_pred}))
print ('\nRegresión polinomial grado 2\nmse: {} r2: {}'.format(mse, r2),'\n')



#Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='g')
print ('\nRegresión polinomial grado 2\nmse: {} r2: {}'.format(mse, r2),'\n')

# ~ ###########     EXPERIMENT 3

# ~ # Modelo de regresión polinomial grado 3
polynomial_features= PolynomialFeatures(degree=3)
x_poly = polynomial_features.fit_transform(x)
model_poly = LinearRegression()
model_poly.fit(x_poly, y)
y_poly_pred = model_poly.predict(x_poly)



mse = mean_squared_error(y, y_poly_pred)
r2 = r2_score(y, y_poly_pred)
mse_list.append(mse)
r2_list.append(r2)

# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')

print ('\nRegresión polinomial grado 3\nmse: {} r2: {}'.format(mse, r2), '\n')

# ~ ###########     EXPERIMENT 3.1

# ~ ####Escalado de los datos####
# ~ #Standard Scaler
x_poly_standard_scaler = preprocessing.StandardScaler().fit_transform(x_poly)
print (x_poly_standard_scaler)
model_poly.fit(x_poly_standard_scaler, y)
y_poly_pred = model_poly.predict(x_poly_standard_scaler)


mse = mean_squared_error(y, y_poly_pred)
r2 = r2_score(y, y_poly_pred)
mse_list.append(mse)
r2_list.append(r2)


# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')
print ('\nRegresión polinomial grado 3 escalado estándar\nmse: {} r2: {}'.format(mse, r2),'\n')

# ~ ###########     EXPERIMENT 3.2

x_poly_robust_scaler = preprocessing.RobustScaler().fit_transform(x_poly)
model_poly.fit(x_poly_robust_scaler, y)
y_poly_pred = model_poly.predict(x_poly_robust_scaler)
mse = mean_squared_error(y, y_poly_pred)
r2 = r2_score(y, y_poly_pred)
print ('Regresión polinomial grado 3 escalado robusto\nmse: {} r2: {}'.format(mse, r2))
mse_list.append(mse)
r2_list.append(r2)


# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')
print ('\nRegresión polinomial grado 3 escalado robusto\nmse: {} r2: {}'.format(mse, r2),'\n')



# ~ ###########     EXPERIMENT 4
polynomial_features= PolynomialFeatures(degree=3)
x_poly = polynomial_features.fit_transform(x)
x_poly_robust_scaler = preprocessing.RobustScaler().fit_transform(x_poly)
regr = SGDRegressor(learning_rate = 'constant', eta0 = 0.001, max_iter= 10000)
regr.fit(x_poly_robust_scaler, y)
y_poly_pred = regr.predict(x_poly_robust_scaler)
mse = mean_squared_error(y, y_poly_pred)
r2 = r2_score(y, y_poly_pred)

mse_list.append(mse)
r2_list.append(r2)


# ~ #Ajustes para que la curva trazada se vea correctamente
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
print (tuple(sorted_zip))
x_sorted, y_poly_pred = zip(*sorted_zip)
print(pd.DataFrame({'x': x_sorted, 'Predicted': y_poly_pred}))
#plt.plot(x_sorted, y_poly_pred, color='b')
print ('Regresión polinomial estocástico grado 3 escalado robusto\nmse: {} r2: {}'.format(mse, r2))


# initialize data of lists.
data = {'mse':mse_list,
        'r2':r2_list}
 
# Creates pandas DataFrame.
df = pd.DataFrame(data, index =['Regresión lineal',
                                'Regresión polinomial grado 2',
                                'Regresión polinomial grado 3',
                                'Regresión polinomial grado 3 escalado estándar',
                                'Regresión polinomial grado 3 escalado robusto',
                                'Regresión polinomial estocástico grado 3 escalado robusto'])

print(df,'\n')

'''