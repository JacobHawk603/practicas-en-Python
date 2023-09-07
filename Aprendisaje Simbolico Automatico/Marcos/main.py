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
    pertenece = False

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def compararPertenencia(self, marco):
        
        dentroDeAreaIzquierda = False
        dentroDeAreaDerecha = False
        dentroDeAreaCentralX = False
        dentroDeAreaSuperior = False
        dentroDeAreaInferior = False
        dentroDeAreaCentralY = False

        if((abs(marco.lim_interno.get_x() - self.x_coord) < marco.grueso_izquierdo) and (abs(marco.lim_externo.get_x - self.x_coord) < marco.grueso_derecho)):
            dentroDeAreaDerecha = True

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

def inicializarPuntos(axis):

    puntos = []

    for i in range(tamano_espacio):
        x = np.random.randint(0, tamano_espacio)
        y = np.random.randint(0, tamano_espacio)

        nuevoPunto = Punto(x, y)

        puntos.append(nuevoPunto)

        axis.plot(nuevoPunto.x_coord, nuevoPunto.y_coord, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")

    # print("el punto en x: ",puntos[0].x_coord)
    return puntos

def main():
    #vamos a comenzar creando el lienzo

    figure, axis = plt.subplots()
    axis.set_xlim(0,tamano_espacio)
    axis.set_ylim(0,tamano_espacio)
    axis.plot()

    #creamos el marco

    marco = crearMarco(axis)

    print("grueso Izquiero: ({})\n grueso Derecho: ({})\n grueso superior: ({})\n grueso inferior: ({})".format(marco.grueso_izquierdo, marco.grueso_derecho, marco.grueso_superior, marco.grueso_inferior))
    #inicializamos los puntos
    puntos = inicializarPuntos(axis)
    plt.show()
    return 0

if __name__ == "__main__":

    tamano_espacio = 30
    main()