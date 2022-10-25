from random import randint

cadena = "000110000011110101"
bandera = False

def estado0(entrada, contador):#Si retorna True, La cadena que se ha inspeccionado cuenta con una cantidad par tanto de ceros como de unos
    #print("estado0")
    #print(contador)
    global bandera

    try:
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado1(entrada, contador)
        else:
            contador+=1
            estado2(entrada, contador) 
    except:

        bandera = True
        return bandera    
        
def estado1(entrada, contador):

    try:
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado0(entrada, contador)
        else:
            contador+=1
            estado3(entrada, contador)
    except:
        bandera = False
        return bandera

def estado2(entrada, contador):
    
    try:
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado3(entrada, contador)
        else:
            contador+=1
            estado0(entrada, contador)
    except:
        bandera = False
        return bandera

def estado3(entrada, contador):
    
    try:
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado2(entrada, contador)
        else:
            contador+=1
            estado1(entrada, contador)
    except:
        bandera = False
        return bandera


'''def main():
    estado0(cadena, 0)
    print(len(cadena))
    #print(contador)
    print(bandera)
    

if __name__ == "__main__":
    main()'''