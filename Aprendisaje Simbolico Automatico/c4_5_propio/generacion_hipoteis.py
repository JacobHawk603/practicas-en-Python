# %%
from arbol import arbol, rama
import numpy as np
import pandas as pd
import copy

# %%
#importamos el dataframe

# dataFrame = pd.read_excel('./src/credit_aproval_dataset.ods')
# dataFrame = dataFrame.drop(['Unnamed: 0'], axis=1)

# X = dataFrame.drop(['A16'], axis=1)
# y = dataFrame['A16']

# # print(dataFrame)
# # print("\n\n Corpus: \n\n", X)
# # print("\n\n target: \n\n", y)

# %%

def generarRama(X, y):
    #identificamos las proporciones del conjunto de datos
    import c_4_5

    total_clases_original = []

    clases = c_4_5.valores_observados(y.values)
    proporcion = []

    for clase in clases:
        total = c_4_5.repeticiones_de_valor(clase, y.values)
        total_clases_original.append([clase, total])

        proporcion.append([clase, total/len(y.values)])

    # print(total_clases_original)
    # print(clases)
    # print(proporcion)



    # %%
    #obtenemos la muestra basandonos en los datos anteriores.

    import preprocesamiento

    x_muestra, y_muestra = preprocesamiento.extraer_muestra(X, y, proporcion, len(y.values), 0.5)

    # print(x_muestra)
    # print(y_muestra)

    # # print(len(x_muestra), len(y_muestra))

    # # print(len(x_muestra)/(len(x_muestra) + len(y_muestra)))

    clases_muestra = c_4_5.valores_observados(y_muestra[0].values)
    total_clases_muestra = []

    for clase in clases_muestra:
        total = c_4_5.repeticiones_de_valor(clase, y_muestra[0].values)
        total_clases_muestra.append([clase, total])

    # print(total_clases_muestra)

    # %%
    #limpiamos el dataset de datos faltantes

    dataframe_muestra = pd.concat([x_muestra, y_muestra], axis=1)

    # print(dataframe_muestra)

    dataframe_limpio = dataframe_muestra.dropna()
    x_muestra_limpio = dataframe_limpio.drop([0], axis=1)
    y_muestra_limpio = dataframe_limpio[0]

    # %%
    #calculamos la entorpia de la muestra ya limpia

    repeticiones_de_clase_muestra = []
    # print(len(y_muestra_limpio.values))

    for clase in clases_muestra:
        total_limpio = c_4_5.repeticiones_de_valor(clase, y_muestra_limpio.values)
        repeticiones_de_clase_muestra.append([clase, total_limpio])

    # print(repeticiones_de_clase_muestra)

    total_repeticiones = []
    for clase in repeticiones_de_clase_muestra:
        total_repeticiones.append(clase[1])

    entropia_muestra = c_4_5.entropia(total_repeticiones)

    # print(entropia_muestra)

    # %%
    #obtengamos los diferentes valores observados por atributo

    valores_observados_por_atributo = []
    valores_observados_por_atributo_copia = []

    for atributo in x_muestra_limpio.columns:

        # # print("\n\n", atributo, ":\n\n")

        valores_observados = c_4_5.valores_observados(x_muestra_limpio[atributo].values)
        auxiliar = []
        for element in valores_observados:
            auxiliar.append([element, c_4_5.repeticiones_de_valor(element, x_muestra_limpio[atributo])])
            # # print([element, c_4_5.repeticiones_de_valor(element, x_muestra_limpio[atributo])])
        
        valores_observados_por_atributo.append([atributo, auxiliar])
        valores_observados_por_atributo_copia.append([atributo, auxiliar])
            
    # print(valores_observados_por_atributo)

    # for atributo in valores_observados_por_atributo:
        # print([atributo[0], len(atributo[1])])
        

    # %%
    #ahora sí podemos comenzar a particionar nuestra muestra, comencemos con las entropias de los atributos con menos diversidad de valores observados

    lengh = 2
    entropias_por_atributo = []

    #hagamos un poco de trampa: analizando el resultado de este bloque de código si valores_observados_atributo > 0, sabemos que cuando dicha lista es <=6 
    # los atributos que restan en la misma, ya no son categoricos, ergo, los atributos restantes, requieren de encontrar el mejor intervalo 
    # para particionar. Así que de momento, dejemos esos atributos pendientes de analisis
    while(lengh <= 14):
        
        # print(len(valores_observados_por_atributo))
        atributo_min = ''

        for atributo in valores_observados_por_atributo:
            if(len(atributo[1]) == lengh):
                atributo_min = valores_observados_por_atributo.pop(valores_observados_por_atributo.index(atributo))
                lengh = len(atributo[1])
                break
        
        if(atributo_min == ''):
            lengh +=1
            continue

        
        # print(atributo_min)

        #obtenemos los positivos y negativos por cada valor observado del atributo

        positivos = []
        negativos = []

        for valor_observado in atributo_min[1]:
            
            total_positivos = 0
            total_negativos = 0

            for row, target in zip(x_muestra_limpio[atributo_min[0]].values, y_muestra_limpio.values):
                
                if(valor_observado[0] == row):
                    if(target == '+'):
                        total_positivos += 1
                    else:
                        total_negativos += 1
            
            positivos.append(total_positivos)
            negativos.append(total_negativos)

        # print(positivos, negativos)

        #calculamos la entropia del atributo con menor diversidad que obtuvimos

        entropia_atributo = c_4_5.entropia_de_Atributo([[positivos[0], negativos[0]], [positivos[1], negativos[1]]],)

        # print(atributo_min[0], entropia_atributo)
        entropias_por_atributo.append([atributo_min[0], entropia_atributo])


    # %%
    #veamos lo que queda en la lista de valores_observados por atributo
    # for valor in valores_observados_por_atributo:
        # print(valor)

    # %%
    #los restantes, los vamos a agrupar en intervalos para calcular su entropia

    # for atributo in valores_observados_por_atributo:

    particiones_de_atributo = []
    repeticiones_de_particiones = []

    for atributo in valores_observados_por_atributo:
        # print("\n\n{}\n\n".format(atributo[0]))

        particion_de_atributo, repeticiones_de_clase_de_particion = c_4_5.intervalo_particion(atributo, x_muestra_limpio[atributo[0]].values, y_muestra_limpio.values)

        # print("La mejor particion para el atributo es: ", particion_de_atributo)
        particiones_de_atributo.append(particion_de_atributo)
        repeticiones_de_particiones.append([atributo[0], repeticiones_de_clase_de_particion])

        



    # %%
    #revisamos que las listas importantes estén bien

    # print(particiones_de_atributo)

    # for particion in particiones_de_atributo:
        # print(particion[0])

    # for repeticion in repeticiones_de_particiones:
        # print(repeticion)



    # %%
    # ahora obtengamos una nueva lista con el atributo y las tuplas etiqueta-repeticiones para ahora así, tener el mismo formato que las variables categoricas y poder calcular la entropia

    valores_observados_por_atributo_no_categorico = []
    etiquetas_valores_no_categoricos = []

    for particion in particiones_de_atributo:
        etiquetas_valores_no_categoricos.append(particion[0])

    # print (etiquetas_valores_no_categoricos) 

    for repeticiones, etiquetas in zip(repeticiones_de_particiones, etiquetas_valores_no_categoricos):
        # print("lo esta haciendo", repeticiones[0])

        if(len(repeticiones[1][0]) < 2):
            # print("rarito")
            if(len(repeticiones[1][1]) < 2):
                valores_observados_por_atributo_no_categorico.append([repeticiones[0], [[etiquetas[0], repeticiones[1][0][0]], [etiquetas[1], repeticiones[1][1][0]]]])
            else:
                valores_observados_por_atributo_no_categorico.append([repeticiones[0], [[etiquetas[0], repeticiones[1][0][0]], [etiquetas[1], repeticiones[1][1][0]+ repeticiones[1][1][1]]]])
        else:
            if(len(repeticiones[1][1]) < 2):
                valores_observados_por_atributo_no_categorico.append([repeticiones[0], [[etiquetas[0], repeticiones[1][0][0] + repeticiones[1][0][1]], [etiquetas[1], repeticiones[1][1][0]]]])
            else:
                valores_observados_por_atributo_no_categorico.append([repeticiones[0], [[etiquetas[0], repeticiones[1][0][0] + repeticiones[1][0][1]], [etiquetas[1], repeticiones[1][1][0]+ repeticiones[1][1][1]]]])
            

    # for valor in valores_observados_por_atributo_no_categorico:

        # print(valor)



    # %%
    #ahora ya podemos calcular las entropias de cada uno de esos atributos no categoricos para comenzar a generar nuestro arbol

    for valor_observado, repeticiones in zip(valores_observados_por_atributo_no_categorico, repeticiones_de_particiones):
        positivos = []
        negativos = []
        # print(repeticiones)

        if(len(repeticiones[1]) < 2):
            total_positivos = repeticiones[1][0]
            total_negativos = 0
        else:
            total_positivos = repeticiones[1][0]
            total_negativos = repeticiones[1][1]

        for row, target in zip(x_muestra_limpio[repeticiones[0]].values, y_muestra_limpio.values):
            
            if(valor_observado[0] == row):
                if(target == '+'):
                    total_positivos += 1
                else:
                    total_negativos += 1
        
        positivos.append(total_positivos)
        negativos.append(total_negativos)

        # print(positivos[0], negativos[0])

        #calculamos la entropia del atributo con menor diversidad que obtuvimos

        #reordenamos los elementos del arreglo
        ramas = []

        for positivo, negativo in zip(positivos, negativos):
            # print("tupla", positivo)
            for i, j in zip(range(len(positivo)), range(len(negativo))):
                ramas.append([positivo[i], negativo[j]])

        # print(ramas)
            
            # ramas.append(tupla)
        
        # print("ramas", ramas)

        entropia_atributo = c_4_5.entropia_de_Atributo(ramas)

        # print(repeticiones[0], entropia_atributo)
        entropias_por_atributo.append([repeticiones[0], entropia_atributo])

    # %%
    #mostramos ahora si toda la lista de entropias de los atributos:

    # for entropia in entropias_por_atributo:
        # print(entropia)

    #tambien mostramos los valores observados por atributo

    # for observado in valores_observados_por_atributo_copia:
        # print(observado)

    # %%
    #para comenzar a generar el arbol, tomemos los atributos en función de la minima entropia
    entropia_minima = []
    valor_entropia = 1

    for entropia in entropias_por_atributo:
        if(entropia[1] < valor_entropia):
            entropia_minima = entropia

    # print(entropia_minima)

    # %%
    #conociendo el atributo con menor entropia genramos la regla

    nueva_rama = None
    atributos_rama = []

    for valor_observado in valores_observados_por_atributo_copia:
        if(valor_observado[0] == entropia_minima[0]):
            if(len(valor_observado[1]) <= 14):
                # print(valor_observado)

                for atribute in valor_observado[1]:
                    atributos_rama.append(atribute[0])

            break

    for valor_observado in valores_observados_por_atributo_no_categorico:
        if(valor_observado[0] == entropia_minima[0]):
            # print("no categorico\n\n",valor_observado)

            for atribute in valor_observado[1]:
                atributos_rama.append(atribute[0])
            
            break

    # print(atributos_rama)

    #creamos la rama

    nueva_rama = rama(atributos_rama, entropia_minima[0])

    nueva_rama.mostrarRama()


    return nueva_rama