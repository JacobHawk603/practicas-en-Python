from symtable import Symbol
from tkinter import Y
from unittest.util import strclass
import matplotlib.pyplot as plt
import math
import numpy as np
from librerias import calculadoraLib
from sympy import solve, Symbol, Eq

strA = input("a: ") #<- Alfa
strB = input("b: ") #<- Beta
strD = input("d: ") #<- Deta
strR = input("r: ") #<- Gama

strA = strA.replace(" ", "")
strB = strB.replace(" ", "")
strD = strD.replace(" ", "")
strR = strR.replace(" ", "")

strA = strA.replace("i", "j")
strB = strB.replace("i", "j")
strD = strD.replace("i", "j")
strR = strR.replace("i", "j")

A = complex(strA)
B = complex(strB)
D = complex(strD)
R = complex(strR)

def General():
    fz = []
    fz.append(float(input("A(x2 + y2), valor de A: ")))
    fz.append(float(input("Bx valor, de B: ")))
    fz.append(float(input("Cy, valor de C: ")))
    fz.append(float(input("valor de D: ")))

    if -fz[3] + (fz[1]/(2*fz[0])) + (fz[2]/(2*fz[0])) < 0:
        print("No existe una circunferencia con radio menor a cero, asi que cambiaremos el signo de tu radio")
        fz[3] = -fz[3]
    return fz

def graficaRecta(fz):
    
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
        
    X, Y = np.meshgrid(x,y)
    print(fz[0], fz[1], fz[2], fz[3])
    F = fz[1]*X + fz[2]*Y + fz[3]
    #F = X**2 + Y**2 - 0.6
    plt.scatter(-fz[3]/fz[1],0)
    plt.scatter(0, -fz[3]/fz[2])

    plt.contour(X,Y,F,[0])
    plt.grid()
    plt.show()

def graficaCircunferenciaGeneral(fz):

    if fz[0] == 0:
        graficaRecta(fz)
        return
    else:
        x = np.linspace(-(-fz[3] + (fz[1]/(2*fz[0]))**2 + (fz[2]/(2*fz[0]))**2 + 5), (-fz[3] + (fz[1]/(2*fz[0]))**2 + (fz[2]/(2*fz[0]))**2 + 5), 100)
        y = np.linspace(-(-fz[3] + (fz[1]/(2*fz[0]))**2 + (fz[2]/(2*fz[0]))**2 + 5), (-fz[3] + (fz[1]/(2*fz[0]))**2 + (fz[2]/(2*fz[0]))**2 + 5), 100)
        
    X, Y = np.meshgrid(x,y)
    print(fz[0], fz[1], fz[2], fz[3])
    F = fz[0]*(X**2 + Y**2) + fz[1]*X + fz[2]*Y + fz[3]
    #F = X**2 + Y**2 - 0.6
    plt.scatter(-fz[1]/2, -fz[2]/2)
    plt.contour(X,Y,F,[0])
    plt.grid()
    plt.show()


def cartesiana():
    fz = []
    fz.append(float(input("(X-xi)2: valor de xi: ")))
    fz.append(float(input("(Y-yi)2: vaglor de yi: ")))
    fz.append(float(input("valor de r2: ")))

    if fz[2] < 0:
        print("No existe una circunferencia con radio menor a cero, asi que cambiaremos el signo de tu radio")
        fz[2] = -fz[2]
    return fz

def graficaCircunferenciaCartesiana(fz):
    x = np.linspace(-(math.sqrt(fz[2]) + 5), (math.sqrt(fz[2]) + 5), 100)
    y = np.linspace(-(math.sqrt(fz[2]) + 5), (math.sqrt(fz[2]) + 5), 100)
    X, Y = np.meshgrid(x,y)
    print(fz[0], fz[1], fz[2])
    F = (X - fz[0])**2 + (Y - fz[1])**2 - fz[2]
    #F = X**2 + Y**2 - 0.6
    plt.scatter(fz[0], fz[1])
    plt.contour(X,Y,F,[0])
    plt.grid()
    plt.show()

def conversionGeneral2Cartesiana(fz):
    gz =[]
    gz.append(pow(-fz[1]/2,2))
    gz.append(pow(-fz[2]/2,2))
    gz.append(-fz[3]+fz[1]+fz[2])
    return gz

def puntosNotables(fz):
    puntos = []
    puntos.append(complex(fz[0], fz[1]+fz[2]))
    puntos.append(complex(fz[0]-fz[2], fz[1]))
    puntos.append(complex(fz[0], fz[1]-fz[2]))
    return puntos

def puntosNotablesRecta(fz):
    puntos = []
    puntos.append(complex(-fz[3]/fz[1],0))
    puntos.append(complex(0, -fz[3]/fz[2]))
    puntos.append(complex((puntos[0].real+puntos[1].real)/2, (puntos[0].imag+puntos[1].imag)/2))
    print(puntos)
    return puntos


def transformacionMobius(puntos, A, B, D, R):
    transformaciones = []

    for i in range(0, 3):
        transformaciones.append(calculadoraLib.razonCompleja(calculadoraLib.sumaCompleja(calculadoraLib.productoComplejo(A, puntos[i]), B), calculadoraLib.sumaCompleja(calculadoraLib.productoComplejo(D, puntos[i]), R)))
    
    return transformaciones



def encontrarRadio(puntosMobius):
    x = Symbol('x')
    y = Symbol('y')
    r = Symbol('r')
    fz = (x-puntosMobius[0].real)**2 + (y-puntosMobius[0].imag)**2 - r**2
    gz = (x-puntosMobius[1].real)**2 + (y-puntosMobius[1].imag)**2 - r**2
    hz = (x-puntosMobius[2].real)**2 + (y-puntosMobius[2].imag)**2 - r**2

    datos = solve([fz, gz, hz], [x, y, r])
    print(datos[1][2])
    return datos[1]

switch = int(input("1: forma general\n\n2: forma cartesiana"))


if switch == 1:
    ecuacion = General()
    graficaCircunferenciaGeneral(ecuacion)

    if ((A==complex('j') and B==complex('j') and D==complex('1') and R==complex('1')) or (A==complex('1') and B==complex('1') and D==complex('1') and R==complex('1'))):
        plt.scatter(1,0)
        plt.grid()
        plt.show() 
    else:

        if ecuacion[0] != 0:
            ecuacion = conversionGeneral2Cartesiana(ecuacion)
            puntos = puntosNotables(ecuacion)
        else:
            puntos = puntosNotablesRecta(ecuacion)
        
        puntosMobius = transformacionMobius(puntos, A, B, D, R)
        ecuacionTransformada = encontrarRadio(puntosMobius)
        graficaCircunferenciaCartesiana(ecuacionTransformada)
elif switch == 2:
    ecuacion = cartesiana()
    graficaCircunferenciaCartesiana(ecuacion)

    if (A==complex('j') and B==complex('j') and D==complex('j') and R==complex('j') ):
        plt.scatter(1,0)
        plt.grid()
        plt.show() 
    else:
        puntos = puntosNotables(ecuacion)

        puntosMobius = transformacionMobius(puntos, A, B, D, R)
        ecuacionTransformada = encontrarRadio(puntosMobius)
        graficaCircunferenciaCartesiana(ecuacionTransformada)