import cv2
import numpy as np
import copy
import matplotlib.pyplot as pl
import math

img = cv2.imread('momiji.jpg', 1)
imgGris = cv2.imread('momiji.jpg', 0)
#largo, alto, profundidad = img.shape
cv2.imshow("Imagen de una ninja", img)

def datosEstadisticos(img):
    media = np.mean(img[: , :])
    mediana = np.median(img[: , :])
    varianza = np.var(img[:, :])
    desviacion = np.std(img[:, :])

    print("media Aritmetica: ", media)
    print("mediana: ", mediana)
    print("varianza: ", varianza)
    print("desviacion estandar", desviacion)


#graficando el histograma de la capa b
print("histograma y variables de la capa b\n\n")
datosEstadisticos(img[:, :, 0])
pl.hist(img[:, : , 0])
pl.show()


#graficando el histograma de la capa g
print("histograma y variables de la capa g\n\n")
datosEstadisticos(img[:, :, 1])
pl.hist(img[:, : , 1])
pl.show()


#graficando el histograma de la capa r
print("histograma y variables de la capa r\n\n")
datosEstadisticos(img[:, :, 2])
pl.hist(img[:, : , 2])
pl.show()

#graficando el histograma de la imgen a escala de grisesd
print("histograma y variables de la imagen a escala de grises\n\n")
datosEstadisticos(imgGris[:, :])
pl.hist(imgGris[: , :])
pl.show()



