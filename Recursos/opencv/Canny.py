import cv2 as cv
import numpy as np

""" El contorno Canny es lo mismo que el sobel solo que opera únicamente
con el gradiente, cv.Canny funciona con un valor minimo y un valor máximo 
del gradiente, es decir, proyecta las regiones de mayor y menor intensidad 
de acuerdo a los valores del umbral puestos en cada variable"""
imagen = cv.imread('imagenX.jpg')
imagen = ~imagen
nImg = cv.resize(imagen, (0,0), fx=0.2, fy=0.2)

contornoImg = cv.Canny(nImg,20,30)

cv.imshow('Imagen recalculada',contornoImg)
cv.waitKey(0)
cv.destroyAllWindows()