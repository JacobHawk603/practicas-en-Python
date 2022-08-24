import cv2
import numpy as np

def filtroPromedio():
    img = cv2.imread("src/practica7/1-img-promedio.jpg",0)
    img2 = cv2.imread("src/practica7/4-img-Laplaciano.jpg", 0)
    img3 = cv2.imread("src/practica7/7-img-Sobel.jpg", 0)

    
    largoIMG, altoIMG = img.shape
    imgRes = np.zeros([largoIMG-2, altoIMG-2])
    
    mascara1 = np.zeros([3,3], img.dtype)

    largoMAS, altoMAS = mascara1.shape
    for x in range(largoMAS):
        for y in range(altoMAS):
            mascara1[x,y] = 1

    imgRes= cv2.filter2D(img, -1, mascara1)
    imgRes2 = cv2.medianBlur(img, 3)

    #ahora aplicamos el filtro laplaciano a la imagen 2
    img2Res = cv2.Laplacian(img2, 0)
    print("a este me refiero: ",0)

    #ahora aplicaremos el filtro de sobel
    img3Res = cv2.Sobel(img3, cv2.CV_8U, 1,0,ksize=3)


    cv2.imshow("imagen 1 original", img)
    cv2.imshow("imagen 2 original", img2)
    cv2.imshow("imagen 3 original", img3)
    cv2.imshow("filtro promedio", imgRes)
    cv2.imshow("filtro de mediana", imgRes2)
    cv2.imshow("filtro Laplaciano", img2Res)
    cv2.imshow("filtro de Sobel", img3Res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

filtroPromedio()

