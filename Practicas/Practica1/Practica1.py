from PIL import Image
import time

def abrir_imagen(imagen):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/etsza/Desktop/Imagenes/" + imagen) #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def escala_de_grises(imagen):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("CMA-x1.png") #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen2 = imagen
    i = 0
    while i < imagen2.size[0]:
        j = 0
        while j < imagen2.size[1]:
            r, g, b = imagen2.getpixel((i,j))
            p = (r + g + b) / 3
            gris = int (p)
            pixel = tuple ([gris,gris,gris])
            imagen2.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen2.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")    
    
def negativo_color(imagen):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/etsza/Desktop/Imagenes/" + imagen) #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen5 = imagen
    i = 0
    while i < imagen5.size[0]:
        j = 0
        while j < imagen5.size[1]:
            r, g, b = imagen5.getpixel((i,j))
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixel = tuple ([rn,gn,bn])
            imagen5.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen5.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def negativo_gris(imagen):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/etsza/Desktop/Imagenes/" + imagen) #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen6 = imagen
    i = 0
    while i < imagen6.size[0]:
        j = 0
        while j < imagen6.size[1]:
            r, g, b = imagen6.getpixel((i,j))
            p = (r + g + b) / 3
            gn = 255 - p
            gris = int (gn)
            pixel = tuple ([gris,gris,gris])
            imagen6.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen6.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

def blanco_negro (imagen,parametro):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/etsza/Desktop/Imagenes/" + imagen) #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen7 = imagen
    i = 0
    while i < imagen7.size[0]:
        j = 0
        while j < imagen7.size[1]:
            r, g, b = imagen7.getpixel((i,j))
            p = (r + g + b) / 3
            if p < parametro:
                imagen7.putpixel((i,j),(0,0,0))
            else:
                imagen7.putpixel((i,j),(255,255,255))
            j+=1
        i+=1
    imagen7.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

def negativo_blanco_negro (imagen,parametro):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/etsza/Desktop/Imagenes/" + imagen) #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen7 = imagen
    i = 0
    while i < imagen7.size[0]:
        j = 0
        while j < imagen7.size[1]:
            r, g, b = imagen7.getpixel((i,j))
            p = (r + g + b) / 3
            if p < parametro:
                imagen7.putpixel((i,j),(255,255,255))
            else:
                imagen7.putpixel((i,j),(0,0,0))
            j+=1
        i+=1
    imagen7.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
