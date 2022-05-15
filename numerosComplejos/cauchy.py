from ast import Expression
from cv2 import sqrt
import numpy as np
from sympy import true
from librerias import mobiusLib
import sympy as sp
from sympy.abc import z, e
from sympy import sin, cosh
import math

puntos = np.zeros((2, 2), float)

switch = int(input('1. Forma general\n2. Forma Centro Radio\n'))

if (switch == 1):
    circ = mobiusLib.General()
    circ = mobiusLib.conversionGeneral2CentroRadio(circ)
elif (switch == 2):
    circ = mobiusLib.centroRadio()

str_z0 = input('inserte el numero complejo: (x+iy): ')
str_z0 = str_z0.replace(' ', '')
str_z0 = str_z0.replace('i', 'j')

z0 = complex(str_z0)

catalogoFunciones = int(input("1. cte\n2. z^n\n3. e^z\n4. sen(z)\n5.cosh(z)"))

if (catalogoFunciones == 1):
    str_fz = input('inserte el numero complejo: (x+iy): ')
    str_fz = str_z0.replace(' ', '')
    str_fz = str_z0.replace('i', 'j')

    fz = complex(str_fz)

    fzSymb = str_fz

elif(catalogoFunciones == 2):
    m = float(input('valor del exponente m: '))

    fz = z0**m

    fzSymb = z**m

elif(catalogoFunciones == 3):
    fz = np.e**z0

    fzSymb = e**z

elif(catalogoFunciones == 4):
    fz = np.sin(z0)

    fzSymb = sin(z)

elif(catalogoFunciones == 5):
    fz = np.cosh(z0)

    fzSymb = cosh(z)

n = int(input('inserte el exponente n: '))

def validar_z0(curva, z0):
    if((z0.real < (curva[0]+np.sqrt(curva[2]))) and (z0.real > (curva[0] - np.sqrt(curva[2]))) and (z0.imag < (curva[1]+np.sqrt(curva[2]))) and (z0.imag > (curva[1] - np.sqrt(curva[2]))) and (np.sqrt(((curva[0]-z0.real)**2 + (curva[1]-z0.imag)**2)) < np.sqrt(curva[2]))):
        return True
    else:
        return False


puntos[0] = [circ[0],z0.real]
puntos[1] = [circ[1], z0.imag]


mobiusLib.graficaCircunferenciaCentroRadio(circ, puntos)

if validar_z0(circ, z0):
    print('z0 existe dentro de la curva')
    integral = complex(2*np.pi*complex('j')*fz)
    print('La integral de Cauchy es: ',integral)

    derivadaSymb = sp.diff(fzSymb, z, n-1)
    print(derivadaSymb)

    derivada = derivadaSymb.subs([(e, np.e),(z, z0)])

    print(derivada)

    integralGeneralizada = complex((2*np.pi*complex('j')*derivada)/math.factorial(n-1))
    print('La integral de cauchy generalizada es: ',integralGeneralizada)

else:

    print('0 no existe dentro de la curva, el resultado de la integral es 0')