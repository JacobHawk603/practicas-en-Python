from threading import Thread

def estado1(cadena, posicion, camino):
    camino.append(1)

    #0 -> negro
    #1 -> rojo
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
        else:          
            Thread(target=estado2, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado5, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena1")
        print("el camino que siguio el rey es:\n\n", camino)

def estado2(cadena, posicion, camino):

    camino.append(2)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado1, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado3, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado5, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena2")
        print("el camino que siguio el rey es:\n\n", camino)


def estado3(cadena, posicion, camino):
    
    camino.append(3)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado8, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado2, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado4, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena3")
        print("el camino que siguio el rey es:\n\n", camino)

def estado4(cadena, posicion, camino):
    
    camino.append(4)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado3, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado8, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena4")
        print("el camino que siguio el rey es:\n\n", camino)


def estado5(cadena, posicion, camino):
    
    camino.append(5)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado1, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado9, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado2, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena5")
        print("el camino que siguio el rey es:\n\n", camino)


def estado6(cadena, posicion, camino):
    
    camino.append(6)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado1, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado9, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado3, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado2, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado5, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena6")
        print("el camino que siguio el rey es:\n\n", camino)

def estado7(cadena, posicion, camino):
    
    camino.append(7)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado3, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado8, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado2, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado4, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado12, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena7")
        print("el camino que siguio el rey es:\n\n", camino)

def estado8(cadena, posicion, camino):
    
    camino.append(8)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado3, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado4, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado12, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena8")
        print("el camino que siguio el rey es:\n\n", camino)

def estado9(cadena, posicion, camino):
    
    camino.append(9)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado14, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado5, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado13, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena9")
        print("el camino que siguio el rey es:\n\n", camino)

def estado10(cadena, posicion, camino):
    
    camino.append(10)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado9, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado14, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado5, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado13, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado15, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena10")
        print("el camino que siguio el rey es:\n\n", camino)

def estado11(cadena, posicion, camino):
    
    camino.append(11)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado6, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado8, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado14, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado16, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado12, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado15, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena11")
        print("el camino que siguio el rey es:\n\n", camino)

def estado12(cadena, posicion, camino):
    
    camino.append(12)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado8, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado16, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado7, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado15, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena12")
        print("el camino que siguio el rey es:\n\n", camino)

def estado13(cadena, posicion, camino):
    
    camino.append(13)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado9, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado14, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena13")
        print("el camino que siguio el rey es:\n\n", camino)

def estado14(cadena, posicion, camino):
    
    camino.append(14)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado9, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado13, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado15, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena14")
        print("el camino que siguio el rey es:\n\n", camino)

def estado15(cadena, posicion, camino):
    
    camino.append(15)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado14, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado16, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado10, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado12, args=(cadena, posicion+1, camino)).start()
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena15")
        print("el camino que siguio el rey es:\n\n", camino)

def estado16(cadena, posicion, camino):
    
    camino.append(16)
    try:
        if(cadena[posicion] == '0'):
            Thread(target=estado11, args=(cadena, posicion+1, camino)).start()
        else:
            Thread(target=estado12, args=(cadena, posicion+1, camino)).start()
            Thread(target=estado15, args=(cadena, posicion+1, camino)).start()
    except:
        print("El rey ha llegado a la esquina")
        print("el camino que siguio el rey es:\n\n", camino)

#Hasta aquí terminan los estados del autómata----------------------------------------------------------

#generamos las combinaciones tipo conjunto potencia para ir obteniendo caminos posibles para el rey
def generadorCadenas():
    m = int(input("ingrese el valor de m>2: "))
    #k = int(input("ingrese el valor de k: "))

    cadena = []
    
    for i in range(m-2):
        for j in range(2**(i+2)):
            
            #print(bin(j)[2:])
            aux = '#0' + str(i+4) + 'b'
            cadena.append(format(j, aux)[2:])
    
    print(cadena)
    return cadena

def main():
    cadenaPrueba = "000"
    posicion = 0
    cadenas = []
    caminos = []
    
    #caminosArchivo = open("./caminos1.txt", "w", encoding="utf8")

    #cadenas = generadorCadenas()
    #print(cadenas)


    Thread(target=estado1, args=(cadenaPrueba, posicion, caminos)).start()



if __name__ == "__main__":
    main()



# def cubo(valor):
#     valor+=1
#     return valor**3

# def main():
#     print(Pool().map(cubo, [2,3,5]))

