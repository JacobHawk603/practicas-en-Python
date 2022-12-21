import cv2
import numpy as np

def main():

    #cargamos la imagen
    imagen = cv2.imread("../src/triangulo.png")

    cv2.imshow("triangulo", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    rotar(imagen)
    return 0

def rotar(imagen):
    angulo = np.pi/4
    tx = 0
    ty = 450

    imgTransformada = np.zeros((500,500, 3), imagen.dtype)

    matriz = np.matrix([[np.cos(angulo), -np.sin(angulo), tx], [np.sin(angulo), np.cos(angulo), ty],[0, 0, 1]])

    prueba = np.matrix([[1,2,3],[4,5,6],[7,8,9]])

    print(matriz)
    print(matriz.I)

    #le aplcamos la transformacion a la imagen

    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            
            x = np.dot(matriz.I[0], [i,j,1])
            y = np.dot(matriz.I[1], [i,j,1])
            z = np.dot(matriz.I[2], [i,j,1])

            if z != 0:
                x /= z
                y /= z

            #print(int(x))
            # if x >= 209:    x = 208
            # if y>=209:      y = 208

            imgTransformada[int(x),int(y)] = imagen[i,j]
    

    cv2.imshow("triangulo2", imgTransformada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()