from asyncore import write
from pickle import FALSE, TRUE
from pprint import pprint
from random import randint
import automataParesCerosUnos as filtroPares
import turtle


def generadorDeCadenas64Bits(cantidad):
    cadenas = ""
    for i in range(cantidad):
        cadena = ""
        for i in range(0,64):
            cadena += str(randint(0,1000000)%2)
        
        cadenas += cadena + ","
    return cadenas

#Autómata principal

def readyState(bandera):
    if bandera == 1:
        print("conexión exitosa")
        print("generando archivo")

        cadena = generadorDeCadenas64Bits(1000000)

        archivo = open("src/original.txt", "a")
        archivo.write(cadena)
        archivo.close()
        print("archivo generado exitosamente")
        
        print("enviando archivo")
        
        #las lineas comentadas a continuación son una solución idealizada, en la que mandamos archivos al servidor simulado
        #no obstante, al mandar el archivo "original.txt" con los mismos elementos que ya había evaluado anteriormente se produce reundancia
        #y un errror logico donde en los archivos "pares.txt" y "impares.txt" escribe nuevamente los elementos que ya contenía y agrega los nuevos
        #Por cuestiones de optimización, decidí no enviar al siguiente estado del automata el archivo "original.txt"
        #en vez de eso, enviamos los elementos generados aleatoriamente para que unicamente evalúe los nuevos elementos
        #existen otras soluciones como la creacion de un archivo "token.txt" para crear un contador que lleve el conteo de los elementos ya evaluados
        #Pero altería la idea de tener tres archivos, ñadiendo un cuarto archivo, por lo que he descartado esta idea, pero no está demas comentarla.
        
        
        #archivo = open("src/original.txt", "r")
        sendingState(cadena) # <- Madamos una cadena de palabras de 64 bits separadas por comas, en vez del archivo completo
        return True
    else:
        return False
        exit()

def sendingState(archivo):
    #realicemos primero la funcionalidad, posteriomente revisaremos el timeOut
    pares = ""
    impares = ""

    #cadenas = archivo.read().split(",")
    cadenas = archivo.split(',') # <- al no ser un archivo, sino una cadena, solo necesitamos convertir los datos a arreglo, ya no leeer el archivo primero
    cadenas.pop()
    #print(cadenas)
    for element in cadenas:
        if filtroPares.estado0(element, 0):
            pares += element + ","
        else:
            impares += element + ","
    
    archivoPares = open("src/pares.txt", "a")
    archivoImpares = open("src/impares.txt", "a")

    archivoPares.write(pares)
    archivoImpares.write(impares)
    return 1

def GraficarAutomata():
    #coordenadas de mi tortuga
    x = 0
    y = 0

    ventana = turtle.Screen()
    ventana.bgcolor("light blue")
    ventana.title("protocolo")

    tortuga = turtle.Turtle()
    tortuga.penup()

    x = -250
    y = 80

    tortuga.setx(x)
    tortuga.pendown()
    tortuga.circle(80)
    tortuga.penup()

    x -= 50

    tortuga.goto(x,y)
    tortuga.write("ReadyState", font=("Arial", 18, "normal"))

    x +=130

    tortuga.goto(x, y)
    #tortuga.penup()
    tortuga.pendown()
    tortuga.forward(317)


    tortuga.fillcolor(0,0,0)
    tortuga.begin_fill()
    tortuga.circle(3)
    tortuga.end_fill()

    tortuga.forward(3)

    x+=400
    y=0

    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.circle(80)
    tortuga.penup()

    x -=50
    y=50

    tortuga.goto(x,y)
    tortuga.write("Sending\nState", font=("Arial", 18, "normal"))

    x +=130
    y = 80

    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.circle(80, 270)

    tortuga.begin_fill()
    tortuga.circle(3)
    tortuga.end_fill()

    x = -250
    y = 0

    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()

    tortuga.begin_fill()
    tortuga.circle(3)
    tortuga.end_fill()

    tortuga.circle(250, 180)
    tortuga.penup()

    tortuga.goto(0,0)

    turtle.done()

def main():

    #No te olvides de descomentar esta parte para que funcione correctamenete el programa
    '''while(readyState(randint(0,1))):
        print("Protocolo completado")'''

    #a partir de este punto comenzamos a programar el modo grafico-------------------------------------------------------

    GraficarAutomata()

    #--------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


