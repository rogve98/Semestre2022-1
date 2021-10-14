import numpy as np
import cv2 as cv

""" Esta función utiliza las matrices de sobel que son una corrección al
método del gradiente para corrección de imagenes en sus bordes. Las matrices
son como las que se definen en Hsx y Hsy y nos generan una mejor calidad y
visibilidad de los bordes. La idea también es aplicar la norma cuadrada de 
las matrices..."""
imagen = cv.imread('imagenX.jpg')
imagen = ~imagen
nImg = cv.resize(imagen, (0,0), fx=0.25, fy=0.25)

frameFloat = nImg.astype(float)
Hsx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Hsy = np.transpose(Hsx)


bordex = cv.filter2D(frameFloat,-1,Hsx)
bordey = cv.filter2D(frameFloat,-1,Hsy)

Mxy = bordex**2 + bordey**2
Mxy = np.sqrt(Mxy)
Mxy = Mxy/np.max(Mxy)

cv.imshow('bordes', Mxy)
cv.waitKey(0)
cv.destroyAllWindows()