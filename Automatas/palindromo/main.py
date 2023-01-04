from random import randint

def reglas(regla):

    if regla == 1:
        return "\0"
    elif regla == 2:
        return "0"
    elif regla == 3:
        return "1"
    elif regla == 4:
        return "0p0"
    else:
        return "1p1"

def palindromo(contador):
    cadena = ""
    global longitud
    global archivo

    for i in range (contador+1):
        
        if i >0:
            index = cadena.index("p")
        
        if i ==0:
            archivo.write("(0)\t\t\t\tp\n")
            cadena = "p"
        
        elif i < contador:

            #print("esta es la p: ", type(cadena[index]))
            regla = randint(4,5)
            cadena = cadena.replace(cadena[index], reglas(regla))

            archivo.write("({})\tregla: {}\t {}\n".format(str(i), str(regla), cadena))
            print(cadena)
        
        elif i == contador:
            
            print(len(cadena))

            if len(cadena) > longitud:
            
                cadena = cadena.replace(cadena[index], reglas(1))

                archivo.write("({})\tregla: {}\t {}\n".format(str(i), "1", cadena))
            else:

                regla = randint(2,3)
                cadena = cadena.replace(cadena[index], reglas(regla))
                archivo.write("({})\tregla: {}\t {}\n".format(str(i), str(regla), cadena))
    
    return cadena



if __name__ == "__main__":
    longitud = input("longitud del palindromo: ")
    longitud = int(longitud)

    archivo = open("./palindromo.txt", 'w')

    if longitud%2 == 0:
        operaciones = (longitud+2)/2

    else:
        operaciones = (longitud+1)/2
    
    print("el palindromo es: ", palindromo(int(operaciones)))

    