import cv2
import numpy as np

def main():

    #cargamos la imagen
    imagen = cv2.imread("../src/triangulo.png")

    cv2.imshow("triangulo", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 0

def rotar(imagen):
    angulo = np.pi/2
    tx = 0
    ty = 0

    matriz = [[[np.cos(angulo), -np.sin(angulo), 0], [np.sin(angulo), np.cos(angulo), 0]],[tx, ty, 1]]

if __name__ == "__main__":
    main()