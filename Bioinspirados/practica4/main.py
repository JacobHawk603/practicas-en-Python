import random

#variables globales---------------------------------------------------------------------------------------------------------------
sn = 3
#---------------------------------------------------------------------------------------------------------------------------------

class fuenteDeAlimento():
    global sn
    limite = sn #<- SN/2 * D siendo D = 2, ya que D es equivalente a la cantidad de variables a optimizar, y en este caso son x y y
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def aptitud(self):
        return self.x**2 + self.y**2

    def resetLimite(self):
        '''reseta la variable limite a su valor inicial (que para este problema es sn)'''
        self.limite = sn

    def mostrarFuente(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class obrera:
    observadoras = []   #<- lista que contiene las observadoras que estan siguiendo a la obrera
                        #   esto con el objetivo de tener referencias de las obicaciones de estas observadoras, cercanas a la obrera

    def __init__(self, fuenteComida): #<- (estado) 0: inactivo (no tiene este rol asignado), 1: activo
        self.fuenteComida = fuenteComida

    def abandonarFuente(self):
        '''retira la informacion de la fuente de alimento, y una vez que de hace esto, se debe de cambiar el rol de la abeja'''

        self.fuenteComida = None

    def explotarFuente(self, xk, yk):
        '''
        visita una flor cercana a su solucion asociada, y evalua la aptitud\n\n
        si la aptitud de la flor cercana es mejor que la aptiud de la solucion, el limite regresará a cero, y la solución tomara como centro
        la nueva ubicacion encontrada\n\n

        en caso contrario, el limite decrementara 1 unidad su valor, y si este llega a cero, se debe de abandonar la fuente de alimento\n\n

        (xk,yk) -> coordenadas de la solucion de alguna abeja que se encuentre por ahí
        '''

        x = self.fuenteComida.x + random.uniform(-1,1) * (self.fuenteComida.x - xk)
        y = self.fuenteComida.y + random.uniform(-1,1) * (self.fuenteComida.y - yk)

        flor = fuenteDeAlimento(x,y)

        if flor.aptitud > self.fuenteComida:
            self.fuenteComida = flor
        else:
            self.fuenteComida.limite -= 1

    def limpiarObservadoras(self):
        self.observadoras.clear()


class observadora:

    abejaObrera = None
    fuenteAlimento = None
    
    def evaluarFuente(self, fuenteDeAlimento):
        '''
        evalua la fit de la solucion de alguna abeja obrera y decide si la sigue o no\n\n

        fuenteDeAlimento -> (fuenteAlimento)\n\n
        '''
        fit = 0

        #se trata de un problema de minimizacion, asi que tenemos que transformar el fitness
        if fuenteDeAlimento.aptitud() >= 0:
            fit = 1/(1+fuenteDeAlimento.aptitud())
        else:
            fit = 1 + abs(fuenteDeAlimento.aptitud())

        return fit

    
    def elegirObrera(self, obreras):
        '''
        realiza la seleccion de la observadora sobre que abeja obrera seguir\n\n

        obreras -> (lista -> abejas) lista de abejas con todas las abejas que tienen el rol de obreras
        '''        
        
        #creamos una lista auxiliar que contendra todas las abejas obreras, junto con su probabilidad de seleccion
        p_sel = []
        
        #todas las abejas observadoras van a determinar el mismo valor de aptitud para cada una de las soluciones de las obreras
        #asi que podemos sacar el fit acumulado una sola vez y funcionara igual que si lo evaluamos con todas
        fit_sum = 0

        for obrera in obreras:
            fit_sum += self.evaluarFuente(obrera.abejaObrera.fuenteComida)

        #teniendo el fit acumulado, ahora podemos sacar la probabilidad de seleccion y tenemos que volver a recorrer todo el arreglo de obreras
        for obrera in obreras:

            print("obrera in obreras:\t", obrera)
            proba = self.evaluarFuente(obrera.abejaObrera.fuenteComida)/fit_sum

            p_sel.append([obrera, proba])

        #aplicamos la ruleta para seleccionar a la abeja obrera
        print("despues de obrera in obreras:\t", p_sel)
        self.abejaObrera = ruleta(p_sel)
        print(type(self.abejaObrera))
        self.abejaObrera.observadoras.append(self)  # <- la observadora se anota ella misma en la lista de las observadoras que siguen a la obrera

    def explotarFuente(self, xk, yk):
        '''
        visita una flor cercana a su solucion asociada, y evalua la aptitud\n\n
        si la aptitud de la flor cercana es mejor que la aptiud de la solucion, el limite regresará a cero, y la solución tomara como centro
        la nueva ubicacion encontrada\n\n

        en caso contrario, el limite decrementara 1 unidad su valor, y si este llega a cero, se debe de abandonar la fuente de alimento\n\n

        (xk,yk) -> coordenadas de la solucion de alguna abeja que se encuentre por ahí
        '''

        x = self.fuenteComida.x + random.uniform(-1,1) * (self.fuenteComida.x - xk)
        y = self.fuenteComida.y + random.uniform(-1,1) * (self.fuenteComida.y - yk)

        flor = fuenteDeAlimento(x,y)    #<- en el caso de la observadora, esta va a ser la solución que representará

        if flor.aptitud > self.abejaObrera.fuenteComida:
            self.abejaObrera.fuenteComida = flor
        else:
            self.abejaObrera.fuenteComida.limite -= 1

        self.fuenteAlimento = flor



class exploradora:
    
    def buscarFuenteDeComida(self):

        '''retorna una fuente de alimento, y una vez hecho esto, debe procederse a cambiar el rol de la abeja'''

        x = -5 + random.uniform(0,1) * (5 -(-5))    #<-- los limites superior e inferior son [-5,5]
        y = -5 + random.uniform(0,1) * (5 -(-5))    #<-- los limites superior e inferior son [-5,5]

        fuenteEncontrada = fuenteDeAlimento(x,y)

        return fuenteEncontrada

    


class abeja:
    abejaExploradora = None
    abejaObservadora = None
    abejaObrera = None
    
    def __init__(self, rol, fuenteAlimento = None):
        '''
        rol -> (int): 0: obrera, 1: exploradora, 2: observadora\n\n
        fuenteAlimento -> (fuenteDeAlimento) por defecto, None\n\n
        **nota: se puede dejar vacio la fuente de alimento si no se va a cambiar el rol de la abeja a obrera, o de lo contrario
        aparecera un error en la ejecucion**
        '''
        self.rol = rol

        if rol == 0:
            self.abejaObrera = obrera(fuenteAlimento)
            self.abejaExploradora = None
            self.abejaObservadora = None
        elif rol == 1:
            self.abejaExploradora = exploradora()
            self.abejaObrera = None
            self.abejaObservadora = None
        elif rol == 2:
            self.abejaObservadora = observadora()
            self.abejaExploradora = None
            self.abejaObrera = None
    
    def cambiarRol(self, rol, fuenteAlimento = None):
        '''Las abejas en ABC pueden cambiar de rol bajo siertas condiciones, por ello, este metodo permite que la abeja en cuestion pueda cambiar su rol en la colmena'''

        self.rol = rol

        if rol == 0:
            self.abejaObrera = obrera(fuenteAlimento)
            self.abejaExploradora = None
            self.abejaObservadora = None
        elif rol == 1:
            self.abjeaExploradora = exploradora()
            self.abejaObrera = None
            self.abejaObservadora = None
        elif rol == 2:
            self.abejaObservadora = observadora()
            self.abjeaExploradora = None
            self.abejaObrera = None

    def mostrarAbeja(self):

        if self.rol == 0:
            print("rol: {}\t fuente de comida: {}\t aptitud: {}".format("obrera", self.abejaObrera.fuenteComida.mostrarFuente(), self.abejaObrera.fuenteComida.aptitud))
        elif self.rol == 1:
            print("rol: {}\t no tiene fuente de comida asignada".format("exploradora"))
        elif self.rol == 2:
            print("rol: {}\t fuente de comida: {}\t aptitud: {}".format("observadora", self.abejaObservadora.fuenteAlimento.mostrarFuente(), self.abejaObservadora.fuenteAlimento.aptitud))


class colmena:

    observadoras = []
    obreras = []
    exploradoras = []
    
    def __init__(self, abejas):
        '''
        abejas  -> (list(abeja)) lista de tipo abeja, la cual contiene a las abejas que perteneceran a la colmena
        '''
        self.abejas = abejas


    def agregarAbeja(self, abeja):
        '''
        anade a la colmena a una nueva abeja\n\n

        abeja -> (abeja) objeto de la clase abeja que sera agregado a la colmena
        '''

        self.abejas.append(abeja)

    def verAbejas(self):

        for abeja in self.abejas:
            abeja.mostrarAbeja()

    def clasificarAbejas(self):

        '''
        clasifica a cada abeja y guarda 3 listas que contienen a cada abeja en su respectivo grupo
        '''

        self.observadoras.clear()
        self.exploradoras.clear()
        self.observadoras.clear()

        for i in range(len(self.abejas)):

            if abejas[i].rol == 0:
                self.obreras.append(self.abejas[i])
            elif abejas[i].rol == 1:
                self.exploradoras.append(self.abejas[i])
            elif abejas[i].rol == 2:
                self.observadoras.append(self.abejas[i])


def ruleta(p_sel):
    
    '''
    p_sel -> (lista -> [obrera, probabilidad de seleccion])\n\n

    return: abejaObrera
    '''
    print("lo que llega a la ruleta:\t", p_sel)
    #obtenemos la probabilidad acumulada para cada obrera
    p_acum = []
    for i in range(len(p_sel)):
        acumulada = 0
        for j in range(i):
            print("me ejecuto\t", p_sel[j])
            acumulada += p_sel[j][1]
        
        p_acum.append([p_sel[i][0], acumulada])  #<- guardamos a la abeja obrera y a su probabilidad acumulada

    #ahora tenemos que tirar un random para seleccionar a que abeja seguimos

    valorAleatorio = random.uniform(0,1)
    print("valor aleatorio de la ruleta: ", valorAleatorio)

    print("todo el p_acum:", p_acum)

    for i in range(len(p_acum[0])):

        print("un valor de P_acum", p_acum[i])

        if valorAleatorio < p_acum[i][1]:
            print("otro print: \n\n\n", type(p_acum[i][0]))
            return p_acum[i][0]



    
    

if __name__ == "__main__":

    #dase de inicializacion------------------------------------------------------------------------------------------------------
    abejas = []
    miColmena = None
    #anadimos primero a las exploradoras y a las observadoras. Las exploradoras pasaran pronto a ser obreras
    #al lanzar a las abejas exploradoras encontramos encontramos las primeras fuentes de alimento de forma aleatoria (inicializamos las fuentes de alimento)

    for i in range (sn):
        abejas.append(abeja(1))
    
    #en este momento las abejas exploradoras ya han encontrado la fuente de alimento, es momento de transformarlas en obreras

    for i in range(sn):
        abejas[i] = abeja(0, fuenteAlimento=abejas[i].abejaExploradora.buscarFuenteDeComida())
        
    #creamos a las abejas observadoras

    for i in range(sn):
        abejas.append(abeja(2))

    #anadimos todas las abejas a la colmena

    miColmena = colmena(abejas)

    #fin de la dase de inicializacion-----------------------------------------------------------------------------------------------
    #agrupamos a cada abeja con uno de los 3 roles
    miColmena.clasificarAbejas()

    #fase de las abejas obreras-----------------------------------------------------------------------------------------------------

    #la recien obrera regresa con la informacion de la fuente de comida y baila para informar a las obseravdoras
    for i in range(len(miColmena.observadoras)):
        miColmena.observadoras[i].abejaObservadora.elegirObrera(miColmena.obreras)

     #ahora es el turno de las observadoras de explotar su fuente de alimento

    for i in range(len(miColmena.observadoras)):
        miColmena.observadoras[i].abejaObservadora.explotarFuente(miColmena.observadoras[i].abejaObrera.fuenteComida.x, miColmena.observadoras[i].abejaObrera.fuenteComida.y)

    #una vez que ya bailó la obrera, regresa a explotar la fuente de alimento

    for i in range(len(miColmena.obreras)):
        abejaReferencia = random.randint(0, len(miColmena.obreras[i].abejaObrera.observadoras))
        miColmena.obreras[i].abejaObrera.explotarFuente(miColmena.obreras[i].abejaObrera.observadoras[abejaReferencia].abejaObservadora.fuenteAlimento.x, miColmena.obreras[i].abejaObrera.observadoras[abejaReferencia].abejaObservadora.fuenteAlimento.y)



    #aqui hagamos una impresion para ir viendo como van las cosas
    print(type(miColmena))
    miColmena.verAbejas()