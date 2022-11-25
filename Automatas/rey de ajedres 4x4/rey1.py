def estadoA(cadena, posicion):
    bandera = False
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoC(cadena, posicion+1, bandera)
        else:
            bandera = estadoB(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena1")
    
    return bandera

def estadoB(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoE(cadena, posicion+1, bandera)
        else:
            bandera = estadoD(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena2")
    
    return bandera

def estadoC(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoF(cadena, posicion+1, bandera)
        else:
            bandera = estadoD(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena3")
    
    return bandera

def estadoD(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoI(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena4")
    
    return bandera

def estadoE(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoI(cadena, posicion+1, bandera)
        else:
            bandera = estadoH(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena5")
    
    return bandera

def estadoF(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoG(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena6")
    
    return bandera

def estadoG(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoF(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("Felicidades, el rey ha llegado a la esquina opuesta")
        bandera = True
        return bandera
    
    return bandera

def estadoH(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoI(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena8")
    
    return bandera

def estadoI(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoK(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena9")
    
    return bandera

def estadoJ(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoK(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("el rey no llego a la esquina opuesta, prueba otra cadena10")
    
    return bandera

def estadoK(cadena, posicion, bandera):
    
    try:
        if(cadena[posicion] == '0'):
            bandera = estadoK(cadena, posicion+1, bandera)
        else:
            bandera = estadoJ(cadena, posicion+1, bandera)
    except:
        print("Felicidades, el rey ha llegado a la esquina opuesta")
        bandera = True
        return bandera

    return bandera

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
    cadenaPrueba = "00010"
    posicion = 0
    cadenas = []
    caminos = []
    
    caminosArchivo = open("./caminos1.txt", "w", encoding="utf8")

    cadenas = generadorCadenas()
    print(cadenas)

    for i in range(len(cadenas)):

        retorno = estadoA(cadenas[i], posicion)

        if retorno:
            caminos.append(cadenas[i])
            print("cadena aceptada: ", cadenas[i])
            caminosArchivo.write(str(cadenas[i]) + "\n")
        else:
            print("rechazada")



if __name__ == "__main__":
    main()