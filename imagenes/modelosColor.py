import cv2
import numpy as np

imgBGR = cv2.imread("src/coloresRGB2.jpg", 1)
imgCMYK = np.zeros(imgBGR.shape, imgBGR.dtype)
imgHSI = np.zeros(imgBGR.shape, imgBGR.dtype)
largo, alto, profundidad = imgBGR.shape

c = ((1-imgBGR[:,:,2]/255)*255)
m = (1-imgBGR[:,:,1]/255)*255
y = (1-imgBGR[:,:,0]/255)*255

imgCMYK[:,:,2] = c
imgCMYK[:,:,1] = m
imgCMYK[:,:,0] = y

imgCMYK = np.hstack([imgCMYK[:,:,0], imgCMYK[:,:,1], imgCMYK[:,:,2]])


#conversion HSI

normalR = imgBGR[:,:,2]/255
normalG = imgBGR[:,:,1]/255
normalB = imgBGR[:,:,0]/255

for x in range(largo):
    for y in range(alto):
        teta = np.arccos(((1/2)*((normalR[x,y]-normalG[x,y])+(normalR[x,y]-normalB[x,y]))) / (((normalR[x,y]-normalG[x,y])**2 + ((normalR[x,y]-normalB[x,y])*(normalG[x,y]-normalB[x,y])))**(1/2)))

        if normalB[x,y] <= normalG[x,y]:
            h = teta*255
        else:
            h = (2*np.pi - teta)*255

        if(normalR[x,y] < normalB[x,y] and normalR[x,y]<normalG[x,y]):
            minRGB = normalR[x,y]
        elif(normalB[x,y] < normalR[x,y] and normalB[x,y]<normalG[x,y]):
            minRGB = normalB[x,y]
        elif(normalG[x,y] < normalB[x,y] and normalG[x,y]<normalR[x,y]):
            minRGB = normalG[x,y]
        elif(normalR[x,y] < normalB[x,y] and normalB[x,y]==normalG[x,y]):
            minRGB = normalR[x,y]
        elif(normalB[x,y] < normalR[x,y] and normalR[x,y]==normalG[x,y]):
            minRGB = normalB[x,y]
        elif(normalG[x,y] < normalB[x,y] and normalR[x,y]<normalB[x,y]):
            minRGB = normalG[x,y]
        elif(normalR[x,y] < normalB[x,y] and normalR[x,y]==normalG[x,y]):
            minRGB = normalR[x,y]
        elif(normalB[x,y] < normalR[x,y] and normalB[x,y]==normalG[x,y]):
            minRGB = normalB[x,y]
        elif(normalG[x,y] < normalB[x,y] and normalB[x,y] == normalR[x,y]):
            minRGB=normalG[x,y]
        else:
            minRGB=normalR[x,y]

        s = (1-(3/(normalR[x,y] + normalB[x,y] + normalG[x,y]))*minRGB)*255

        i = ((normalR[x,y] + normalB[x,y] + normalG[x,y])/3)*255

        imgHSI[x,y,0] = h
        imgHSI[x,y,1] = s
        imgHSI[x,y,2] = i

imgHSI = np.hstack([imgHSI[:,:,0],imgHSI[:,:,1],imgHSI[:,:,2]])
cv2.imshow("imagen rgb", imgBGR)
cv2.imshow("capas cmyk", imgCMYK)
cv2.imshow("capas hsi: ", imgHSI)

cv2.waitKey(0)
cv2.destroyAllWindows