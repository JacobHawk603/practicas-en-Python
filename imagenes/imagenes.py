import cv2
import numpy as np
import copy

img = cv2.imread('src/momiji.jpg', 1)
imgGris = cv2.imread('src/momiji.jpg', 0)
largo, alto, profundidad = img.shape
cv2.imshow("Imagen de una ninja", img)

#cv2.imgwrite('imagenNueva.png', img) <- Para guargar una nueva imgaen

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
bgr = np.hstack([b,g,r])
cv2.imshow('Capas', bgr) # <- Todo lo anterior ya separa las capas de color en bgr

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r1 = rgb[:,:,0]
g1 = rgb[:,:,1]
b1 = rgb[:,:,2]

rgb1 = np.hstack([r1,g1,b1])
cv2.imshow('Capas 2', rgb) # <- Todo lo anterior ya separa las capas de color en rgb

# Aquí realizaremos una separación de capas pero modificando valores de la matriz para que la imagen se muestre solo con cada capa de forma independiente

b = copy.copy(img)
g = copy.copy(img)
r = copy.copy(img)

b[:,:,1] = 0
b[:,:,2] = 0 #<- igualamos a 0 las capas de color r y g, dejando en la imagen únicamente la capa b

g[:,:,0] = 0
g[:,:,2] = 0 #<- igualamos a 0 las capas de color r y g, dejando en la imagen únicamente la capa g

r[:,:,0] = 0
r[:,:,1] = 0 #<- igualamos a 0 las capas de color r y g, dejando en la imagen únicamente la capa r

#concatenamos las capas en una sola imagen

bgrColor = np.hstack([b,g,r])

cv2.imshow('capas bgr a color', bgrColor)
cv2.imshow('foto a escala de grises', imgGris)

negativo = np.zeros(img.shape, img.dtype)

for y in range(largo):
    for x in range(alto):
        for z in range(profundidad):
            negativo[y,x,z] = 255- img[y,x,z]

cv2.imshow('negativo de la imagen', negativo)


cv2.waitKey(0)
cv2.destroyAllWindows()
