import pandas as pd
import itertools
import copy

class selector:
    
    etiqueta:str
    valor:str

    def __init__(self, etiqueta:str, valor:str):
        
        self.etiqueta = etiqueta
        self.valor = valor

    def __str__(self):

        return "[{} = {}]".format(self.etiqueta, self.valor)
        
class complejo:

    etiqueta:str
    selectores:list[selector]
    cobertura:int = 0

    def __init__(self, selectores:list[selector], etiqueta:str):

        self.selectores = selectores
        self.etiqueta = etiqueta

    def __str__(self):

        # print("complejo: ", self.etiqueta, "\n\n")
        cadena:str = "complejo: "+ self.etiqueta+ "\n\n"

        for elemento in self.selectores:
            cadena += str(elemento) + " "

        return cadena + "\n\n"

    def agregarSelectores(self, nuevsos_selectores:list[selector]):
        
        for elemento in nuevsos_selectores:
            self.selectores.append(elemento)

    def encontrar_selector(self, etiqueta:str):

        for elemento in self.selectores:

            if elemento.etiqueta == etiqueta:
                return elemento


    def eliminar_selector(self, etiqueta:str):

        self.selectores.pop(self.selectores.index(self.encontrar_selector(etiqueta)))

    def calcular_cobertura(self, dataset_casos_positivos:pd.DataFrame):

        for i, row in dataset_casos_positivos.iterrows():
            
            banderas_selectores:list[bool] = []
            for un_selector in self.selectores:
                
                if row[un_selector.etiqueta] == un_selector.valor:
                        banderas_selectores.append(True)
                else:
                    banderas_selectores.append(False)

            #revisamos si todas las banderas son verdaderas, en ese caso, si está cubriendo al ejemplo positivo
            # de lo contrario, con una sola bandera que sea falsa, no cubre al ejemplo positivo

            for i, bandera in enumerate(banderas_selectores):
                
                if i == len(banderas_selectores)-1 and bandera:
                    #todas las banderas son verdaderas, por lo que si cubre al ejemplo positivo
                    self.cobertura +=1
                
                elif not bandera:
                    break

    def lo_cubre(self, row:pd.DataFrame):
        
        banderas:list[bool] = []

        for un_selector in self.selectores:

            if row[un_selector.etiqueta] == un_selector.valor:
                
                banderas.append(True)
            
            else:
                
                return False
        

        #revisamos si todas las banderas son verdaderas, en ese caso, si está cubriendo al ejemplo positivo
            # de lo contrario, con una sola bandera que sea falsa, no cubre al ejemplo positivo

        for i, bandera in enumerate(banderas):
            
            if i == len(banderas)-1 and bandera:
                #todas las banderas son verdaderas, por lo que si cubre al ejemplo positivo
                return True
            
            elif not bandera:
                return False


class cubrimiento:

    etiqueta:str
    complejos:list[complejo]

    def __init__(self, complejos:list[complejo], etiqueta:str):
        
        self.complejos = complejos
        self.etiqueta = etiqueta

    def __str__(self):

        # print("cubrimiento: ", self.etiqueta, "\n\n")

        cadena:str = "cubrimiento: "+ self.etiqueta+ "\n\n"

        for elemento in self.complejos:
            cadena += str(elemento) + "\n"
        
        return cadena

    def agregarComplejos(self, nuevos_complejos:list[complejo]):

        for elemento in nuevos_complejos:
            self.complejos.append(elemento)
    
    def encontrarComplejo(self, etiqueta:str):

        for elemento in self.complejos:

            if elemento.etiqueta == etiqueta:
                return elemento
            
    def eliminar_complejo(self, etiqueta:str):

        print("la etiqueta: ", etiqueta)
        self.complejos.pop(self.complejos.index(self.encontrarComplejo(etiqueta)))

class estrella:

    Su_Cubrimiento:cubrimiento

    def generarEstrella(self, semilla:pd.DataFrame, dominios_atributos:list[list[str]]):

        atributos = semilla.drop('Class', axis=1).values.tolist()

        print(atributos)

        clase = semilla['Class'].values
        etiquetas:list[str] = semilla.drop(['Class'], axis=1).columns.to_list()

        #generamos las conbinaciones n en k con los elementos de la semilla
        combinaciones:list[list[str]] = []

        for i in range(1, len(*atributos)+1):

            for combinacion in itertools.combinations(*atributos, i):
                combinaciones.append(list(combinacion))
        
        print("las combinaciones son: \n\n", combinaciones)
        print("longitud total:", len(combinaciones))

        complejos:list[complejo] = []

        for i, combinacion in enumerate(combinaciones):

            selectores:list[selector] = []
            for atributo in combinacion:

                #para saber a que columna pertenece, tenemos que comparar el atributo con los dominios de cada columna
                etiqueta:str = ""

                for j, dominio in enumerate(dominios_atributos):
                    if dominio.__contains__(atributo):
                        etiqueta = etiquetas[j]
                        break


                selectores.append(selector(etiqueta, atributo))
    
            complejos.append(complejo(selectores ,'complejo {}'.format(i)))

            # selectores.clear()
        
        #por el momento, para ver como va quedando la codificacion, veamos agreguemos ese complejo al cobrimiento y veamos el resultado

        self.Su_Cubrimiento = cubrimiento(complejos, "cubrimiento de {} -> {}".format(*atributos, clase))

        # print(self.Su_Cubrimiento)

    def eliminar_complejos_que_cubren_ejemplos_negativos(self, dataset_ejemplos_negativos:pd.DataFrame):

        for i, row in dataset_ejemplos_negativos.iterrows():

            #para la fila que estamos revisando, observemos TODOS los complejos, y revisemos cuales cubren a la fila

            for mi_complejo in self.Su_Cubrimiento.complejos:

                banderas_selectores:list[bool] = []
                for un_selector in mi_complejo.selectores:
                    
                    if row[un_selector.etiqueta] == un_selector.valor:
                        banderas_selectores.append(True)

                    else:
                        banderas_selectores.append(False)
                
                # si todas las banderas son verdaderas, implica que el complejo está cubriendo al ejemplo negativo
                # si alguna bandera es falsa, el complejo no cubre al ejemplo negativo

                for i, bandera in enumerate(banderas_selectores):

                    if not bandera:
                        # no cubre al ejemplo negativo, podemos saltar a la siguiente iteración
                        break

                    else:

                        if i >= len(banderas_selectores)-1 and bandera:
                            # en este caso, todas las banderas se cumplieron, se esta cubriendo un ejemplo negativo, por lo que hayq eu eliminar este complejo
                            self.Su_Cubrimiento.eliminar_complejo(mi_complejo.etiqueta)

    def reducirEstrella(self, dataset_casos_positivos:pd.DataFrame):

        #calculamos la cobertura de todos y cada uno de los complejos, para seleccionar el o los complejos con mayor cobertura
        for un_complejo in self.Su_Cubrimiento.complejos:
            un_complejo.calcular_cobertura(dataset_casos_positivos)

        #ahora con todas las coberturas listas, identificamos si hay alguno que tenga una mayor cobertura
        cobertura_maxima:int = 0
        complejos_coberturas:list[tuple[int, complejo]] = []

        for i, un_complejo in enumerate(self.Su_Cubrimiento.complejos):
            
            if un_complejo.cobertura > cobertura_maxima:
                cobertura_maxima = un_complejo.cobertura

                complejos_coberturas.append((cobertura_maxima, un_complejo))
            
            elif un_complejo.cobertura == cobertura_maxima:

                complejos_coberturas.append((un_complejo.cobertura, un_complejo))
            
            else:

                complejos_coberturas.append((un_complejo.cobertura, un_complejo))

        #ahora, todos los complejos que tengan la mayor cobertura al final del bucle anterior, sobrevivirán, el resto será funado
        print("la cobertura máxima: ", cobertura_maxima)
        for cobertura, elemento in complejos_coberturas:

            if cobertura < cobertura_maxima:

                #eliminamos el complejo
                print("el complejo {} con cobertura: {} será eliminado por la cobertura {}".format(elemento.etiqueta, elemento.cobertura, cobertura_maxima))
                self.Su_Cubrimiento.eliminar_complejo(elemento.etiqueta)
            
            else:
                print("el complejo {} con cobertura {} se salvó de la guillotina".format(un_complejo.etiqueta, un_complejo.cobertura))

    def Eliminar_Ejemplos_Cubiertos(self, dataset_casos_positivos:pd.DataFrame):

        # print(dataset_casos_positivos)

        for i, row in dataset_casos_positivos.iterrows():

            for un_complejo in self.Su_Cubrimiento.complejos:
                
                if un_complejo.lo_cubre(row):
                    dataset_casos_positivos = dataset_casos_positivos.drop(i)
                    break
        
        return dataset_casos_positivos
           
    

def generarCubrimiento(estrellas:list[estrella], casos_positivos:pd.DataFrame, casos_negativos:pd.DataFrame, dominios_completos_atributos:list[list[str]]):

    ##obtenemos la semilla
    semilla = casos_positivos.sample()  # <- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html

    ##generamos la estrella

    una_estrella = estrella()

    una_estrella.generarEstrella(semilla, dominios_completos_atributos)

   


    ## Eliminar complejos que cubren ejemplos negativos
    una_estrella.eliminar_complejos_que_cubren_ejemplos_negativos(casos_negativos)

   


    ## Reducir la estrella en la medida de lo posible
    una_estrella.reducirEstrella(casos_positivos)

    #hasta aquí ya quedó lista la estrella, as`+i que hay que agregarla a la lista de estrellas
    estrellas.append(una_estrella)


    # Si aún quedan ejemplos por cubrir, debemos de volver a seleccionar semilla
    ## Para esto, vamos a quitar del dataset de entrenamiento los registros que ya están cubiertos por alguna estrella
    casos_por_cubrir = una_estrella.Eliminar_Ejemplos_Cubiertos(casos_positivos)

    if not casos_por_cubrir.empty:
        generarCubrimiento(estrellas, casos_por_cubrir, casos_negativos, dominios_completos_atributos)
    

    #con el dataset nuevo dataset volvemos a seleccionar la semilla 

    # print(casos_por_cubrir)
    # print(casos_positivos)

    return estrellas

def prediccion_de_clase(estrellas:list[estrella], validacion:pd.DataFrame, clases:list[str]):

    predicciones:list[str] = []

    for i, row in validacion.iterrows():

        for una_estrella in estrellas:

            contador_auxiliar:int = 0
            for un_complejo in una_estrella.Su_Cubrimiento.complejos:

                if un_complejo.lo_cubre(row):

                    predicciones.append(clases[0])
                    break
                
                else:
                    contador_auxiliar +=1
            
            if contador_auxiliar >= len(una_estrella.Su_Cubrimiento.complejos):
                predicciones.append(clases[1])

            break
    
    return predicciones

def probarHipotesis(valores_predichos:list[str], valores_reales:list[str], casos_positivos:list[str]):

    vp = 0
    fp = 0
    vn = 0
    fn = 0

    for predicho, real in zip(valores_predichos, valores_reales):
        
        if(predicho == real and casos_positivos.__contains__(real)):
            vp += 1
        elif(predicho == real and not casos_positivos.__contains__(real)):
            vn += 1
        elif(predicho != real and not casos_positivos.__contains__(real)):
            fp += 1
        elif(predicho != real and not casos_positivos.__contains__(predicho) and casos_positivos.__contains__(real)):
            #un falso negativo en este algoritmo, en donde las estrellas son consistentes, solo puede implicar que el registro pertenece a ambas clases
            #por tanto, hagamos una modificación aquí, no agreguemos el ejemplo como un falso negativo, sino que agreguemosle .5 y .5 a los falses respectivamente
            # fn += 1
            fp += 0.5
            fn += 0.5

        elif(predicho != real and casos_positivos.__contains__(predicho) and casos_positivos.__contains__(real)):
            vp += 1

    accuracy = (vp + vn)/(vp + vn + fp + fn)
    presicion = vp/(vp + fp)
    recall = vp/(vp+fn)
    f1 = 2*((presicion * recall)/(presicion + recall))


    print("vp: {}\tfp: {}\nfn: {}\t vn: {}".format(vp, fp, fn, vn))
    print("accuracy: {}\nprecision: {}\nrecall: {}\nf1: {}".format(accuracy, presicion, recall, f1))
    return 0
