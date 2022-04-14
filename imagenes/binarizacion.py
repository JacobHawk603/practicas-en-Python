import cv2
import numpy as np

umbral = int(input('valor del Umbral: '))
img = cv2.imread('lenna_main.jpg', 0)
cv2.imshow("imagen original", img)
largo, alto = img.shape


img2 = np.zeros(img.shape, img.dtype)

for x in range(largo):
    for y in range(alto):
        if(img[x, y]<umbral):
            img2[x, y] = 0
        else:
            img2[x,y] = 255


cv2.imshow("imagen umnbralada", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()