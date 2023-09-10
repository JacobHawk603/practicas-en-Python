import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

class Marco():

    def __init__(self, externo, interno):
        self.lim_externo = externo
        self.lim_interno = interno

        self.grueso_izquierdo = self.lim_interno.get_x() - self.lim_externo.get_x()
        self.grueso_derecho = (self.lim_externo.get_x() + self.lim_externo.get_width()) - (self.lim_interno.get_x() + self.lim_interno.get_width())
        self.grueso_superior = (self.lim_externo.get_y() + self.lim_externo.get_height()) - (self.lim_interno.get_y() + self.lim_interno.get_height())
        self.grueso_inferior = self.lim_interno.get_y() - self.lim_externo.get_y()

class Punto():
    perteneceAlMarco = False
    fuera_marco=False
    dentro_marco=False

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def compararPertenencia(self, marco):
        
        if((self.x_coord < marco.lim_externo.get_x()  or (self.x_coord > marco.lim_externo.get_x() + marco.lim_externo.get_width())) or (self.y_coord < marco.lim_externo.get_y()  or (self.y_coord > marco.lim_externo.get_y() + marco.lim_externo.get_height()))):
            self.fuera_marco = True

        elif(marco.lim_externo.get_y() <= self.y_coord and self.y_coord <= (marco.lim_externo.get_y() + marco.lim_externo.get_height())):

            # Verificando si el pounto se encuentra en la parte izquierda del marco
            if((abs(marco.lim_interno.get_x() - self.x_coord) <= marco.grueso_izquierdo) and (abs(marco.lim_externo.get_x() - self.x_coord) <= marco.grueso_izquierdo)):
                self.perteneceAlMarco = True
                print("un punto esta en el area iquierzda")

            #verificando si el punto se encuentra en el area derecha del marco
            elif((abs(marco.lim_interno.get_x() + marco.lim_interno.get_width() - self.x_coord) <= marco.grueso_derecho) and (abs(marco.lim_externo.get_x() + marco.lim_externo.get_width() - self.x_coord) <= marco.grueso_derecho)):
                self.perteneceAlMarco = True
                print("un punto esta en el area derecha")

            elif(marco.lim_externo.get_x() <= self.x_coord and self.x_coord <= (marco.lim_externo.get_x() + marco.lim_externo.get_width())):

                # Verificando si el pounto se encuentra en la parte inferior del marco
                if((abs(marco.lim_interno.get_y() - self.y_coord) <= marco.grueso_inferior) and (abs(marco.lim_externo.get_y() - self.y_coord) <= marco.grueso_inferior)):
                    self.perteneceAlMarco = True
                    print("un punto esta en el area inferior")

                #verificando si el punto se encuentra en el area superior del marco
                elif((abs(marco.lim_interno.get_y() + marco.lim_interno.get_height() - self.y_coord) <= marco.grueso_superior) and (abs(marco.lim_externo.get_y() + marco.lim_externo.get_height() - self.y_coord) <= marco.grueso_superior)):
                    self.perteneceAlMarco = True
                    print("un punto esta en el area superior")

                else:
                    self.dentro_marco=True
            
            else:
                self.dentro_marco=True

        return 0

def crearMarco(axis):
    x = np.random.randint(3, 7)
    y = np.random.randint(5, 9)

    #incremento de las variables x, y para el marco interior
    m = np.random.randint(1, 3)
    n = np.random.randint(1, 3)

    width = np.random.randint(7, 20)
    height = np.random.randint(9, 20)

    # decremento en la base y altura del rectangulo
    d_width = np.random.randint(1, 10)
    d_height = np.random.randint(1, 10)

    rectanguloexterno = Rectangle((x,y), width, height, fill=False)
    rectanguloInterno = Rectangle((x+m,y+n), abs(width-m-d_width), abs(height-n-d_height), fill=False)

    #definimos el marco en una variable para tenerla siempre con nosotros
    marco = Marco(rectanguloexterno,rectanguloInterno)

    axis.add_patch(marco.lim_externo)
    axis.add_patch(marco.lim_interno)

    print("({},{})\n{}\n{}".format(x, y, m, n))

    return marco

def crearRectanguloDeHipotesis(puntos):
    
    min_x_ext_izq = 100000
    max_y_ext_izq = 0

    max_x_ext_der = 0
    min_y_ext_der = 100000

    for punto in puntos:

        #obteniendo el extremo superior izquierdo
        if(punto.x_coord < min_x_ext_izq):
            min_x_ext_izq = punto.x_coord

        if(punto.y_coord > max_y_ext_izq):
            max_y_ext_izq = punto.y_coord
        
        #obteniendo el extremo inferior derecho

        if(punto.x_coord > max_x_ext_der):
            max_x_ext_der = punto.x_coord

        if(punto.y_coord < min_y_ext_der):
            min_y_ext_der = punto.y_coord

    return min_x_ext_izq, max_x_ext_der, min_y_ext_der, max_y_ext_izq

def crearHipotesis(puntosSobreMarco, puntosDentro, axis):
    
    #sacamos el limite externo del marco
    
    x1, x2, y1, y2 = crearRectanguloDeHipotesis(puntosSobreMarco)

    lim_externo = Rectangle((x1,y1), width=(x2-x1), height=(y2-y1), fill=False)

    #sacamos el limite interno del marco

    x3, x4, y3, y4 = crearRectanguloDeHipotesis(puntosDentro)

    lim_interno = Rectangle((x3,y3), width=(x4-x3), height=(y4-y3), fill=False)

    #construimos el marco hipotetico

    hipotesis = Marco(lim_externo, lim_interno)

    #dibujamos el marco

    axis.add_patch(hipotesis.lim_externo)
    axis.add_patch(hipotesis.lim_interno)

    return hipotesis

def inicializarPuntos():

    puntos = []

    for i in range(tamano_espacio):
        x = np.random.randint(0, tamano_espacio)
        y = np.random.randint(0, tamano_espacio)

        nuevoPunto = Punto(x, y)

        puntos.append(nuevoPunto)

    # print("el punto en x: ",puntos[0].x_coord)
    return puntos

def main():

    regenerar = True

    #creamos los arreglos de los puntos en el lienzo
    puntosSobreMarco = []
    puntosFuera = []
    puntosDentro= []

    #vamos a comenzar creando el lienzo

    figure, axis = plt.subplots()
    axis.set_xlim(0,tamano_espacio)
    axis.set_ylim(0,tamano_espacio)
    axis.plot()
    
    while(regenerar):

        #creamos el marco

        marco = crearMarco(axis)

        print("grueso Izquiero: ({})\n grueso Derecho: ({})\n grueso superior: ({})\n grueso inferior: ({})".format(marco.grueso_izquierdo, marco.grueso_derecho, marco.grueso_superior, marco.grueso_inferior))
        #inicializamos los puntos
        puntos = inicializarPuntos()

        for punto in puntos:
            punto.compararPertenencia(marco)
            
            if(punto.perteneceAlMarco):
                puntosSobreMarco.append(punto)
                axis.plot(punto.x_coord, punto.y_coord, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
            elif(punto.fuera_marco):
                puntosFuera.append(punto)
                axis.plot(punto.x_coord, punto.y_coord, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")
            elif(punto.dentro_marco):
                puntosDentro.append(punto)
                axis.plot(punto.x_coord, punto.y_coord, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="blue")

        if((len(puntosSobreMarco) < 4) or (len(puntosDentro) < 4) or (len(puntosFuera) < 4)):
            axis.clear()
            puntosFuera.clear()
            puntosDentro.clear()
            puntosSobreMarco.clear()
            regenerar=True
        else:
            regenerar=False

    plt.show()

    #creamos la segunda grafica

    figure, axis = plt.subplots()
    axis.set_xlim(0,tamano_espacio)
    axis.set_ylim(0,tamano_espacio)
    axis.plot()

    for punto in puntos:
        punto.compararPertenencia(marco)
        
        if(punto.perteneceAlMarco):
            axis.plot(punto.x_coord, punto.y_coord, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
        else:
            axis.plot(punto.x_coord, punto.y_coord, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")

    hipotesis = crearHipotesis(puntosSobreMarco, puntosDentro, axis)

    #axis2 = figure.add_subplot(1,2,1)

    plt.show()

    return 0

if __name__ == "__main__":

    tamano_espacio = 30
    main()