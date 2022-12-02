import cv2
from librerias import binarizacion
from librerias import filtros
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
import numpy as np
import matplotlib.pyplot as plt

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

    #aplicamos el suavizado con el gausiano
    kernelGaussiano = filtros.kernelGauss(5,1)
    
    #obtenemos la imagen de transición
    imagenExpandida = filtros.expandirImagen(imagenBN, kernelGaussiano)

    #aplicamos tambien el filtro gausiano
    filtradaGausiano = filtros.filtrarImagen(imagenExpandida, imagenBN, kernelGaussiano)

    #obtenemos el umbral con OTSU
    umbral = binarizacion.OTSU(histograma)

    #umbralamos
    imagenUmbraladaGaussiana = binarizacion.umbralar(filtradaGausiano, largo, alto, umbral)

    #aplicamos el watershed desde la funcion
    #waterShed(imagenUmbraladaGaussiana)

    cv2.imshow("Lenna", imagen)
    cv2.imshow("Lenna blanco y negro", imagenBN)
    cv2.imshow("Lenna Umbralada", imagenUmbraladaGaussiana)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #waterShed(imagenUmbraladaGaussiana, imagen, umbral)
    watershed2(imagenUmbraladaGaussiana)


def waterShed(imagenUmbralada, imagen, umbral):

    thresh = umbral
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(imagenUmbralada,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    cv2.imshow("distancia", dist_transform)

    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    #cv2.imshow("markers", markers)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(imagen,markers)
    imagen[markers == -1] = [255,0,0]

    cv2.imshow("imagen", imagen)
    cv2.imshow("unknown area", unknown)
    cv2.imshow("fondo segurp", sure_bg)
    cv2.imshow("frente seguro", sure_fg)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    '''figura = plt.figure()
    axis1 = figura.add_subplot(1)
    axis1.'''

def watershed2(image):
    distance = ndi.distance_transform_edt(image)
    coords = peak_local_max(distance, footprint=np.ones((3, 3)), labels=image)
    mask = np.zeros(distance.shape, dtype=bool)
    mask[tuple(coords.T)] = True
    markers, _ = ndi.label(mask)
    labels = watershed(-distance, markers, mask=image)

    fig, axes = plt.subplots(ncols=3, figsize=(9, 3), sharex=True, sharey=True)
    ax = axes.ravel()

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Overlapping objects')
    ax[1].imshow(-distance, cmap=plt.cm.gray)
    ax[1].set_title('Distances')
    ax[2].imshow(labels, cmap=plt.cm.nipy_spectral)
    ax[2].set_title('Separated objects')

    for a in ax:
        a.set_axis_off()

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()