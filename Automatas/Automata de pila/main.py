from random import randint

class nodo:
    dato = None
    siguienteDato = None

class pila:
    tope = nodo()

    # def Pila(self):
    #     return 0

    def estaVacia(self):
        if self.tope.dato == None:
            return True
        else:
            return False

    def vaciarPila(self):

        while not self.estaVacia():
            self.sacarElemento()
    
    def agregarElemento(self, elemento):
        
        nuevoDato = nodo()
        nuevoDato.dato = elemento
        nuevoDato.siguienteDato = self.tope

        self.tope = nuevoDato

    
    def sacarElemento(self):
        
        if self.estaVacia():
            print("error, la pila ya estaba vacía")
            exit(1)
        
        x = self.tope.dato
        temporal = self.tope
        self.tope = self.tope.siguienteDato

        del temporal

        return x
    
    def nodoInicio(self):
        '''muestra el primer dato de la pila'''

        if self.tope == None:
            print("error, la pila esta vacia")
            exit(1)
        
        return self.tope.dato

    def mueve(self, pila):
        '''mueve todos los elementos de una pila externa, a nuestra pila'''
        x = 0

        while not pila.estaVacia():
            x = pila.sacarElemento()
            self.agregarElemento(x)
    
    def mostrarPila(self):
        '''muestra todos los elementos de nuestra pila'''

        if self.estaVacia():
            print("la pila esta vacia")
            return

        pilaAuxiliar = pila()
        x = 0

        print("los elementos de la pila son:\n\n")

        while not self.estaVacia():
            x = self.sacarElemento()
            print(x)
            pilaAuxiliar.agregarElemento(x)

        #devolvemos los datos de la pila auxiliar a la pila original
        self.mueve(pilaAuxiliar)

        print("\n\n")
    
    def cantidadElementos(self):
        '''regresa la cantidad de elementos que existen en la pila'''

        if self.estaVacia():
            return 0
        
        pilaAuxiliar = pila()
        x = 0
        contador = 0

        while not self.estaVacia:
            x = self.sacarElemento()
            pilaAuxiliar.agregarElemento(x)
            contador +=1
        
        #regresamos los elementos a la pila original
        self.mueve(pilaAuxiliar)

        return contador



def fcl(estado, caracter, ultimoAlmacenado):
    '''
    enota por sus siglas el lenguaje libre de contexto\n\n
    
    estado <- (bool) elemento booleano que servirá para denotar p y q:\n\t
        True <- denota al estado q\n\t
        False <- denota al estado p\n\n
    
    caracter <- (char) caracter 0 o 1 procedente de una cadena que estemos evaluando\n\n
    
    ultimoAlmacenado <-(char) es el ultimo valor que almacenamos en la pila procedente de la cadena que estamos evaluando
    '''
    q = True
    p = False

    global miPila
    global rechazada

    if estado == q and caracter == '0':
        
        print("(q, 0, {})".format(miPila.tope.dato))
        miPila.agregarElemento('X')

    elif estado == q and caracter == '1':
        estado = p

    if estado == p:

        if caracter == '1' and ultimoAlmacenado != None:

            print("(p, 1, {})".format(miPila.tope.dato))
            miPila.sacarElemento()

        elif caracter == '1' and ultimoAlmacenado == None:

            print("(p, 1, {})".format(miPila.tope.dato))
            print("sigue solicitando sacar datos de la pila, pero ya esta vacia, la cadena no es valida")

            rechazada = True

    return estado


def generarCadena(longitud):
    '''
    devuelve una cadena de longitud "longitud"\n\n

    **nota: la probabilidad de que sea aceptada una cadena que se ha generado bajo este metodo es muy baja,
    ya que para ser aceptada debe de ser simétrica, y en este metodo, partiendo de la longitud total, escoge
    de forma aleatoria la cantidad de ceros y unos**
    
    '''

    if longitud > 100000:
        print("la cadena no puede exceder los 10000 caracteres")
        exit(0)

    ceros = randint(0, longitud)
    unos = longitud-ceros

    cadena = ""

    for i in range (ceros):
        cadena += '0'

    for i in range (unos):
        cadena += '1'

    return cadena

if __name__ == "__main__":

    cadena = ""
    opcion = input("1. inresar la cadena manualmente\n2.generar la cadena automaticamente\n\n")
    
    if opcion == 2:
        longitud = input("longitud de la cadena")

        cadena = generarCadena(longitud)
    
    elif opcion == 1:

        #cadena = input("ingrese la cadena (primero ceros y después unos si desea que el programa funcione correctamente): ")
        cadena = "00001111"

    miPila = pila()
    rechazada = False

    # print("mi pila cuando se supone que esta vacia: ") 
    
    # print(miPila.mostrarPila())

    # miPila.agregarElemento(5)

    # print("mi pila cuando le agrego un elemento: ")
    # print(miPila.mostrarPila())

    # miPila.agregarElemento(2)

    # print("mi pila cuando le agrego otro elemento: ")
    # print(miPila.mostrarPila())

    # miPila.agregarElemento(6)

    # print("mi pila cuando le agrego otro elemento: ")
    # print(miPila.mostrarPila())

    # miPila.sacarElemento()

    # print("mi pila al quitarle un elemento")
    # print(miPila.mostrarPila())

    estado = True

    for i in range (len(cadena)):

        estado = fcl(estado, cadena[i], miPila.tope.dato)

    if miPila.estaVacia() and not rechazada:
        print("cadena aceptada")
    else:
        print("cadena rechazada")