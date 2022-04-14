from operator import xor
import cv2
import numpy as np

img1 = cv2.imread('lenna_main.jpg', 0)
img2 = cv2.imread('momiji2.jpg', 0)

def sumaImagenes(img1, img2):
    img3 = np.zeros(img1.shape, img1.dtype)
    auxiliar = np.zeros(img1.shape, int)
    auxiliar2 = np.zeros(img1.shape, int)
    auxiliar3 = np.zeros(img1.shape, int)
    largo1, alto1 = img1.shape

    for x in range(largo1):
        for y in range(alto1):
            auxiliar[x,y] = img1[x,y]
            auxiliar2[x,y] = img2[x,y]
            auxiliar3[x,y] = (auxiliar[x,y] + auxiliar2[x,y])
            if(auxiliar3[x,y] >255):
                auxiliar3[x,y] = 255

            img3[x,y]=auxiliar3[x,y]
    
    return img3


def restaImagenes(img1, img2):
    img3 = np.zeros(img1.shape, img1.dtype)
    auxiliar = np.zeros(img1.shape, int)
    auxiliar2 = np.zeros(img1.shape, int)
    auxiliar3 = np.zeros(img1.shape, int)
    largo, alto = img1.shape

    for x in range(largo):
        for y in range(alto):
            auxiliar[x,y] = img1[x,y]
            auxiliar2[x,y] = img2[x,y]
            auxiliar3[x,y] = (auxiliar[x,y] - auxiliar2[x,y])
            if(auxiliar3[x,y] <0):
                auxiliar3[x,y] = 0

            img3[x,y]=auxiliar3[x,y]

    return img3

def ANDdeImagenes(img1, img2):
    img3 = np.zeros(img1.shape, img1.dtype)

    largo, alto = img1.shape

    for x in range(largo):
        for y in range(alto):

            img3[x,y]=img1[x,y] and img2[x,y]

    print(img1[0:5, 0:5])
    print(img2[0:5, 0:5])
    print(img3[0:5, 0:5])

    return img3


def ORdeImagenes(img1, img2):
    img3 = np.zeros(img1.shape, img1.dtype)
    largo, alto = img1.shape

    for x in range(largo):
        for y in range(alto):

            img3[x,y]=img1[x,y] or img2[x,y]

    return img3

def XORdeImagenes(img1, img2):
    img3 = np.zeros(img1.shape, img1.dtype)
    largo, alto = img1.shape

    for x in range(largo):
        for y in range(alto):

            img3[x,y] = xor(img1[x,y], img2[x,y])

    return img3

img3 = cv2.add(img1, img2)

cv2.imshow('imagen 1', img1)
cv2.imshow('imagen 2', img2)

cv2.imshow('suma de imagen 1 y 2', sumaImagenes(img1, img2))
cv2.imshow('resta de imagen 1 y 2', restaImagenes(img1, img2))
cv2.imshow('AND de imagenes 1 y 2', ANDdeImagenes(img1, img2))
cv2.imshow('Or de imagenes 1 y 2', ORdeImagenes(img1, img2))
cv2.imshow('XOR de imagenes 1 y 2', XORdeImagenes(img1, img2))


cv2.waitKey(0)
cv2.destroyAllWindows()