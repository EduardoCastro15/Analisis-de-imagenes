import cv2
import numpy as np
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage.morphology import watershed
from skimage.feature import peak_local_max

nombrei = 'Otono.jpg'

def Histograma():
	im = Image.open(nombrei)
	im = im.convert('L')
	[ren, col] = im.size
	total = ren * col
	a = np.asarray(im, dtype = np.float32)
	a = a.reshape(1, total)
	a = a.astype(int)
	a = max(a)
	valor = 0
	maxd = max(a)
	grises = maxd
	vec = np.zeros(grises + 1)
	for i in range(total - 1):
		valor = a[i]
		vec[valor] = vec[valor] + 1    
	plt.plot(vec)
	plt.show() 

image = cv2.imread(nombrei)
#Histograma()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = gray[50:740, 40:74]
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#thresh = cv2.threshold(gray, 249, 255, cv2.THRESH_BINARY)[1]

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations = 1)
erosion = cv2.erode(dilation, kernel, iterations = 1)
dilation = cv2.dilate(erosion, kernel, iterations = 1)

dilation1 = cv2.dilate(thresh1, kernel, iterations = 1)
erosion1 = cv2.erode(dilation1, kernel, iterations = 1)
dilation1 = cv2.dilate(erosion1, kernel, iterations = 1)

Mezcla = cv2.bitwise_xor(dilation, dilation1)
Mezcla = cv2.bitwise_not(Mezcla)

Closing = cv2.morphologyEx(Mezcla, cv2.MORPH_CLOSE, kernel)

kernel1 = np.array((
        [-1,-1,-1],
        [ 1, 1, 1],
        [ 1, 1, 1]), dtype="int") #
kernel2 = np.array((
        [ 1, 1, 1],
        [ 1, 1, 1],
        [-1,-1,-1]), dtype="int") #
kernel3 = np.array((
        [ 1, 1,-1],
        [ 1, 1,-1],
        [ 1, 1,-1]), dtype="int") #
kernel4 = np.array((
        [-1, 1, 1],
        [-1, 1, 1],
        [-1, 1, 1]), dtype="int") #
kernel5 = np.array((
        [ 1, 1,-1],
        [ 1,-1,-1],
        [-1,-1,-1]), dtype="int") #
kernel6 = np.array((
        [-1, 1, 1],
        [-1,-1, 1],
        [-1,-1,-1]), dtype="int") #
kernel7 = np.array((
        [-1,-1,-1],
        [-1,-1, 1],
        [-1, 1, 1]), dtype="int") #
kernel8 = np.array((
        [-1,-1,-1],
        [ 1,-1,-1],
        [ 1, 1,-1]), dtype="int") #

output_image1 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel1)
output_image2 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel2)
output_image3 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel3)
output_image4 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel4)
output_image5 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel5)
output_image6 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel6)
output_image7 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel7)
output_image8 = cv2.morphologyEx(Mezcla, cv2.MORPH_HITMISS, kernel8)

Suma = cv2.add(output_image1, output_image2)
Suma = cv2.add(Suma, output_image3)
Suma = cv2.add(Suma, output_image4)
Suma = cv2.add(Suma, output_image5)
Suma = cv2.add(Suma, output_image6)
Suma = cv2.add(Suma, output_image7)
Suma = cv2.add(Suma, output_image8)

cv2.imshow('thresh', thresh)
cv2.moveWindow('thresh', 200, 5)

cv2.imshow('dilation', dilation)
cv2.moveWindow('dilation', 400, 5)

cv2.imshow('dilation1', dilation1)
cv2.moveWindow('dilation1', 600, 5)

cv2.imshow('Mezcla', Mezcla)
cv2.moveWindow('Mezcla', 800, 5)

cv2.imshow('Closing', Closing)
cv2.moveWindow('Closing', 1000, 5)

cv2.imshow('Suma', Suma)
cv2.moveWindow('Suma', 1200, 5)

cv2.waitKey()
cv2.destroyAllWindows()
