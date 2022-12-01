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
    imagen = cv2.imread("../src/monedad.jpg", 1)
    imagenBN = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    largo, alto = imagenBN.shape

    #obtenemos el histograma de la imagen para el futuro umbralado
    histograma = obtenerHistograma(imagenBN)

    #aplicamos el suavizado
    kernelLoG = filtros.kernelLoG(5, 1)

    #aplicamos el suavizado con el gausiano
    kernelGaussiano = filtros.kernelGauss(5,1)
    
    #obtenemos la imagen de transición
    imagenExpandida = filtros.expandirImagen(imagenBN, kernelLoG)

    #aplicamos el filtro LoG
    filtradaLoG = filtros.filtrarImagen(imagenExpandida, imagenBN, kernelLoG)

    #aplicamos tambien el filtro gausiano
    filtradaGausiano = filtros.filtrarImagen(imagenExpandida, imagenBN, kernelGaussiano)

    #obtenemos el umbral con OTSU
    umbral = binarizacion.OTSU(histograma)

    #umbralamos
    imagenUmbraladaLoG = binarizacion.umbralar(filtradaLoG, largo, alto, umbral)
    imagenUmbraladaGaussiana = binarizacion.umbralar(filtradaGausiano, largo, alto, umbral)

    #aplicamos el watershed desde la funcion
    #waterShed(imagenUmbraladaGaussiana)

    cv2.imshow("Lenna", imagen)
    cv2.imshow("Lenna blanco y negro", imagenBN)
    cv2.imshow("Lenna Umbralada", imagenUmbraladaLoG)
    cv2.imshow("Lenna Umbralada", imagenUmbraladaGaussiana)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    waterShed(imagenUmbraladaGaussiana, imagen, umbral)


def waterShed(imagenUmbralada, imagen, umbral):

    thresh = umbral
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(imagenUmbralada,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)
    cv2.imshow("Lenna", sure_fg)


    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(imagen,markers)
    imagen[markers == -1] = [255,0,0]

    cv2.imshow("watershed", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()