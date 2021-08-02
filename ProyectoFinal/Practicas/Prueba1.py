import cv2
import numpy as np
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage.morphology import watershed
from skimage.feature import peak_local_max

nombrei = 'Otono.jpg' #Imagen
image = cv2.imread(nombrei) #Abrir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Gris
#gray = gray[:, 40:74] #Cortar

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Umbralizar
thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #Negativo

kernel = np.array((
        [ 0, 0, 0],
        [ 0, 0, 0],
        [ 1, 1, 1]), dtype="uint8") #Kernel
kernel1 = np.array((
        [ 1, 1,-1],
        [ 1, 1,-1],
        [ 1, 1,-1]), dtype="uint8") #Kernel
dilation = cv2.dilate(thresh, kernel, iterations = 1) #Dilatar
dilation1 = cv2.dilate(thresh1, kernel, iterations = 1) #Dilatar negativo

Mezcla = cv2.bitwise_not(cv2.bitwise_xor(dilation, dilation1)) #Hacer fondo negro y gatos blancos
Mezcla = cv2.dilate(Mezcla, kernel1, iterations = 1)

cv2.imshow('thresh', thresh)
cv2.moveWindow('thresh', 100, 5)

cv2.imshow('thresh1', thresh1)
cv2.moveWindow('thresh1', 300, 5)

cv2.imshow('dilation', dilation)
cv2.moveWindow('dilation', 500, 5)

cv2.imshow('dilation1', dilation1)
cv2.moveWindow('dilation1', 700, 5)

cv2.imshow('Mezcla', Mezcla)
cv2.moveWindow('Mezcla', 900, 5)

cv2.waitKey()
cv2.destroyAllWindows()
