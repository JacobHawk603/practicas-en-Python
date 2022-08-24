#import numpy as np

from asyncore import write


m = int(input("ingrese el valor de m: "))
#k = int(input("ingrese el valor de k: "))

cadena = '{e},{0,1},'
cadenaBin = ''
for i in range(m):
    cadena +='{'
    for j in range(2**(i+2)):
        cadenaBin = '' + bin(j)[2:]
        for k in range(2**(i)-len(cadenaBin)):
            cadena+='0'
        #print(bin(j)[2:])
        cadena+= bin(j)[2:] + ','
    cadena+= '},'

print(cadena)
#txt = open('conjuntoPotencia.txt','w')
#txt.write(cadena)
        