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
gray = gray[50:740, 40:73] #Cortar

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Umbralizar
thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #Negativo

kernel = np.ones((3, 3), np.uint8) #Kernel
dilation = cv2.dilate(thresh, kernel, iterations = 1) #Dilatar
dilation1 = cv2.dilate(thresh1, kernel, iterations = 1) #Dilatar negativo

Mezcla = cv2.bitwise_not(cv2.bitwise_xor(dilation, dilation1)) #Hacer fondo negro y gatos blancos

kernel1 = np.array((
        [-1,-1,-1,-1,-1],
        [ 1, 1, 1, 1, 1],
        [ 1, 1, 1, 1, 1],
        [ 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0]), dtype="uint8")
HitMiss = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel1) #Ubicar lineas indeseadas

Erosion = cv2.erode(HitMiss, kernel, iterations = 1)

Final = cv2.bitwise_xor(HitMiss, Mezcla)


cv2.imshow('thresh', thresh)
cv2.moveWindow('thresh', 100, 5)

cv2.imshow('Mezcla', Mezcla)
cv2.moveWindow('Mezcla', 300, 5)

cv2.imshow('HitMiss', HitMiss)
cv2.moveWindow('HitMiss', 500, 5)

cv2.imshow('Erosion', Erosion)
cv2.moveWindow('Erosion', 700, 5)

cv2.imshow('Final', Final)
cv2.moveWindow('Final', 900, 5)

cv2.waitKey()
cv2.destroyAllWindows()
