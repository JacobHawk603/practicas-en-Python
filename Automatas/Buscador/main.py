#definimos un arreglo global con todos los contadores 
#[covid, gripa, contagio, distancia, calentura, cansancio, cubrebocas, dolor]
contadores = [0,0,0,0,0,0,0,0]

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
        elif(cadena[i] == 'o'):
            bandera = estadoG(cadena, i+1, bandera)
        elif(cadena[i] == 'u'):
            bandera = estadoH(cadena, i+1, bandera)
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
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoU(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'e'):
            bandera = estadoAA(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoV(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoAB(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoW(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAC(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoX(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'r'):
            bandera = estadoAD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoY(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAE(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoZ(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 't'):
            bandera = estadoAG(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAA(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'b'):
            bandera = estadoAH(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAB(cadena, i, bandera):
    bandera = True
    contadores[0]+=1
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

def estadoAC(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'n'):
            bandera = estadoAM(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAD(cadena, i, bandera):
    bandera = True
    contadores[7]+=1
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

def estadoAE(cadena, i, bandera):
    bandera = True
    contadores[1]+=1
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

def estadoAF(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 's'):
            bandera = estadoAJ(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAG(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'u'):
            bandera = estadoAK(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAH(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'o'):
            bandera = estadoAL(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAJ(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAN(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAK(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'r'):
            bandera = estadoAO(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAL(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoAP(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAM(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoAQ(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAN(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'n'):
            bandera = estadoAR(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAO(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAS(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAP(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAT(cadena, i+1, bandera)
        elif(cadena[i] == 'o'):
            bandera = estadoG(cadena, i+1, bandera)
        elif(cadena[i] == 'u'):
            bandera = estadoH(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAQ(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoE(cadena, i+1, bandera)
        elif(cadena[i] == 'i'):
            bandera = estadoAU(cadena, i+1, bandera)
        elif(cadena[i] == 'o'):
            bandera = estadoG(cadena, i+1, bandera)
        elif(cadena[i] == 'u'):
            bandera = estadoH(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAR(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoBD(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAS(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAS(cadena, i, bandera):
    bandera = True
    contadores[4]+=1
    try:
        if(cadena[i] == 'c'):
            bandera = estadoBD(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAT(cadena, i, bandera):
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
        elif(cadena[i] == 's'):
            bandera = estadoAX(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAU(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoAY(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAV(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 't'):
            bandera = estadoAZ(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAW(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoBD(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoAX(cadena, i, bandera):
    bandera = True
    contadores[6] += 1
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

def estadoAY(cadena, i, bandera):
    bandera = True
    contadores[3] += 1
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

def estadoAZ(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoD(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoBA(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoBA(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoBB(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoBB(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoBB(cadena, i+1, bandera)
        elif(cadena[i] == 'i'):
            bandera = estadoBC(cadena, i+1, bandera, 0)
        elif(cadena[i] == 'r'):
            bandera = estadoL(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoBC(cadena, i, bandera, camino):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoBB(cadena, i+1, bandera)
        elif(cadena[i] == 'o'):
            bandera = estadoBE(cadena, i+1, bandera, camino)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoBD(cadena, i, bandera):
    bandera = False
    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoBB(cadena, i+1, bandera)
        elif(cadena[i] == 'a'):
            bandera = estadoE(cadena, i+1, bandera)
        elif(cadena[i] == 'i'):
            bandera = estadoBC(cadena, i+1, bandera, 1)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def estadoBE(cadena, i, bandera, camino):
    bandera = True

    if(camino == 0):
        contadores[2] +=1
    else:
        contadores[5] +=1

    try:
        if(cadena[i] == 'c'):
            bandera = estadoB(cadena, i+1, bandera)
        elif(cadena[i] == 'd'):
            bandera = estadoC(cadena, i+1, bandera)
        elif(cadena[i] == 'g'):
            bandera = estadoBB(cadena, i+1, bandera)
        else:
            bandera = estadoA(cadena, i+1, bandera)
    except:
        return bandera
    
    return bandera

def main():
    cadena = "covid" #<- cualquier cadena de la que se desee encontrar las palabras del automata
    bandera = estadoA(cadena,0, False)
    print(bandera, contadores)    
    return 0

if __name__ == "__main__":
    main()