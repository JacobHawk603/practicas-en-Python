from encodings import utf_8
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np
import sys
import pickle
import random

class Validation_set:
	def __init__(self, X_train:list | np.ndarray, y_train:list | np.ndarray, X_test:list | np.ndarray, y_test:list | np.ndarray):
		self.X_train = X_train
		self.y_train = y_train
		self.X_test = X_test
		self.y_test = y_test

class Test_set:
	def __init__(self, X_test, y_test):
		self.X_test = X_test
		self.y_test = y_test

class Data_set:
	def __init__(self, validation_set: Validation_set | list[Validation_set], test_set: Test_set):
		self.validation_set = validation_set
		self.test_set = test_set

def generate_train_test(target_label:str, file_path:str=None, dataframe:pd.DataFrame=None, kfolds:int = None, test_size=0.4, shuffle = True):
	# ~ pd.options.display.max_colwidth = 200		#Define el acho de las columnas (ancho máximo por default 50 caracteres)		
	#Lee el corpus original del archivo de entrada y lo pasa a un DataFrame
	if(file_path != None):
		df = pd.read_csv(file_path, sep=',', engine='python')
	else:
		df = dataframe

	X = df.drop(target_label,axis=1).values    						#corpus sin etiquetas 
	y = df[target_label].values 									#etiquetas

	#definims una variable para controlar los pliegues
	#pliegues = input("validacion cruzada con cuantos pliegues")
	#tamanoTest = 1/pliegues

	#Separa corpus en conjunto de entrenamiento y prueba

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle = shuffle)	
	
	print('\n Dataset\n', df)
	print('\n Corpus')
	print('\n', *X)
	print ('----------------------')
	print('\n Etiquetas')
	print('\n', *y)
	print ('----------------------')
	print('\n Conjunto de prueba')
	print('\n X_test\n', *X_test)
	print('\n y_test\n', *y_test)
	print ('----------------------')
	print('\n Conjunto de entrenamiento = Conjunto de Validación')
	print('\n X_train\n', *X_train)
	print('\n y_train\n', *y_train)
	
	if kfolds != None:
		#Crea pliegues para la validación cruzada
		print ('----------------------')
		print('\n VALIDACION CRUZADA k=2\n')
		validation_sets:list[Validation_set] = []
		kf = KFold(n_splits=kfolds)
		c=0
		for train_index, test_index in kf.split(X_train):
			c=c+1
			X_train_v, X_test_v = X_train[train_index], X_train[test_index]
			y_train_v, y_test_v = y_train[train_index], y_train[test_index]
			#Agrega el pliegue creado a la lista
			validation_sets.append(Validation_set(X_train_v, y_train_v, X_test_v, y_test_v))
			# print('\n PLIEGUE', c, '\n')
			# print('X_train_v', *X_train_v,  '\ny_train_v', *y_train_v,'\n')
			# print('X_test_v',  *X_test_v,  '\ny_test_v', *y_test_v)
		
		#Almacena el conjunto de prueba
		my_test_set = Test_set(X_test, y_test)	
		
		#Guarda el dataset con los pliegues del conjunto de validación y el conjunto de pruebas
		my_data_set = Data_set(validation_sets, my_test_set) 
		return (my_data_set)

	else:
		#guardamos los conjuntos de validacion y prueba en la clase my_data_set
		validation_sets = []

		validation_sets.append(Validation_set(X_train, y_train, X_test, y_test))
		my_test_set = Test_set(X_test, y_test)

		my_data_set = Data_set(validation_sets, my_test_set) 
		return (my_data_set)
	
def manejo_datasets(target_label:str, file_path:str = None, dataframe:pd.DataFrame = None, kfolds=3, test_size=0.3, shuffle:bool = False):

	if file_path != None:
		data = pd.read_csv(file_path)
	else:
		data = dataframe

	target = data[target_label]
	labels:str = ""

	for i, label in enumerate(data.drop(target_label, axis=1).columns.to_list()):

		if i < len(data.drop(target_label, axis=1).columns.to_list())-1:
			labels += label + ","
		else:
			labels += label

	my_data_set=generate_train_test(dataframe=data, target_label=target_label, kfolds=kfolds, test_size=test_size, shuffle=shuffle)
	
	#Guarda el dataset en formato csv
	np.savetxt("X_test.csv", my_data_set.test_set.X_test, delimiter=",", fmt="%s",
           header="x")
	
	np.savetxt("y_test.csv", my_data_set.test_set.y_test, delimiter=",", fmt="%s",
           header="y", comments="")
    
	i = 1
	for val_set in my_data_set.validation_set:
		np.savetxt("X_train.csv", val_set.X_train, delimiter=",", fmt="%s",
           header=labels, comments="")
		np.savetxt("X_test.csv", val_set.X_test, delimiter=",", fmt="%s",
           header=labels, comments="")
		
		print("Este es el print que buscas: ", val_set.y_train)
		print("Este es el print secundario: ", val_set.y_test)
		print("Este es el print terciario: ", val_set.X_train)

		# auxiliar = np.array(val_set.y_train)
	
		np.savetxt("y_train.csv", val_set.y_train, delimiter=",",
           header=target_label, comments="")
		np.savetxt("y_test.csv", val_set.y_test, delimiter=",", fmt="%d",
           header=target_label, comments="")
		i = i + 1
	
	#Guarda el dataset en pickle
	dataset_file = open ('dataset.pkl','wb')
	pickle.dump(my_data_set, dataset_file)
	dataset_file.close()
	
	dataset_file = open ('dataset.pkl','rb')
	my_data_set_pickle = pickle.load(dataset_file)
	print ("-----------------------------------------------")
	print (*my_data_set_pickle.test_set.X_test)
