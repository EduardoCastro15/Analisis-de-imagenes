import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage.morphology import watershed
from skimage.feature import peak_local_max

# Cargar la imagen, convertir a escala de grises, y Umbralalizacioon por Otsu
image = cv2.imread('Otono1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Calcular la distancia Euclidea de cada pixel binario al pixel cero mas cercano, luego encuentra los picos
distance_map = ndimage.distance_transform_edt(thresh)
local_max = peak_local_max(distance_map, indices=False, min_distance=5, labels=thresh)

# Aplicar analisis de componentes conexos, luego aplicar Watershed
markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
labels = watershed(-distance_map, markers, mask=thresh)

# Iterar atravez de etiquetas unicas
total_area = 0
for label in np.unique(labels):
	if label == 0:
		continue

	# Crear mascara
	mask = np.zeros(gray.shape, dtype="uint8")
	mask[labels == label] = 255

	# Encontrar contornos y determinar el area del contorno
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
	c = max(cnts, key=cv2.contourArea)
	area = cv2.contourArea(c)
	total_area += area
	cv2.drawContours(image, [c], -1, (36,255,12), 1)

print(total_area)
cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()
