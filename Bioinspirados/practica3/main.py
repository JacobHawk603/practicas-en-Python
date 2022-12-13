import random

class particula:
    pbest = [1000,1000,2000000] #<- [valorX, valorY, aptitud]
    velocidad = [random.uniform(-5, 5), random.uniform(-5, 5)] #<- inicializar velocidad con distribucion uniforme usando los parametros para x y y

    def __init__(self, valorX = 0, valorY = 0):
        '''por defecto se inicializa con (0,0)'''

        self.valorX = valorX
        self.valorY= valorY

    def aptitud(self):
        '''debuelve la aptitud el individuo con base en la funcion objetivo'''
        objetivo = self.valorX**2 + self.valorY**2

        return objetivo

    def p_best(self):
        '''devuelve el la mejor posicion en la que ese individuo ha estado a lo alrgo del tiempo'''

        if(self.pbest[2] > self.aptitud()):
            self.pbest = [self.valorX, self.valorY, self.aptitud()]
        elif(self.pbest[2] < self.aptitud()):
            self.pbest = self.pbest
        
        return self.pbest
    

    def actualizarPosicion(self, a, b1, b2, r1, r2, gbest):
        '''
        actualiza la posicion de la particula
        a:      inercia
        b1 :    factor de aprendizaje (influencia propia)
        b2 :    factor de aprendizaje (influencia social)
        r1, r2 :Valores aleatorios con uniform(0,1)
        gbest: mejor particula que la poblacion ha tenido
        '''
        nuevaVelocidad =[a*self.velocidad[0] + b1*r1*(self.p_best()[0] - self.valorX) + b2*r2*(gbest[0] - self.valorX),
                        a*self.velocidad[1] + b1*r1*(self.p_best()[1] - self.valorY) + b2*r2*(gbest[1]- self.valorY)]

        self.valorX = nuevaVelocidad[0]
        self.valorY = nuevaVelocidad[1]
        self.velocidad = nuevaVelocidad

    def mostrarParticula(self):
        print("individuo: ({},{})\taptitud:{}".format(self.valorX, self.valorY, self.aptitud()))



class poblacion:

    individuos = []

    def __init__(self, a, b1, b2, r1, r2):
        '''
        se inicializa con esos valores, porque son requeridos para las actualizaciones de la poblacion
        
        a:      inercia
        b1 :    factor de aprendizaje (influencia propia)
        b2 :    factor de aprendizaje (influencia social)
        r1, r2 :Valores aleatorios con uniform(0,1)
        '''

        self.a = a
        self.b1 = b1
        self.b2 = b2
        self.r1 = r1
        self.r2 = r2

    def verPoblacion(self):
        
        for individuo in self.individuos:
        
            print("individuo: ({},{})\taptitud:{}\tpbest ({},{})\taptitud: {}".format(individuo.valorX, individuo.valorY, individuo.aptitud(), individuo.p_best()[0], individuo.p_best()[1], individuo.p_best()[2]))
        
    def agregarIndividuos(self, particula):
        '''agrega particulas a la poblacion'''

        self.individuos.append(particula)

    def l_best(self):
        '''buscamos minimizar la funcion objetivo, asi que este metodo retorna la aptitud mejor entre la poblacion'''
        lbest = particula(10000) #<- lo inicializamos con un valor muy grande, ya que queremos minimizarlo, y eso se vera reflejado desde la primer iteracion

        for individuo in self.individuos:

            if(lbest.aptitud() > individuo.aptitud()):
                lbest = individuo
            elif(lbest.aptitud() < individuo.aptitud()):
                lbest = lbest
        
        return lbest
    
    def actualizarPoblacion(self, gbest):

        for individuo in self.individuos:
            individuo.actualizarPosicion(self.a, self.b1, self.b2, self.r1, self.r2, gbest)


def main():

    #definimos la funcion objetivo y el intervalo
    x = 0
    y = 0
    pbest = 0
    gbest = [1000,1000,2000000] #<- lo inicializamos con un valor muy grande, ya que queremos minimizarlo, y eso ocurrira desde la primer iteracio
    #intervao de -5 a 5
    objetivo = x**2 + y**2

    #definimos los parametros de ejecucion
    N = 20          #<- numero de particulas
    a = 0.8         #<- inercia
    b1 = 0.7        #<- factor de aprendizaje(influencia propia)
    b2 = 1          #<- factor de aprendizaje(influencia social)

    #definimos variables importantes

    miPoblacion = poblacion(a, b1, b2, random.uniform(0,1), random.uniform(0,1))  #<- contendra elementos de la clase particula
    iteraciones = 50

    #inicializacion aleatoria de posiciones actuales de las particulas
    for i in range(N):

        miPoblacion.agregarIndividuos(particula(random.uniform(-5, 5), random.uniform(-5, 5)))
    
    print("generacion 0\n")
    print(miPoblacion.verPoblacion())
    
    #evaluamos las funciones objetivo con las posiciones actuales de las particulas y asignamos los mejores valores a gbest

    if gbest[2] > miPoblacion.l_best().aptitud():
        gbest = [miPoblacion.l_best().valorX, miPoblacion.l_best().valorY, miPoblacion.l_best().aptitud()]
    elif gbest[2] < miPoblacion.l_best().aptitud():
        gbest = gbest


    print("lbest: ({}, {})\t aptitud: {}".format(miPoblacion.l_best().valorX, miPoblacion.l_best().valorY, miPoblacion.l_best().aptitud()))
    print("gbest: ({}, {})\t aptitud: {}\n\n".format(gbest[0], gbest[1], gbest[2]))

    for i in range(1, iteraciones):

        miPoblacion.actualizarPoblacion(gbest)

               
        if gbest[2] > miPoblacion.l_best().aptitud():
            gbest = [miPoblacion.l_best().valorX, miPoblacion.l_best().valorY, miPoblacion.l_best().aptitud()]
        elif gbest[2] < miPoblacion.l_best().aptitud():
            gbest = gbest

        print("generacion {}\n\n".format(i))

        print(miPoblacion.verPoblacion())

        print("lbest: ({}, {})\t aptitud: {}".format(miPoblacion.l_best().valorX, miPoblacion.l_best().valorY, miPoblacion.l_best().aptitud()))
        

        print("gbest: ({}, {})\t aptitud: {}\n\n".format(gbest[0], gbest[1], gbest[2]))

if __name__ == "__main__":
    main()