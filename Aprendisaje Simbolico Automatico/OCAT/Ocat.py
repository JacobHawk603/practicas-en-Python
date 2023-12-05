class Selector:

    etiqueta:str
    valor:any
    positivo:bool

    def __init__(self, etiqueta:str, valor, positivo:bool = True):
        self.etiqueta = etiqueta
        # self.valor = valor
        self.positvo = positivo
    
    def __str__(self):

        cadena:str = ""

        if not self.positvo:
            cadena += "¬"

        cadena += f"[{self.etiqueta} = {self.valor}]"

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

    selectores:list[Selector]

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

class Cubrimiento:

    etiqueta:str
    complejos:list[Complejo]

    def __init__(self, etiqueta:str, complejos:list[Complejo] | None = None):
        
        self.complejos = complejos

        if not complejos == None:
            self.etiqueta = etiqueta

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