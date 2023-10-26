from random import randint, uniform

class General:

    acepta_todo:bool
    etiquetas:list[str]
    rechazados:list[list[str]]
    aceptados:list[list[str]]

    def __init__(self, etiquetas_atributos:list[str] = None, acepta_todo:bool = True) -> None:

        self.acepta_todo = acepta_todo
        self.etiquetas = etiquetas_atributos
        self.rechazados = []
        self.aceptados = []
        
        for i in range(len(etiquetas_atributos)):
            self.rechazados.append([])
            self.aceptados.append([])

    def __str__(self):

        cadena = ""

        if self.acepta_todo:  
            
            for i in range(len(self.etiquetas)):
                cadena += '*,'

            cadena = cadena[:len(cadena)-1]
        
        else:

            for aceptados_atributo in self.aceptados:
                
                if len(aceptados_atributo) == 0:

                    cadena += "*, "

                else:

                    cadena += "{}, ".format(aceptados_atributo)

            cadena = cadena[:len(cadena)-2]
            
        return "<{}>".format(cadena)
    
    
    def especializar(self, etiqueta:str, atributo:str):

        if self.acepta_todo:
            
            self.acepta_todo = False
            self.rechazados[self.etiquetas.index(etiqueta)].append(atributo)
        
        else:

            self.rechazados[self.etiquetas.index(etiqueta)].append(atributo)

    def agregar_aceptados(self, etiqueta:str, atributo:str):

        if self.acepta_todo:
            
            self.acepta_todo = False
            self.aceptados[self.etiquetas.index(etiqueta)].append(atributo)
        
        else:

            self.aceptados[self.etiquetas.index(etiqueta)].append(atributo)


class Especifica:

    acepta_vacio:bool
    etiquetas:list[str]
    aceptados:list[list[str]]

    def __init__(self, etiquetas_atributos:list[str] = None, acepta_vacio:bool = True) -> None:
        
        self.acepta_vacio = acepta_vacio
        self.etiquetas = etiquetas_atributos
        self.aceptados = []
        
        for i in range(len(etiquetas_atributos)):
            self.aceptados.append([])

    def generalizar(self, etiqueta:str, atributo:str):

        if not self.acepta_vacio:
            self.aceptados[self.etiquetas.index(etiqueta)].append(atributo)

        else:
            self.acepta_vacio = False
            self.aceptados[self.etiquetas.index(etiqueta)].append(atributo)


    def __str__(self):

        cadena = ""

        if self.acepta_vacio:  
            
            for i in range(len(self.etiquetas)):
                cadena += '0,'

            cadena = cadena[:len(cadena)-1]
        
        else:

            for aceptados_atributo in self.aceptados:

                if len(aceptados_atributo) == 0:

                    cadena += "0, "

                else:
                
                    cadena += "{}, ".format(aceptados_atributo)
            
            cadena = cadena[:len(cadena)-2]
            
        return "<{}>".format(cadena)
    

def minimas_Especializaciones(hipotesis_general:General, dominios_atributos:list[list[str]]):

    #Lo ideal es que la lista de hipotesis, solo contenga 1 elemento para cuando sea invocada esta función

    minimasEspecializaciones:list[General] = []
    index_etiqueta = 0

    for dominio_atributo in dominios_atributos:
        
        for valor_observado in dominio_atributo:
            #creamos una hipotesis general
            nueva_hipotesis = General(hipotesis_general.etiquetas)
            nueva_hipotesis.agregar_aceptados(nueva_hipotesis.etiquetas[index_etiqueta], valor_observado)

            minimasEspecializaciones.append(nueva_hipotesis)

        index_etiqueta+=1


    return minimasEspecializaciones


def validar_hipotesis_generales(hipotesis_generales:list[General], fila:list[str], caso_positivo:bool = True):

    hipotesis_rechazadas = []

    for hipotesis in hipotesis_generales:

        bandera_mochadora = True

        print("hipotesis que estamos evaluando: {}\n".format(hipotesis))

        for aceptados, valor_observado in zip(hipotesis.aceptados, fila):

            print("valor observado: {}\t lista de aceptados: {}".format(valor_observado, aceptados))

            if caso_positivo:
            
                if aceptados.__contains__(valor_observado):

                    bandera_mochadora = False

            else:

                if not aceptados.__contains__(valor_observado):

                    bandera_mochadora = False

        if bandera_mochadora:
            
            hipotesis_rechazadas.append(hipotesis)
            print("mochamos la hipotesis general {} porque no cubre al caso observado".format(hipotesis))
        
        else:
            
            print("no mochamos nada")

        
    while(len(hipotesis_rechazadas)>0):
        
        hipotesis_a_mochar = hipotesis_rechazadas.pop()

        hipotesis_generales.pop(hipotesis_generales.index(hipotesis_a_mochar))
            


    return hipotesis_generales

def predicciones(fila:list[str], hipotesis_general:General=None, hipotesis_especifica:Especifica=None):

    banderas:list[bool] = []
    contador_banderas = 0

    for i in range(len(fila)):
        banderas.append(False)

    if hipotesis_general != None:

        for valor_observado, aceptados, bandera_index in zip(fila, hipotesis_general.aceptados, range(len(banderas))):

            print("len aceptados: ", len(aceptados))

            if len(aceptados) > 0:

                for aceptado in aceptados:

                    if(aceptado == valor_observado):
                        banderas[bandera_index] = True
            else:
                banderas[bandera_index] = True

        for bandera in banderas:
            if bandera:
                contador_banderas +=1
        
        if(contador_banderas >= len(banderas)):
            return randint(1, 2)
        
        else:
            print("este es el contador:", contador_banderas)
            return 3
        
    else:

        #estamos evaluando la hipotesis esecifica

        for valor_observado, aceptados, bandera_index in zip(fila, hipotesis_especifica.aceptados, range(len(banderas))):

            if len(aceptados) > 0:

                for aceptado in aceptados:
            
                    if(aceptado == valor_observado):
                        banderas[bandera_index] = True

            else:
                banderas[bandera_index] = True

        for bandera in banderas:
            if bandera:
                contador_banderas +=1
        
        if(contador_banderas >= len(banderas)):
            return randint(1, 2)
        
        else:
            return 3
        
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
            fn += 1
        elif(predicho != real and casos_positivos.__contains__(predicho) and casos_positivos.__contains__(real)):
            vp += 1

    accuracy = (vp + vn)/(vp + vn + fp + fn)
    presicion = vp/(vp + fp)
    recall = vp/(vp+fn)
    f1 = 2*((presicion * recall)/(presicion + recall))


    print("vp: {}\tfp: {}\nfn: {}\t vn: {}".format(vp, fp, fn, vn))
    print("accuracy: {}\nprecision: {}\nrecall: {}\nf1: {}".format(accuracy, presicion, recall, f1))
    return 0

def probarHipotesis2(predicciones_generales:list[list[str]], prediccion_especifica:list[str], porcentaje_general:float = 0.75):

    porcentaje_por_hipotesis_general = porcentaje_general/len(predicciones_generales)
    porcentaje_especifico = 1 - porcentaje_general

    valor_aleatorio = uniform(0,1)

    matriz_predicciones = predicciones_generales
    matriz_predicciones.append(prediccion_especifica)

    prediccion_final:list[str] = []

    for i in range(len(matriz_predicciones[0])):

        if(valor_aleatorio > porcentaje_general):
            prediccion_final.append(prediccion_especifica[0])
        
        else:
            modulo = int(valor_aleatorio % porcentaje_por_hipotesis_general)

            prediccion_final.append(predicciones_generales[modulo][i])

    return prediccion_final