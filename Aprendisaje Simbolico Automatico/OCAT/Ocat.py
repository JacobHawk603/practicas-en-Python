import pandas as pd

class Selector:

    etiqueta:str
    valor:any
    positivo:bool

    def __init__(self, etiqueta:str, valor, positivo:bool = True):
        self.etiqueta = etiqueta
        self.valor = valor
        self.positvo = positivo
    
    def __str__(self):

        cadena:str = ""

        if not self.positvo:
            cadena += "¬"

        cadena += f"[{self.etiqueta} = {self.valor}]"

        return cadena
    
class Identificador:

    etiqueta:str
    row:int
    column:int

    def __init__(self, row:int, column:int, etiqueta:str):

        self.row = row
        self.column = column
        self.etiqueta = etiqueta

    def __str__(self):

        return f"X{self.row},{self.column}"
    
class Complejo:

    etiqueta:str
    selectores:list[Selector] = []

    def __init__(self, etiqueta:str, selectores:list[Selector] | None = None):
        self.etiqueta = etiqueta

        if not selectores == None:
            self.selectores = selectores

    def __str__(self):

        cadena:str = "("

        if len(self.selectores) > 0:

            for i, selector in enumerate(self.selectores):

                cadena += str(selector)

                if i < len(self.selectores)-1:
                    cadena += " "

        cadena += ")"

        return cadena
    
    def agregar_selectores(self, nuevsos_selectores:list[Selector]):
        
        for elemento in nuevsos_selectores:
            self.selectores.append(elemento)

    def encontrar_selector(self, etiqueta:str):

        for elemento in self.selectores:

            if elemento.etiqueta == etiqueta:
                return elemento


    def eliminar_selector(self, etiqueta:str):

        self.selectores.pop(self.selectores.index(self.encontrar_selector(etiqueta)))

    
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

class Cubrimiento:

    etiqueta:str
    complejos:list[Complejo] = []

    def __init__(self, etiqueta:str, complejos:list[Complejo] | None = None):
        
        self.etiqueta = etiqueta

        if not complejos == None:
            self.complejos = complejos

    def __str__(self):

        # print("cubrimiento: ", self.etiqueta, "\n\n")

        # cadena:str = "cubrimiento: "+ self.etiqueta+ "\n\n"
        cadena:str = ""

        for elemento in self.complejos:
            cadena += str(elemento) + "\n"
        
        return cadena

    def agregarComplejos(self, nuevos_complejos:list[Complejo]):

        for elemento in nuevos_complejos:
            self.complejos.append(elemento)
    
    def encontrarComplejo(self, etiqueta:str):

        for elemento in self.complejos:

            if elemento.etiqueta == etiqueta:
                return elemento
            
    def eliminar_complejo(self, etiqueta:str):

        print("la etiqueta: ", etiqueta)
        self.complejos.pop(self.complejos.index(self.encontrarComplejo(etiqueta)))

def prediccion_de_clase(cobertura:Cubrimiento, validacion:pd.DataFrame, clases:list[str]):

    predicciones:list[str] = []

    for i, row in validacion.iterrows():

        contador_auxiliar:int = 0
        for complejo in cobertura.complejos:

            if complejo.lo_cubre(row):

                predicciones.append(clases[0])
                break
            
            else:
                contador_auxiliar +=1
        
        if contador_auxiliar >= len(cobertura.complejos):
            predicciones.append(clases[1])

        # break
    
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
        elif(predicho != real and casos_positivos.__contains__(real)):
            #un falso negativo en este algoritmo, en donde las estrellas son consistentes, solo puede implicar que el registro pertenece a ambas clases
            #por tanto, hagamos una modificación aquí, no agreguemos el ejemplo como un falso negativo, sino que agreguemosle .5 y .5 a los falses respectivamente
            fn += 1
            # fp += 0.5
            # fn += 0.5

        elif(predicho != real and casos_positivos.__contains__(predicho) and casos_positivos.__contains__(real)):
            vp += 1

    accuracy = (vp + vn)/(vp + vn + fp + fn)
    presicion = vp/(vp + fp)
    recall = vp/(vp+fn)
    f1 = 2*((presicion * recall)/(presicion + recall))


    print("vp: {}\tfp: {}\nfn: {}\t vn: {}".format(vp, fp, fn, vn))
    print("accuracy: {}\nprecision: {}\nrecall: {}\nf1: {}".format(accuracy, presicion, recall, f1))
    return 0