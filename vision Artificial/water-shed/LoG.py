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
    imagenBN = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    largo, alto = imagenBN.shape

    #obtenemos el histograma de la imagen para el futuro umbralado
    histograma = obtenerHistograma(imagenBN)

    #aplicamos el suavizado
    kernelLoG = filtros.kernelLoG(5, 1)
    
    #obtenemos la imagen de transición
    imagenExpandida = filtros.expandirImagen(imagenBN, kernelLoG)

    #aplicamos el filtro LoG
    filtradaLoG = filtros.filtrarImagenLoG(imagenExpandida, imagenBN, kernelLoG)

    #obtenemos el umbral con OTSU
    #umbral = binarizacion.OTSU(histograma)

    #umbralamos
    #imagenUmbraladaLoG = binarizacion.umbralar(filtradaLoG, largo, alto, umbral)

    #aplicamos el watershed desde la funcion
    #waterShed(imagenUmbraladaGaussiana)

    #deteccion de bordes
    obtenerBordes(filtradaLoG)

    cv2.imshow("Lenna", imagen)
    cv2.imshow("Lenna blanco y negro", imagenBN)
    #cv2.imshow("Lenna Umbralada", imagenUmbraladaLoG)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def obtenerBordes(imagenFiltradaLog):

    largo, alto = imagenFiltradaLog.shape
    
    matrizDetectoraBordes = np.zeros(imagenFiltradaLog.shape, imagenFiltradaLog.dtype)
    matrizDelta = np.zeros(imagenFiltradaLog.shape, imagenFiltradaLog.dtype)
    imagenBordada = np.zeros(imagenFiltradaLog.shape, imagenFiltradaLog.dtype)

    delta = 5

    #logica para la deteccion de cruces con cero <- matriz detectora de bordes

    for j in range(alto):
        for i in range(largo):

            if(i>0 and i<largo-1):
                if((imagenFiltradaLog[i-1,j] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j] > 0 and imagenFiltradaLog[i,j] < 0)):
                    matrizDetectoraBordes[i-1,j] = 1

                if((imagenFiltradaLog[i+1,j] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j] > 0 and imagenFiltradaLog[i,j] < 0)):
                    matrizDetectoraBordes[i+1,j] = 1

                if(j > 0 and j<alto-1):
                    if((imagenFiltradaLog[i,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j-1] = 1

                    if((imagenFiltradaLog[i,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j+1] = 1

                    if((imagenFiltradaLog[i-1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j-1] = 1

                    if((imagenFiltradaLog[i+1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j+1] = 1

                    if((imagenFiltradaLog[i-1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j+1] = 1

                    if((imagenFiltradaLog[i+1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j-1] = 1

                elif(j==0):

                    if((imagenFiltradaLog[i,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j+1] = 1

                    if((imagenFiltradaLog[i+1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j+1] = 1

                    if((imagenFiltradaLog[i-1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j+1] = 1
                
                elif(j == alto-1):

                    if((imagenFiltradaLog[i,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j-1] = 1

                    if((imagenFiltradaLog[i+1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j-1] = 1

                    if((imagenFiltradaLog[i-1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j-1] = 1
            
            elif(i == 0):

                if((imagenFiltradaLog[i+1,j] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j] > 0 and imagenFiltradaLog[i,j] < 0)):
                    matrizDetectoraBordes[i+1,j] = 1

                if(j > 0 and j < alto-1):
                    if((imagenFiltradaLog[i,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j-1] = 1

                    if((imagenFiltradaLog[i,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j+1] = 1

                    if((imagenFiltradaLog[i+1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j+1] = 1

                    if((imagenFiltradaLog[i+1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j-1] = 1

                elif(j==0):

                    if((imagenFiltradaLog[i,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j+1] = 1

                    if((imagenFiltradaLog[i+1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j+1] = 1
                
                elif(j == alto-1):

                    if((imagenFiltradaLog[i,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j-1] = 1

                    if((imagenFiltradaLog[i+1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i+1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i+1,j-1] = 1

            elif(i == largo-1):

                if((imagenFiltradaLog[i-1,j] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j] > 0 and imagenFiltradaLog[i,j] < 0)):
                    matrizDetectoraBordes[i-1,j] = 1

                if(j > 0 and j < alto-1):
                    if((imagenFiltradaLog[i,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j-1] = 1

                    if((imagenFiltradaLog[i,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j+1] = 1

                    if((imagenFiltradaLog[i-1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j+1] = 1

                    if((imagenFiltradaLog[i-1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j-1] = 1

                elif(j==0):

                    if((imagenFiltradaLog[i,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j+1] = 1

                    if((imagenFiltradaLog[i-1,j+1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j+1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j+1] = 1
                
                elif(j == alto-1):

                    if((imagenFiltradaLog[i,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i,j-1] = 1

                    if((imagenFiltradaLog[i-1,j-1] < 0 and imagenFiltradaLog[i,j] >0) or (imagenFiltradaLog[i-1,j-1] > 0 and imagenFiltradaLog[i,j] < 0)):
                        matrizDetectoraBordes[i-1,j-1] = 1

    #Logica para la segunda matriz <- matriz delta:

    for j in range(alto):
        for i in range(largo):

            if(i>0 and i<largo-1):
                if(abs(imagenFiltradaLog[i-1,j] - imagenFiltradaLog[i,j]) > delta):
                    matrizDelta[i-1,j] = 1

                if(abs(imagenFiltradaLog[i+1,j] - imagenFiltradaLog[i,j]) > delta):
                    matrizDelta[i+1,j] = 1

                if(j > 0 and j<alto-1):
                    if(abs(imagenFiltradaLog[i,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j-1] = 1

                    if(abs(imagenFiltradaLog[i,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j+1] = 1

                    if(abs(imagenFiltradaLog[i-1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j-1] = 1

                    if(abs(imagenFiltradaLog[i+1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j+1] = 1

                    if(abs(imagenFiltradaLog[i-1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j+1] = 1

                    if(abs(imagenFiltradaLog[i+1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j-1] = 1

                elif(j==0):

                    if(abs(imagenFiltradaLog[i,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j+1] = 1

                    if(abs(imagenFiltradaLog[i+1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j+1] = 1

                    if(abs(imagenFiltradaLog[i-1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j+1] = 1
                
                elif(j == alto-1):

                    if(abs(imagenFiltradaLog[i,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j-1] = 1

                    if(abs(imagenFiltradaLog[i-1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j-1] = 1

                    if(abs(imagenFiltradaLog[i+1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j-1] = 1
            
            elif(i == 0):

                if(abs(imagenFiltradaLog[i+1,j] - imagenFiltradaLog[i,j]) > delta):
                    matrizDelta[i+1,j] = 1

                if(j > 0 and j<alto-1):
                    if(abs(imagenFiltradaLog[i,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j-1] = 1

                    if(abs(imagenFiltradaLog[i,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j+1] = 1

                    if(abs(imagenFiltradaLog[i+1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j+1] = 1

                    if(abs(imagenFiltradaLog[i+1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j-1] = 1

                elif(j==0):

                    if(abs(imagenFiltradaLog[i,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j+1] = 1

                    if(abs(imagenFiltradaLog[i+1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j+1] = 1
                
                elif(j == alto-1):

                    if(abs(imagenFiltradaLog[i,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j-1] = 1

                    if(abs(imagenFiltradaLog[i+1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i+1,j-1] = 1

            elif(i == largo-1):

                if(abs(imagenFiltradaLog[i-1,j] - imagenFiltradaLog[i,j]) > delta):
                    matrizDelta[i-1,j] = 1

                if(j > 0 and j<alto-1):
                    if(abs(imagenFiltradaLog[i,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j-1] = 1

                    if(abs(imagenFiltradaLog[i,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j+1] = 1

                    if(abs(imagenFiltradaLog[i-1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j-1] = 1

                    if(abs(imagenFiltradaLog[i-1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j+1] = 1

                elif(j==0):

                    if(abs(imagenFiltradaLog[i,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j+1] = 1

                    if(abs(imagenFiltradaLog[i-1,j+1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j+1] = 1
                
                elif(j == alto-1):

                    if(abs(imagenFiltradaLog[i,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i,j-1] = 1

                    if(abs(imagenFiltradaLog[i-1,j-1] - imagenFiltradaLog[i,j]) > delta):
                        matrizDelta[i-1,j-1] = 1
    
    for i in range(alto):
        for j in range(largo):
            imagenBordada[j,i] = not(matrizDelta[j,i] and matrizDetectoraBordes[j,i])

    #revisemos que estamos haciendolo correctamente
    prueba = binaria2Umbralada(matrizDetectoraBordes)
    prueba2 = binaria2Umbralada(matrizDelta)

    cv2.imshow("prueba", prueba)
    cv2.imshow("prueba2", prueba2)
    cv2.imshow("imagen bordada", imagenBordada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def binaria2Umbralada(matrizBordes):

    largo, alto = matrizBordes.shape

    convertida = np.zeros(matrizBordes.shape, matrizBordes.dtype)

    for i in range(alto):
        for j in range(largo):

            if(matrizBordes[j,i] == 1):
                convertida[j,i] = 0
            else:
                convertida[j,i] = 255

    return convertida


if __name__ == "__main__":
    main()