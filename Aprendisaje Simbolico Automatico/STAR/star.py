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

        banderas_selectores:list[bool] = []

        for un_selector in self.selectores:
            
            for i, row in dataset_casos_positivos.iterrows():

                if row[un_selector.etiqueta] == un_selector.valor:
                    banderas_selectores.append(True)
                else:
                    banderas_selectores.append(False)

            #revisamos si todas las banderas son verdaderas, en ese caso, si está cubriendo al ejemplo positivo
            # de lo contrario, con una sola bandera que sea falsa, no cubre al ejemplo positivo

            for i, bandera in enumerate(banderas_selectores):
                
                if i >= len(banderas_selectores)-1:
                    #todas las banderas son verdaderas, por lo que si cubre al ejemplo positivo
                    self.cobertura +=1


            
            


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