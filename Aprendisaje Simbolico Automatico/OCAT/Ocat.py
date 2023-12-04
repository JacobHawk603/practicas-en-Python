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

        cadena += f"[{self.etiqueta} >= {self.valor}]"

        return 
    
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
    
    identificadores:list[Identificador]

    def __str__(self):

        cadena:str = "("

        if len(self.identificadores) > 0:

            for i, identificador in enumerate(self.identificadores):

                cadena += str(identificador)

                if i < len(self.identificadores)-1:
                    cadena += " or "

        cadena += ")"

        return cadena
    
    def agregarIdentificadores(self, nuevsos_identificadores:list[Selector]):
        
        for elemento in nuevsos_identificadores:
            self.identificadores.append(elemento)

    def encontrar_identificador(self, etiqueta:str):

        for elemento in self.identificadores:

            if elemento.etiqueta == etiqueta:
                return elemento


    def eliminar_identificador(self, etiqueta:str):

        self.identificadores.pop(self.identificadores.index(self.encontrar_identificador(etiqueta)))