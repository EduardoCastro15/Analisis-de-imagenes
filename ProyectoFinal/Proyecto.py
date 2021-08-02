import streamlit as st
import cv2
import numpy as np
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from scipy import ndimage

def PreparadoImagen(image):
	st.subheader("2.- Pasar a escala de grises")
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Gris
	st.image(gray, width=700, caption="Imagen en escala de grises")
	st.subheader("3.- Recortar la imagen, para trabajar unicamente con el area deseada")
	gray = gray[:, :74] #Cortar
	st.image(gray, width=50, caption="Imagen recortada")
	return gray

def UmbralizadoImagen(gray):
	st.subheader("4.- Binarizar la imagen utilizando el método de Otsu")
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Umbralizar
	st.image(thresh, width=50, caption="Imagen binarizada aplicando umbralizado Otsu")
	st.subheader("5.- Aplicar binarizacion inversa a la imagen utilizando el método de Otsu")
	thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #Negativo
	st.image(thresh1, width=50, caption="Imagen binarizada inversamente aplicando umbralizado Otsu")
	return thresh, thresh1

def LocalizacionPatrones(thresh, thresh1):
	st.subheader("6.- Localización de patrones...haciendo uso de los elementos de estructura (ee)")
	kernel = np.array((
	        [ 0, 0, 0],
	        [ 0, 0, 0],
	        [ 1, 1, 1]), dtype="uint8") #Elemento de estructura 1
	kernel1 = np.array((
	        [ 1, 1,-1],
	        [ 1, 1,-1],
	        [ 1, 1,-1]), dtype="uint8") #Elemento de estructura 2

	st.subheader("7.- Dilatar ambas imagenes binarizadas")
	dilation = cv2.dilate(thresh, kernel, iterations = 1) #Dilatar
	st.image(dilation, width=50, caption="Imagen aplicando dilatación")
	dilation1 = cv2.dilate(thresh1, kernel, iterations = 1) #Dilatar negativo
	st.image(dilation1, width=50, caption="Imagen inversa aplicando dilatación")

	st.subheader("8.- Mezclar ambas imagenes dilatadas, usando el operador XOR, y negando el resultado NOT")
	Mezcla = cv2.bitwise_xor(dilation, dilation1) #Hacer fondo blanco y gatos negros
	st.image(Mezcla, width=50, caption="Imagen mezclada usando el operador XOR")
	Mezcla = cv2.bitwise_not(Mezcla)
	st.image(Mezcla, width=50, caption="Imagen anterior negada (NOT)")

	st.subheader("9. Volver a diltar el resultado de la mezcla usando el segundo elemento de estructura")
	Mezcla = cv2.dilate(Mezcla, kernel1, iterations = 1)
	st.image(Mezcla, width=50, caption="Imagen aplicando dilatación")
	return dilation, dilation1, Mezcla

def GradienteMorfologico(image, thresh):
	st.subheader("10.- Aplicar el gradiente morfológico a la imagen ya tratada")
	# Calcular la distancia Euclidea de cada pixel binario al pixel cero mas cercano, luego encuentra los picos
	st.subheader("11.- Calcular la distancia Euclidea de cada pixel binario al pixel cero mas cercano, luego encontrar los picos")
	distance_map = ndimage.distance_transform_edt(thresh)
	local_max = peak_local_max(distance_map, indices=False, min_distance=5, labels=thresh)
	
	# Aplicar analisis de componentes conexos, luego aplicar Watershed
	st.subheader("12.- Aplicar analisis de componentes conexos, luego aplicar Watershed")
	markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
	labels = watershed(-distance_map, markers, mask=thresh)
	
	# Iterar atravez de etiquetas unicas
	st.subheader("13.- Iterar atravez de etiquetas unicas")
	st.subheader("13.1.- Crear máscara")
	st.subheader("13.2.- Encontrar contornos y determinar el area del contorno")
	st.subheader("14.- Dibujar los contornos encontrados en la imagen original e imprimir el área total")
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
		cv2.drawContours(image, [c], -1, (45, 255, 12), 1)
	st.text(total_area)
	#print(total_area)
	return image

def PresentacionImagen(Resultado):
	#cv2.imshow('Resultado', Resultado)
	st.image(Resultado, width=700, caption="Imagen original segmentada", channels='BGR')
	#cv2.moveWindow('thresh', 100, 5)
	#cv2.waitKey()
	#cv2.destroyAllWindows()

if __name__ == "__main__":
	st.title("Proyecto final -Análisis de Imágenes-")
	st.header("Segmentación del símbolo '#'")
	st.subheader("Desarrollo:")
	st.subheader("1.- Abrir la imagen")
	
	nombrei = 'Otono.jpg' #Imagen
	image = cv2.imread(nombrei) #Abrir
	st.image(image, width=700, caption="Imagen original", channels='BGR')

	gray = PreparadoImagen(image)
	thresh, thresh1 = UmbralizadoImagen(gray)
	dilation, dilation1, Mezcla = LocalizacionPatrones(thresh, thresh1)
	Resultado = GradienteMorfologico(image, Mezcla)
	PresentacionImagen(Resultado)
