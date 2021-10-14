import cv2 as cv
import numpy as np

""" Este programa prácticamente nos marca el contorno del umbral (thresolding)
los parámetros de la función threshold nos definen un valor mínimo de umbral y
uno máximo, el mínimo funciona tal que todos los valores menores a el se van al
cero, mientras los que están por arriba del mínimo permanecen. El tope es el 
valor máximo que es el blanco, tomado como referencia 255"""
imagen = cv.imread('imagenX.jpg')
imagen = ~imagen
nImg = cv.resize(imagen, (0,0), fx=0.2, fy=0.2)
gris = cv.cvtColor(nImg, cv.COLOR_BGR2GRAY)
_,th = cv.threshold(gris,254,255,cv.THRESH_BINARY)

contornos, jerarquia = cv.findContours(th, 
	cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(nImg, contornos, -1, (0,255,0), 2)

cv.imshow('th',th)
cv.imshow('imagen', nImg)
#cv.imshow('gris', gris)
cv.waitKey(0)
cv.destroyAllWindows()