import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 

""" Este programa implementa por separado los métodos de sobel para 
la componente x y la componente y. Además calcula el laplaciano para 
la comparación entre ambos métodos. Se diferencía este método de
sobelChido.py porque este analiza las matrices de sobel por separado,
el sobelChido junta ambos resultados en uno. """
imagen = cv.imread('imagenX.jpg')
imagen = ~imagen
nImg = cv.resize(imagen, (0,0), fx=0.2, fy=0.2)
gris = cv.cvtColor(nImg, cv.COLOR_BGR2GRAY)

# Para visualizar en blanco y negro podemos optar por la opción cv.CV_64F
# Para visualizar en escala de grises debemos poner la opción cv.CV_8U
laplaciano = cv.Laplacian(gris,cv.CV_64F)
sobelx = cv.Sobel(gris,cv.CV_8U,1,0,ksize=3)
sobely = cv.Sobel(gris,cv.CV_8U,0,1,ksize=3)

# plt.subplot(2,2,1), plt.imshow(gris,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2), plt.imshow(laplaciano, cmap='gray')
# plt.title('Laplaciano'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray')
# plt.title('SobelX'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4), plt.imshow(sobely, cmap='gray')
# plt.title('SobelY'), plt.xticks([]), plt.yticks([])
# plt.show()

#cv.imshow('Laplaciano', laplaciano)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.waitKey(0)
cv.destroyAllWindows()