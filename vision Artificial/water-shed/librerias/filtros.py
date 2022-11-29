import cv2
import numpy as np

def kernelGauss(dimensionFiltro, sigma):
    
    limiteFiltro = int((dimensionFiltro - 1)/2)
    kernel = np.zeros((dimensionFiltro, dimensionFiltro), float)

    i = 0
    for x in range(-limiteFiltro, limiteFiltro+1):
        j = 0
        for y in range(-limiteFiltro, limiteFiltro+1):
            kernel[i,j] = np.exp(-((pow(x, 2) + pow(y, 2)) / (2 * pow(sigma, 2)))) / (2 * np.pi * sigma**2)
            
            j+=1
        i+=1

    print(np.matrix(kernel))
    
    return kernel

def filtrarImagen(imagenBN, filtro):
    largo, alto = imagenBN.shape
    largoFiltro, altoFiltro = filtro.shape
    filtrada = np.zeros(imagenBN.shape, imagenBN.dtype)

    convolucion = 0
    x = 0
    y = 0

    for i in range(largo-15):
        for j in range(alto-15):

            x = i
            for k in range(largoFiltro):
                y = j
                for l in range(altoFiltro):
                    convolucion += float(imagenBN[x,y]) * filtro[k,l]
                    y += 1
            
                x +=1

            filtrada[i,j] = int(convolucion)
            convolucion = 0
    
    print(filtrada[:50,:50])

    cv2.imshow("original", imagenBN)
    cv2.imshow("suaizada", filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    dimensionFiltro = 15
    sigma = 1.4

    kernel = kernelGauss(dimensionFiltro, sigma)

    imagen = cv2.imread("../../src/lenna_main.jpg", 0)
    filtrarImagen(imagen, kernel)


if __name__ == "__main__":
    main()