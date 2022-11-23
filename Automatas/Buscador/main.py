def estadoA(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoB(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'a'):
            bandera = estadoE(cadena, i+1, bandera)
        elif(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoC(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'i'):
            bandera = estadoJ(cadena, i+1, bandera)
        elif(cadena[i] == 'o'):
            bandera = estadoK(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoD(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'r'):
            bandera = estadoL(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoE(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'l'):
            bandera = estadoM(cadena, i+1, bandera)
        elif(cadena[i] == 'n'):
            bandera = estadoAF(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoG(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'n'):
            bandera = estadoAV(cadena, i+1, bandera)
        elif(cadena[i] == 'v'):
            bandera = estadoP(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera


def main():
        return 0

if __name__ == "__main__":
    main()