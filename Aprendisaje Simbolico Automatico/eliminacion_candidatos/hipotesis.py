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

    # print("me estoy invocando")
    # for valor_observado in fila:

    #     bandera_mochadora = False
    
    #     for hipotesis in hipotesis_generales:

    #         if not hipotesis.aceptados[fila.index(valor_observado)].__contains__(valor_observado):
                
    #             #si no se encuentra el valor observado en la lista de aceptados de la hipotesis, tenemos que eliminarla
    #             bandera_mochadora = True

    #         else:
    #             print("no mochamos nada")

    #     if bandera_mochadora:

    #         print("mochamos la hipotesis general, porque {} no aparece en la misma".format(valor_observado))
    #         hipotesis_generales.pop(hipotesis_generales.index(hipotesis))


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
        
        else:
            
            print("no mochamos nada")

        
    while(len(hipotesis_rechazadas)>0):
        
        hipotesis_a_mochar = hipotesis_rechazadas.pop()

        print("mochamos la hipotesis general, porque {} no aparece en la misma".format(valor_observado))
        hipotesis_generales.pop(hipotesis_generales.index(hipotesis_a_mochar))
            


    return hipotesis_generales