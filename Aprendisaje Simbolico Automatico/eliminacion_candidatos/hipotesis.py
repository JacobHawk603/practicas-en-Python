class General:

    acepta_todo:bool
    etiquetas:list[str]
    rechazados:list[list[str]]

    def __init__(self, etiquetas_atributos:list[str] = None, acepta_todo:bool = True) -> None:

        self.acepta_todo = acepta_todo
        self.etiquetas = etiquetas_atributos
        self.rechazados = []
        
        for i in range(len(etiquetas_atributos)):
            self.rechazados.append([])

    def __str__(self):

        cadena = ""

        if self.acepta_todo:  
            
            for i in range(len(self.etiquetas)):
                cadena += '*,'

            cadena = cadena[:len(cadena)-1]
        
        else:

            for rechazados_atributo in self.rechazados:
                
                cadena += "* - [{}]".format(rechazados_atributo)
            
        return "<{}>".format(cadena)

    
    def especializar(self, etiqueta:str, atributo:str):

        if self.acepta_todo:
            
            self.acepta_todo = False
            self.rechazados[self.etiquetas.index(etiqueta)].append(atributo)
        
        else:

            self.rechazados[self.etiquetas.index(etiqueta)].append(atributo)

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
                
                cadena += "{}, ".format(aceptados_atributo)
            
            cadena = cadena[:len(cadena)-2]
            
        return "<{}>".format(cadena)