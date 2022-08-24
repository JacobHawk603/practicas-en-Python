import numpy as np

from asyncore import write


m = int(input("ingrese el valor de m: "))
#k = int(input("ingrese el valor de k: "))

cadena = '{e},{0,1},'
cadenaBin = ''
for i in range(m-1):
    cadena +='{'
    for j in range(2**(i+2)):
        cadenaBin = '' + bin(j)[2:]
        #print(bin(j)[2:])
        aux = '#0' + str(i+4) + 'b'
        cadena+= format(j, aux)[2:] + ','
    cadena+= '},'

print(cadena)
#txt = open('conjuntoPotencia.txt','w')
#txt.write(cadena)
