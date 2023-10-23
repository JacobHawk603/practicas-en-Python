def valores_observados(valores_observados:list):

    '''Permite conocer todos los diferentes valroes que hay en una sola columna del dataset \n\n
        valores_obsetvados -> list: lista que contiene los valures de una columna específica del dataframe\n\n
        Retorna: lista con los diferentes valores observados en la columna estudidada
    '''

    valores = []

    for valor in valores_observados:
        en_valores = False

        if(len(valores) == 0):
            valores.append(valor)

        else:

            for i in range(len(valores)):

                if(valores[i] == valor):
                    en_valores = True
            
            if(not en_valores):
                valores.append(valor)

    return valores

def repeticiones_de_valor(valor, valores_observados:list):
    '''Permite conocer que tantas veces se repite un valor observado dentro de la columna\n\n
        Returna: int -> numero total de repeticiones
    '''

    contador = 0

    for elemento in valores_observados:
        if(valor == elemento):
            contador +=1
    
    return contador