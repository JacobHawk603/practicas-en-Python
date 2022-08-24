import cv2
import numpy as np


img1 = cv2.imread("src/Practica8/estrella.jpg", 0)
img2 = cv2.imread("src\Practica8\engranes.png", 0)
img3 = cv2.imread("src/Practica8/figura.jpg", 0)

#estrutura1 = [[0,1,0],[1,1,1],[0,1,0]] #<- cruz de 3x3

estructura1 = np.ones((10,10), np.uint8)
estructura2 = np.uint8([[0,1,0],[1,1,1],[0,1,0]])
estructura3 = np.uint8([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]])
estructura4 = np.ones((50,50), np.uint8)

dilatacion1 = cv2.dilate(img1, estructura1, iterations=1)
dilatacion2 = cv2.dilate(img1, estructura2, iterations=1)
dilatacion3 = cv2.dilate(img1, estructura3, iterations=1)

erosion1 = cv2.erode(img2, estructura1, iterations=1)
erosion2 = cv2.erode(img2, estructura2, iterations=1)
erosion3 = cv2.erode(img2, estructura3, iterations=1)

apertura1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, estructura4)
apertura2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, estructura4)
apertura3 = cv2.morphologyEx(img3, cv2.MORPH_OPEN, estructura4)
apertura4 = cv2.morphologyEx(img3, cv2.MORPH_OPEN, estructura4)

clausura1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, estructura4)
clausura2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, estructura4)
clausura3 = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, estructura4)
clausura4 = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, estructura4)



cv2.imshow("imagen original 1",img1)
cv2.imshow("imagen original 2",img2)
cv2.imshow("imagen original 3",img3)

cv2.imshow("dilatacion 1",dilatacion1)
cv2.imshow("dilatacion 2",dilatacion2)
cv2.imshow("dilatacion 3",dilatacion3)

cv2.imshow("erosion 1",erosion1)
cv2.imshow("erosion 2",erosion2)
cv2.imshow("erosion 3",erosion3)

cv2.imshow("apertura 1",apertura1)
cv2.imshow("apertura 2",apertura2)
cv2.imshow("apertura 3",apertura3)
cv2.imshow("apertura 4",apertura4)

cv2.imshow("clausura 1",clausura1)
cv2.imshow("clausura 2",clausura2)
cv2.imshow("clausura 3",clausura3)
cv2.imshow("clausura 4",clausura4)

cv2.waitKey(0)
cv2.destroyAllWindows()