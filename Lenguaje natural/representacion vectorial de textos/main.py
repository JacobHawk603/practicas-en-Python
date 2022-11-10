from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

def vectorizacion():

    dataset = open("./noticias_salida.txt", "r", encoding='utf8')
    corpus = dataset.readlines()
    print(corpus)

    # Representación vectorial binarizada
    # ~ vectorizador_binario = CountVectorizer(binary=True)
    vectorizador_binario = CountVectorizer(binary=True, token_pattern= r'(?u)\w\w+|\w\w+\n|[\.\,\;\:\¿\?\¡\!]')

    X = vectorizador_binario.fit_transform(corpus)

    #https://www.javatpoint.com/convert-pandas-dataframe-to-csv

    df = pd.DataFrame.sparse.from_spmatrix(X, columns=vectorizador_binario.get_feature_names_out())

    binario = open("./binario.txt", 'w', encoding="utf8")
    binario.write(df.to_string())
    binario.close()

    print (vectorizador_binario.get_feature_names_out())
    print (X)#sparse matrix
    print (type(X))#sparse matrix
    # ~ print (type(X.toarray()))#dense ndarray
    print ('Representación vectorial binarizada')
    #print (X.toarray())#dense ndarray

    #Representación vectorial por frecuencia
    vectorizador_frecuencia = CountVectorizer(binary = False, token_pattern= r'(?u)\w\w+|\w\w+\n|[\.\,\;\:\¿\?\¡\!]')
    X = vectorizador_frecuencia.fit_transform(corpus)

    df = pd.DataFrame.sparse.from_spmatrix(X, columns=vectorizador_frecuencia.get_feature_names_out())

    '''frecuencia = open("./frecuencia.txt", 'w', encoding="utf8")
    frecuencia.write(df.to_string())
    frecuencia.close()'''
    print('Representación vectorial por frecuencia')
    #print (X.toarray())

    #Representación vectorial tf-idf
    vectorizador_tfidf = TfidfVectorizer(token_pattern= r'(?u)\w\w+|\w\w+\n|[\.\,\;\:\¿\?\¡\!]')
    X = vectorizador_tfidf.fit_transform(corpus)

    df = pd.DataFrame.sparse.from_spmatrix(X, columns=vectorizador_tfidf.get_feature_names_out())

    tfidf = open("./tfidf.txt", 'w', encoding="utf8")
    tfidf.write(df.to_string())
    tfidf.close()
    print ('Representación vectorial tf-idf')
    print (X.toarray())

    #uso_pandas!!!

def main():
    vectorizacion()

if __name__ == "__main__":
    main()