import cv2
import numpy as np

img = cv2.imread('Captura de pantalla 2022-04-09 225912.jpg', 0)
cv2.imshow("imagen original", img)
largo, alto = img.shape

def binarizacion(largo, alto, img):
    umbral = int(input('valor del Umbral: '))
    img2 = np.zeros(img.shape, img.dtype)
    for x in range(largo):
        for y in range(alto):
            if(img[x, y]<umbral):
                img2[x, y] = 0
            else:
                img2[x,y] = 255
    return img2

def logaritmo(largo, alto, img):
    c = int(input('valor de c: '))
    img2 = np.zeros(img.shape, img.dtype)
    for x in range(largo):
        for y in range(alto):
            img2[x,y] = ((c*np.log2(1+img[x,y]))*255)/(8*c)
    return img2

def potencia(largo, alto, img):
    
    c = int(input('valor de c: '))
    k = float(input('valor de y: '))
    img2 = np.zeros(img.shape, img.dtype)
    for x in range(largo):
        for y in range(alto):
            img2[x,y] = ((c*(img[x,y]**k))*255)/(255**k)
    return img2

#cv2.imshow("imagen umnbralada", binarizacion(largo, alto, img))
cv2.imshow("imagen transformada logaritmo", logaritmo(largo, alto, img))
cv2.imshow("imagen transformada potencia", potencia(largo, alto, img))


cv2.waitKey(0)
cv2.destroyAllWindows()