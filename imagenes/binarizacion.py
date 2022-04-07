import cv2
import numpy as np

umbral = int(input('valor del Umbral'))
print("este commit pertenece al branch 1 y pertenece tambien al branch third")
print("este comentario tambien pertenece al branch third")
img = cv2.imread('rose1.jpg', 0)
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