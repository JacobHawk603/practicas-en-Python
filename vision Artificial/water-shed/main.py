import cv2
from librerias import binarizacion

def obtenerHistograma(imagenBN):
    contador = 0
    histograma = []

    largo, alto = imagenBN.shape

    for i in range(256):
        contador = 0

        for j in range(largo):
            for k in range(alto):
                
                if imagenBN[j,k] == i:
                    contador += 1
        
        histograma.append(contador)

    return histograma

def main():
    imagen = cv2.imread("../src/lenna_main.jpg", 1)
    imagenBN = cv2.imread("../src/lenna_main.jpg", 0)
    largo, alto = imagenBN.shape

    histograma = obtenerHistograma(imagenBN)

    umbral = binarizacion.OTSU(histograma)

    imagenUmbralada = binarizacion.umbralar(imagenBN, largo, alto, umbral)

    cv2.imshow("Lenna", imagen)
    cv2.imshow("Lenna blanco y negro", imagenBN)
    cv2.imshow("Lenna Umbralada", imagenUmbralada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()