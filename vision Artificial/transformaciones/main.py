import cv2
import numpy as np
 
# function which will be called on mouse input
def extraer(action, x, y, flags, *userdata):

    global contador
  # Referencing global variables 
    global top_left_corner, bottom_right_corner
    # Mark the top left corner when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner = [(x,y)]
        # When left mouse button is released, mark bottom right corner
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner = [(x,y)]    
        # Draw the rectangle
        cv2.rectangle(imagen, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
        cv2.imshow("Window",imagen)

        imagenExtraida = recuperarPedazo()
        contador +=1
        #a la imagen que acabamos de extraer le aplicamos la transformacion
        transformar(imagenExtraida)

def recuperarPedazo():

    global top_left_corner, bottom_right_corner
    global imagen

    print(abs(bottom_right_corner[0][1]-top_left_corner[0][1]))
    recuperada = np.zeros((abs(bottom_right_corner[0][1]-top_left_corner[0][1]), abs(bottom_right_corner[0][0]-top_left_corner[0][0]), 3), imagen.dtype)

    x = top_left_corner[0][0]
    y = top_left_corner[0][1]

    for i in range(recuperada.shape[1]):

        for j in range(recuperada.shape[0]):
            if y < bottom_right_corner[0][1]:
                recuperada[j,i] = imagen[y,x]
            else:
                y = top_left_corner[0][1]

            y+=1
        x+=1

    # cv2.imshow("imagen recuperada", recuperada)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return recuperada

def main():

    # Make a temporary image, will be useful to clear the drawing

    global imagen

    temp = imagen.copy()
    # Create a named window
    cv2.namedWindow("Window")
    # highgui function called when mouse events occur
    cv2.setMouseCallback("Window", extraer)
    

    k=0
    # Close the window when key q is pressed
    while k!=113:
        # Display the imagen
        cv2.imshow("Window", imagen)
        k = cv2.waitKey(0)
        # If c is pressed, clear the window, using the dummy imagen
        if (k == 99):
            imagen= temp.copy()
            cv2.imshow("Window", imagen)
 
    cv2.destroyAllWindows()


    # cv2.imshow("triangulo", imagen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # rotar(imagen)
    return 0

def transformar(imagen):
    global contador
    angulo = -np.pi/4
    tx = 450
    ty = 0

    imgTransformada = np.zeros((500,500, 3), imagen.dtype)

    matriz = np.matrix([[np.cos(angulo), -np.sin(angulo), ty], [np.sin(angulo), np.cos(angulo), tx],[0, 0, 1]])

    prueba = np.matrix([[1,2,3],[4,5,6],[7,8,9]])

    print(matriz)
    print(matriz.I)

    #le aplcamos la transformacion a la imagen

    for i in range(imagen.shape[1]):
        for j in range(imagen.shape[0]):
            
            x = np.dot(matriz.I[1], [j,i,1])
            y = np.dot(matriz.I[0], [j,i,1])
            z = np.dot(matriz.I[2], [j,i,1])

            if z != 0:
                x /= z
                y /= z

            #print(int(x))
            # if x >= 209:    x = 208
            # if y>=209:      y = 208

            imgTransformada[int(y),int(x)] = imagen[j,i]
    

    cv2.imshow("transformacion{}".format(contador), imgTransformada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Lists to store the bounding box coordinates
    top_left_corner=[]
    bottom_right_corner=[]
    contador = 1
    #cargamos la imagen
    imagen = cv2.imread("../src/lenna_main.jpg")

    main()