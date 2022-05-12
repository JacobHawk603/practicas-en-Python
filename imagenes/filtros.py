import cv2
import numpy as np

def filtroPromedio():
    img = cv2.imread("src/practica7/1-img-promedio.jpg",0)
    
    largoIMG, altoIMG = img.shape
    imgRes = np.zeros([largoIMG-2, altoIMG-2])
    
    mascara1 = np.zeros([3,3], img.dtype)

    largoMAS, altoMAS = mascara1.shape
    for x in range(largoMAS):
        for y in range(altoMAS):
            mascara1[x,y] = 1

    imgRes= cv2.filter2D(img, -1, mascara1)

    cv2.imshow("original", img)
    cv2.imshow("filtro promedio", imgRes)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

filtroPromedio()

