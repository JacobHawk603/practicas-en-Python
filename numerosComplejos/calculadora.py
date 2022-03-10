from cmath import cos
import math
from re import I
import matplotlib.pyplot as plt


strz1 = input("z1: ")
strz2 = input("z2: ")
n= input("n: ")
m= input("m: ")

strz1 = strz1.replace(" ", "")
strz1 = strz1.replace("i", "j")

strz2 = strz2.replace(" ", "")
strz2 = strz2.replace("i", "j")

print(type(strz1))
print(strz1)
print(type(n))

z1 = complex(strz1)
z2 = complex(strz2)
n = int(n)
m = int(m)

print(type(z1))

def sumaCompleja(z1, z2):
    real = z1.real + z2.real
    im = z1.imag + z2.imag
    suma = complex(real, im)
    #grafica de la suma de numeros complejos

    x = [z1.real, z2.real, suma.real]
    y = [z1.imag, z2.imag, suma.imag]

    return suma


def productoComplejo(z1, z2):
    real1 = z1.real * z2.real
    real2 = -(z1.imag * z2.imag)
    im1 = z1.real * z2.imag
    im2 = z1.imag * z2.real
    real = real1 + real2
    im = im1 + im2
    producto = complex(real, im)

    return producto

def razonCompleja(z1, z2):
    real = ((z1.real * z2.real) + (z1.imag * z2.imag))/((z2.real * z2.real) + (z2.imag * z2.imag))
    im = ((z2.real * z1.imag) - (z1.real * z2.imag))/((z2.real * z2.real) + (z2.imag * z2.imag))
    razon = complex(real, im)

    return razon

def potenciaCompleja(z1, n):
    real=0
    im=0

    for m in range(0, n+1):
        if m%4 == 0:
            real += math.comb(n, m) * pow(z1.real, (n-m)) * pow(z1.imag, m)
        elif m%4 ==1:
            im += math.comb(n, m) * pow(z1.real, (n-m)) * pow(z1.imag, m)
        elif m%4 ==2:
            real -= math.comb(n, m) * pow(z1.real, (n-m)) * pow(z1.imag, m)
        else:
            im -= math.comb(n, m) * pow(z1.real, (n-m)) * pow(z1.imag, m)
    
    potencia = complex(real, im)

    return potencia

def raizCompleja(z1, n):
    raices = []
    real = 0
    im = 0

    moduloZ = pow(pow(z1.real, 2) + pow(z1.imag, 2), 1/2)
    argZ = math.atan(z1.imag/z1.real)

    if argZ<0:
        argZ += math.pi

    for i in range (0, n):
        real = pow(moduloZ, 1/n)*(math.cos((argZ + 2*math.pi * i)/n))
        im = pow(moduloZ, 1/n)*(math.sin((argZ + 2*math.pi * i)/n))
        raices.append(complex(real, im))
        print("La ", i, " raiz de: ", z1, ": ", raices[i])

    return raices

raizCompleja(z2, m)

def exponencialCompleja(z1):
    exponencial = complex (pow(math.e, z1.real)*math.cos(z1.imag), pow(math.e, z1.real)*math.sin(z1.imag))

    return exponencial

def senoComplejo(z1):
    real = math.sin(z1.real)*math.cosh(z1.imag)
    im = math.cos(z1.real)*math.sinh(z1.imag)
    seno = complex(real, im)

    return seno

def cosenoComplejo(z1):
    real = math.cos(z1.real)*math.cosh(z1.imag)
    im = -(math.sin(z1.real)*math.sinh(z1.imag))
    coseno = complex(real, im)

    return coseno

def tangenteCompleja(z1):
    tangente = senoComplejo(z1)/cosenoComplejo(z1)

    return tangente

#-------------------------------------------------------------------------------------------------------------------------------------

def grafSumaCompleja(z1, z2):

    x = [z1.real, z2.real, sumaCompleja(z1, z2).real]
    y = [z1.imag, z2.imag, sumaCompleja(z1, z2).imag]

    titulo = 'suma de los numeros z1 =', z1, ' y  z2= ', z2

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1



def grafProductoComplejo(z1, z2):

    #grafica del producto de numeros complejos

    x = [z1.real, z2.real, productoComplejo(z1,z2).real]
    y = [z1.imag, z2.imag, productoComplejo(z1,z2).imag]

    titulo = 'producto de los numeros z1 =', z1, ' y  z2= ', z2

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1



def grafRazonCompleja(z1, z2):

    #grafica de la razón de numeros complejos 1

    x = [z1.real, z2.real, razonCompleja(z1, z2).real]
    y = [z1.imag, z2.imag, razonCompleja(z1, z2).imag]

    titulo = 'razon de los numeros z1 =', z1, ' y  z2= ', z2, 'respectivamente'

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1



def grafPotenciaCompleja(z1, n):

    x = [z1.real, z2.real, potenciaCompleja(z1,n).real]
    y = [z1.imag, z2.imag, potenciaCompleja(z1,n).imag]

    titulo = 'potencia ', n, ' de  z1= ', z1

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1



def grafRaizCompleja(z1, n):

    #Grafica de raíces complejas de z1
    x = [z.real for z in raizCompleja(z1, n)]
    y = [z.imag for z in raizCompleja(z1, n)]

    titulo = n, ' raíces complejas de z1= ', z1

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()
    return 1



def grafExponencialCompleja(z1):
    
    #grafica de la exponencial de z1

    x = [z1.real, exponencialCompleja(z1).real]
    y = [z1.imag, exponencialCompleja(z1).imag]

    titulo = 'exponencial de z1= ', z1

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()

    return 1



def grafSenoComplejo(z1):

    #grafica del seno de z1

    x = [z1.real, senoComplejo(z1).real]
    y = [z1.imag, senoComplejo(z1).imag]

    titulo = 'seno de z1: ', z1

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1



def grafCosenoComplejo(z1):

    #grafica del seno de z1

    x = [z1.real, cosenoComplejo(z1).real]
    y = [z1.imag, cosenoComplejo(z1).imag]

    titulo = 'coseno de z1: ', z1

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1



def grafTangenteCompleja(z1):

    #grafica de la tangente de z1+z2

    x = [z1.real, tangenteCompleja(z1).real]
    y = [z1.imag, tangenteCompleja(z1).imag]

    titulo = 'tangente de z1: ', z1

    plt.scatter(x, y)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return 1

print("La suma de ", z1, " y ", z2, " es: ", sumaCompleja(z1, z2))
grafSumaCompleja(z1, z2)

print("el producto de ", z1, " y ", z2, " es: ", productoComplejo(z1, z2))
grafProductoComplejo(z1,z2)

print("La razon de ", z1, " y ", z2, " es: ", razonCompleja(z1, z2))
grafRazonCompleja(z1, z2)

print(z1, "elevado a la ", n, " es: ",potenciaCompleja(z1, n))
grafPotenciaCompleja(z1, n)

raizCompleja(z2, m)
grafRaizCompleja(z2, m)

print("e elevado a la ", z1, " es: ",exponencialCompleja(z1))
grafExponencialCompleja(z1)

print("el seno de ", z1, " es. ",senoComplejo(z1))
grafSenoComplejo(z1)

print("el coseno de ", z2, " es: ",cosenoComplejo(z2))
grafCosenoComplejo(z2)

print("La tangente de ", z1, " + ", z2, "es igual a: ",tangenteCompleja(sumaCompleja(z1, z2)))
grafTangenteCompleja(sumaCompleja(z1, z2))