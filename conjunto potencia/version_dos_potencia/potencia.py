import numpy as np

from asyncore import write

token = open("version_dos_potencia/token.txt", "r").read()

if len(token) == 0:
    token = open("version_dos_potencia/token.txt", "w")
    token.write('0')
    token.close()
    token = open("version_dos_potencia/token.txt", "r").read()

print(token)
k = int(token)
#token.close()
m = int(input("ingrese el valor de m: "))
#k = int(input("ingrese el valor de k: "))

if k == 0:
    cadena = '{e},{0,1},'
else:
    cadena = ""
cadenaBin = ''
for i in range(k, m-1):
    cadena +='{'
    for j in range(2**(i+2)):
        cadenaBin = '' + bin(j)[2:]
        #print(bin(j)[2:])
        aux = '#0' + str(i+4) + 'b'
        cadena+= format(j, aux)[2:] + ','
    cadena+= '},'

#print(cadena)
token = token = open("version_dos_potencia/token.txt", "w")
token.write(str(m-1))
token.close()
txt = open("version_dos_potencia/conjuntoPotencia.txt",'a')
txt.write(cadena)
txt.close()
