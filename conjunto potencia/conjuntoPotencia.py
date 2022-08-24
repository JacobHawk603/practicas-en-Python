import numpy as mp

k = int(input("ingresa el valor de k"))
m = 1000

def inicializarCadena(len):
    car = '0'
    cadena = ''
    for i in range(len):
        cadena+=car

    return cadena

print(inicializarCadena(k))

def conjuntoPotencia(cadena, anterior):
    auxiliar = ''
    original = cadena
    if len(cadena) != 1 :
        #print(cadena[1:])
        auxiliar = conjuntoPotencia(cadena[1:], '')
    else:
        print(anterior + '0')
        cadena = '1'
        print(anterior + cadena)
        return cadena
    
    conjuntoPotencia(cadena[1:], anterior+cadena[0])

    cadena = '1' + cadena[1:]
    
    conjuntoPotencia(cadena[1:], anterior+cadena[0])
    '''print(cadena)
    cadena = cadena[0] + auxiliar
    print(cadena)
    cadena = '1' + original[1:]
    auxiliar = conjuntoPotencia(cadena[1:])'''

    '''print(cadena)
    cadena = cadena[0] + auxiliar
    print(cadena)'''
    #cadena = '1' + cadena[1:]
    return cadena

conjuntoPotencia(inicializarCadena(k), '')