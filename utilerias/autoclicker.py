import mouse
import time

# left click
# mouse.click('left')

# # right click
# mouse.click('right')

# # middle click
# mouse.click('middle')

def switch_bandera():
    global bandera

    # print("right click")
    bandera = False

if __name__ == "__main__":

    bandera = True

    print("""Este algoritmo grabará todos los movimientos que hagas con el mause, y una vez que presiones el boton derecho del mouse,
           comenzará a repetir los movimientos que realizaste\n\n
          
          comencemos por grabar los movimientos:\n\n
          
          1. mueve el mouse como quieras moverlo\n
          2. presiona el botón derecho del mouse""")

    events = mouse.record()

    print("el algoritmo se está ejecutando...\n\n si deseas parar el bucle, pulsa el botón isquiero del mouse")
    
    while bandera:

    #     mouse.click('left')
    #     mouse.wheel(1)
    #     # print("click")
    #     x,y = mouse.get_position()

    #     print(x,y)
        
    #     mouse.on_click(callback=print("left click"))

    #     time.sleep(3)

        mouse.on_click(callback=switch_bandera)

        mouse.play(events[:-1])

    print("Se ha parado el bucle, hasta pronto")