import cv2
from librerias import binarizacion
from librerias import filtros
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
import numpy as np

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

    #obtenemos el histograma de la imagen para el futuro umbralado
    histograma = obtenerHistograma(imagenBN)

    #aplicamos el suavizado
    kernel = filtros.kernelLoG(5, 1)
    
    #obtenemos la imagen de transición
    imagenExpandida = filtros.expandirImagen(imagenBN, kernel)

    #aplicamos el filtro LoG
    filtradaLoG = filtros.filtrarImagen(imagenExpandida, imagenBN, kernel)

    #obtenemos el umbral con OTSU
    umbral = binarizacion.OTSU(histograma)

    #umbralamos
    imagenUmbralada = binarizacion.umbralar(filtradaLoG, largo, alto, umbral)

    #aplicamos el watershed desde la funcion
    waterShed(imagenUmbralada)

    cv2.imshow("Lenna", imagen)
    cv2.imshow("Lenna blanco y negro", imagenBN)
    cv2.imshow("Lenna Umbralada", imagenUmbralada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def waterShed(imagenUmbralada):

    distancia = ndi.distance_transform_edt(imagenUmbralada)
    coordenadas = peak_local_max(min_distance=distancia, labels=imagenUmbralada)
    mascara = np.zeros(distancia.shape, dtype=bool)
    mascara[tuple(coordenadas.T)] = True
    marcadores, _ = ndi.label(mascara)
    etiquetas = cv2.watershed(imagenUmbralada, marcadores)


    cv2.imshow("watershed", etiquetas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()