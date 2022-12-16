import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

from librerias import Datasets

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


def main(): 

    #obtenemos los datasets con el conjunto de validacion y el de prueba de cada uno de los dataset
    datasetIris = Datasets.generate_train_test("./src/iris.csv", 'species', 3)


    #para el dataset de los emails, tendremos que trabajarlo manualmente su formato como dataset, debido a que hay que remover columnas del dataset, antes de obtener los pliegues

    dataFrameEmails = pd.read_csv("./src/emails.csv", sep=',', engine='python')
    sinTarget = dataFrameEmails.drop('Prediction',axis=1)
    X = sinTarget.drop('Email No.',axis=1).values
    y = dataFrameEmails['Prediction'].values 		

    datasetEmails = Datasets.crearConjuntosDeValidacion(3, X, y)


    print("dataset Emails conjunto de validacion:\n\n", datasetEmails.validation_set[0].X_train)

    #probemos ahora que pasa al mandar los datasets a sus respectivos metodos
    #emails(datasetIris)

    emails(datasetEmails)
    return 0

def emails(dataset):

    exactitudPromedio = 0
    exactitudPromedioSinNormalizar = 0
    clf = GaussianNB()

    for pliegue in dataset.validation_set:

        clf.fit(pliegue.X_train, pliegue.y_train)

        y_predict = clf.predict(pliegue.X_train)
        print ('------------Gaussian NB------------')
        print (y_predict)
        print (clf.predict_proba(pliegue.X_train))
        # ~ print (clf.predict_log_proba(X))

        print (accuracy_score(pliegue.y_train, y_predict))
        print (accuracy_score(pliegue.y_train, y_predict, normalize=False))

        #guardamos la presición obtenida en la variable del promedio
        exactitudPromedio += accuracy_score(pliegue.y_train, y_predict)
        exactitudPromedioSinNormalizar += accuracy_score(pliegue.y_train, y_predict, normalize=False)

        target_names =clf.classes_
        print (target_names)

        print(classification_report(pliegue.y_train, y_predict, target_names=target_names))
        print (confusion_matrix(pliegue.y_train, y_predict, labels=target_names))

    #dividimos la exactitud promedio entre el total de pliegues que estamos usando

    exactitudPromedio /= len(dataset.validation_set)

    print("la exactitud promedio es: ", exactitudPromedio)


    #realizamos la prediccion para el conjunto de prueba
    y_predict_test = clf.predict(dataset.test_set.X_test)

    print("la presicion obtenida en el conjunto de prueba para el gaussiano es: ", accuracy_score(dataset.test_set.y_test, y_predict_test))


    #hacemos lo mismo pero con la distribución multinomial

    print ('\n------------Multinomial NB------------')
    
    exactitudPromedio = 0
    exactitudPromedioSinNormalizar = 0
    clf = MultinomialNB()

    for pliegue in dataset.validation_set:
        
        clf.fit(pliegue.X_train, pliegue.y_train)

        y_predict = clf.predict(pliegue.X_train)
        print (accuracy_score(pliegue.y_train, y_predict))
        print (accuracy_score(pliegue.y_train, y_predict, normalize=False))

        #guardamos la presición obtenida en la variable del promedio
        exactitudPromedio += accuracy_score(pliegue.y_train, y_predict)
        exactitudPromedioSinNormalizar += accuracy_score(pliegue.y_train, y_predict, normalize=False)

        print(classification_report(pliegue.y_train, y_predict, target_names=target_names))
        cm = confusion_matrix(pliegue.y_train, y_predict, labels=target_names)
        print (cm)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
        disp.plot()
        plt.show()

    exactitudPromedio /= len(dataset.validation_set)

    print("la exactitud promedio es: ", exactitudPromedio)
        

     #realizamos la prediccion para el conjunto de prueba
    y_predict_test = clf.predict(dataset.test_set.X_test)

    print("la presicion obtenida en el conjunto de prueba para el gaussiano es: ", accuracy_score(dataset.test_set.y_test, y_predict_test))

def iris(dataset):

    exactitudPromedio = 0
    exactitudPromedioSinNormalizar = 0

    for pliegue in dataset.validation_set:

        clf = GaussianNB()
        clf.fit(pliegue.X_train, pliegue.y_train)

        y_predict = clf.predict(pliegue.X_train)
        print ('------------Gaussian NB------------')
        print (y_predict)
        print (clf.predict_proba(pliegue.X_train))
        # ~ print (clf.predict_log_proba(X))

        print (accuracy_score(pliegue.y_train, y_predict))
        print (accuracy_score(pliegue.y_train, y_predict, normalize=False))

        exactitudPromedio += accuracy_score(pliegue.y_train, y_predict)
        exactitudPromedioSinNormalizar += accuracy_score(pliegue.y_train, y_predict, normalize=False)

        target_names =clf.classes_
        print (target_names)

        print(classification_report(pliegue.y_train, y_predict, target_names=target_names))
        print (confusion_matrix(pliegue.y_train, y_predict, labels=target_names))


    exactitudPromedio /= len(dataset.validation_set)

    print("la exactitud promedio es: ", exactitudPromedio)

    # ~ print ('\n------------Multinomial NB------------')
    # ~ clf = MultinomialNB()
    # ~ clf.fit(X, y)

    # ~ y_predict = clf.predict(X)
    # ~ print (accuracy_score(y, y_predict))
    # ~ print (accuracy_score(y, y_predict, normalize=False))

    # ~ print(classification_report(y, y_predict, target_names=target_names))
    # ~ cm = confusion_matrix(y, y_predict, labels=target_names)
    # ~ print (cm)
    # ~ disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
    # ~ disp.plot()
    # ~ plt.show()


if __name__ ==  "__main__":
    main()