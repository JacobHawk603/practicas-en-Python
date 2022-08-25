import matplotlib.pyplot as plt

primos = []
primosCad = []
m = int(input("inserte el numero maximo de primos: "))

def encontrarPrimo(primos, numero):
    bandera = True
    for i in range(len(primos)):
        if numero % primos[i] == 0:
            bandera = False
            break
    return bandera

def convertirACadena(primos):
    cadenaArr = []
    for i in range(len(primos)):
        cadenaArr.append(bin(primos[i])[2:])
    
    print(cadenaArr)
    return cadenaArr

i = 2
while(len(primos) < m):

    if encontrarPrimo(primos, i):
        primos.append(i)
        #print(primos)
    
    i+=1
print(primos)
primosCad = convertirACadena(primos)