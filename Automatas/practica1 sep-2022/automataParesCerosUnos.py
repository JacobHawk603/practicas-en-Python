from random import randint

cadena = "000101010010"
bandera = False

def estado0(entrada, contador):#Si retorna True, La cadena que se ha inspeccionado cuenta con una cantidad par tanto de ceros como de unos
    #print("estado0")
    #print(contador)
    global bandera
    if contador < len(entrada):
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado1(entrada, contador)
        else:
            contador+=1
            estado2(entrada, contador)
        
    else:
        bandera = True
    
    return bandera
    
        
def estado1(entrada, contador):
    #print("estado1")
    if contador < len(entrada):
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado0(entrada, contador)
        else:
            contador+=1
            estado3(entrada, contador)

def estado2(entrada, contador):
    #print("estado2")
    if contador < len(entrada):
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado3(entrada, contador)
        else:
            contador+=1
            estado0(entrada, contador)

def estado3(entrada, contador):
    #print("estado3")
    if contador < len(entrada):
        #print(entrada[contador])
        if entrada[contador] == '1':
            contador+=1
            estado2(entrada, contador)
        else:
            contador+=1
            estado1(entrada, contador)


'''def main():
    estado0(cadena, 0)
    print(len(cadena))
    #print(contador)
    print(bandera)
    

if __name__ == "__main__":
    main()'''