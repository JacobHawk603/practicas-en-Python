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

def estadoH(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'b'):
            bandera[i] = estadoO(cadena, i+1, bandera)
        elif(cadena[i] == 'c'):
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

def estadoJ(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 's'):
            bandera = estadoQ(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoK(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'l'):
            bandera = estadoR(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoL(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'i'):
            bandera = estadoS(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoM(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'e'):
            bandera = estadoT(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoN(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'l'):
            bandera = estadoR(cadena, i+1, bandera)
        elif(cadena[i] == 'v'):
            bandera = estadoP(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoO(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'r'):
            bandera = estadoU(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoP(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'i'):
            bandera = estadoV(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoQ(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 't'):
            bandera = estadoW(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoR(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'o'):
            bandera = estadoX(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoS(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'p'):
            bandera = estadoY(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoT(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'n'):
            bandera = estadoZ(cadena, i+1, bandera)
        else:
            bandera = estado(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera


def main():
        return 0

if __name__ == "__main__":
    main()