import numpy as np
import sympy as sp
from sympy.abc import z, e
from librerias import mobiusLib
import math

n = int(input("inserte el valor de n: "))
if(n < 0):
    print("valor invalido para n")
    exit()

m = int(input("inserte el valor de m: "))

if(m < 0):
    print("valor invalido para m")
    exit()


a = int(input("inserte el valor de a: "))
b = int(input("inserte el valor de b: "))
c = int(input("inserte el valor de c: "))

r = float(input("inserte el valor del radio r: "))

if(r < 0):
    print("valor invalido para r")
    exit()

gama = [0,0,r**2]


puntos = [[0,b,0],[a,0,-c]]

mobiusLib.graficaCircunferenciaCentroRadio(gama, puntos)

fzSymb = (z**n)/(((z-(a*complex('j')))**m)*(z-b)*((z+(c*complex('j')))**4))

def validarPunto(punto, radio):
    if(punto < radio):
        return True
    else:
        return False

def residuo(fzSymb, z0, m):
    res = (1/math.factorial(m-1))*sp.diff((((z-z0)**m) * fzSymb), z, m-1)
    
    print("el residuo parcial simbolico: ", res)
    print("el residuo parcial: ", complex(res.subs(z,z0)))
    return complex(res.subs(z,z0))

residuos = complex('0+0j')

if(validarPunto(abs(a), r)):
    residuos += residuo(fzSymb, a*complex('j'), m)
if(validarPunto(abs(b), r)):
    residuos += residuo(fzSymb, b, 1)
if(validarPunto(abs(c), r)):
    residuos += residuo(fzSymb, -c*complex('j'), 4)

integral = 2*math.pi * complex('j') * residuos

print("el rseultado de la integral ",fzSymb, "es: ", integral)