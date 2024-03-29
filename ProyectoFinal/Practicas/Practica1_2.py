# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:11:55 2020

@author: etsza
"""

from PIL import Image
import time
import cv2

def abrir_imagen(imagen):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/georg/Desktop/" + imagen) #Concatena la ruta de la carpeta 
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def sumacolor (imagen1,imagen2):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta1 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen1) #Concatena la ruta de la carpeta 
    imagen1 = Image.open(ruta1) #Para buscar la imagen"""
    imagen1.show()
    ruta2 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen2) #Concatena la ruta de la carpeta 
    imagen2 = Image.open(ruta2) #Para buscar la imagen"""
    imagen2.show()
    imagen9 = imagen1
    imagen10 = imagen2
    i = 0
    while i < imagen9.size[0]:
        j = 0
        while j < imagen9.size[1]:
            rvalor1, gvalor1, bvalor1 = imagen9.getpixel ((i,j))
            rvalor2, gvalor2, bvalor2 = imagen10.getpixel ((i,j))
            rvaloraux1 = rvalor1 + rvalor2
            if rvaloraux1 >= 255:
                rvaloraux1 = 255
            else:
                rvaloraux1 = rvaloraux1
            gvaloraux1 = gvalor1 + gvalor2
            if gvaloraux1 >= 255:
                gvaloraux1 = 255
            else:
                gvaloraux1 = gvaloraux1
            bvaloraux1 = bvalor1 + bvalor2
            if bvaloraux1 >= 255:
                bvaloraux1 = 255
            else:
                bvaloraux1 = bvaloraux1
            pixel1 = tuple ([rvaloraux1,gvaloraux1,bvaloraux1])
            imagen9.putpixel((i,j),pixel1)
            rvaloraux2 = rvalor2 + rvalor1
            if rvaloraux2 >= 255:
                rvaloraux2 = 255
            else:
                rvaloraux2 = rvaloraux2
            gvaloraux2 = gvalor2 + gvalor1
            if gvaloraux2 >= 255:
                gvaloraux2 = 255
            else:
                gvaloraux2 = gvaloraux2
            bvaloraux2 = bvalor2 + bvalor1
            if bvaloraux2 >= 255:
                bvaloraux2 = 255
            else:
                bvaloraux2 = bvaloraux2
            pixel2 = tuple ([rvaloraux2,gvaloraux2,bvaloraux2])
            imagen10.putpixel((i,j),pixel2)
            j+=1
        i+=1
    imagen9.show()
    size = (imagen9.size[0],imagen9.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen9,(0,0))
    nueva.save("suma12.png")
    imagen10.show()
    size = (imagen10.size[0],imagen10.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen10,(0,0))
    nueva.save("suma21.png")
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

def sumagris (imagen1,imagen2):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta1 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen1) #Concatena la ruta de la carpeta 
    imagen1 = Image.open(ruta1) #Para buscar la imagen"""
    imagen1.show()
    ruta2 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen2) #Concatena la ruta de la carpeta 
    imagen2 = Image.open(ruta2) #Para buscar la imagen"""
    imagen2.show()
    imagen9 = imagen1
    imagen10 = imagen2
    i = 0
    while i < imagen9.size[0]:
        j = 0
        while j < imagen9.size[1]:
            rvalor1, gvalor1, bvalor1 = imagen9.getpixel ((i,j))
            rvalor2, gvalor2, bvalor2 = imagen10.getpixel ((i,j))
            valor1 = (rvalor1+gvalor1+bvalor1)/3
            valor2 = (rvalor2+gvalor2+bvalor2)/3
            valor1= int(valor1)
            valor2= int (valor2)
            valoraux1 = valor1 + valor2
            if valoraux1 >= 255:
                valoraux1 = 255
            else:
                valoraux1 = valoraux1
            pixel1 = tuple ([valoraux1,valoraux1,valoraux1])
            imagen9.putpixel((i,j),pixel1)            
            j+=1
        i+=1
    imagen9.show()
    size = (imagen9.size[0],imagen9.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen9,(0,0))
    nueva.save("suma.png")
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def restacolor (imagen1,imagen2):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta1 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen1) #Concatena la ruta de la carpeta 
    imagen1 = Image.open(ruta1) #Para buscar la imagen"""
    imagen1.show()
    ruta2 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen2) #Concatena la ruta de la carpeta 
    imagen2 = Image.open(ruta2) #Para buscar la imagen"""
    imagen2.show()
    imagen9 = imagen1
    imagen10 = imagen2
    i = 0
    while i < imagen9.size[0]:
        j = 0
        while j < imagen9.size[1]:
            rvalor1, gvalor1, bvalor1 = imagen9.getpixel ((i,j))
            rvalor2, gvalor2, bvalor2 = imagen10.getpixel ((i,j))
            rvaloraux1 = rvalor1 - rvalor2
            if rvaloraux1 <= 0:
                rvaloraux1 = 0
            else:
                rvaloraux1 = rvaloraux1
            gvaloraux1 = gvalor1 - gvalor2
            if gvaloraux1 <= 0:
                gvaloraux1 = 0
            else:
                gvaloraux1 = gvaloraux1
            bvaloraux1 = bvalor1 - bvalor2
            if bvaloraux1 <= 0:
                bvaloraux1 = 0
            else:
                bvaloraux1 = bvaloraux1
            pixel1 = tuple ([rvaloraux1,gvaloraux1,bvaloraux1])
            imagen9.putpixel((i,j),pixel1)
            rvaloraux2 = rvalor2 - rvalor1
            if rvaloraux2 <= 0:
                rvaloraux2 = 0
            else:
                rvaloraux2 = rvaloraux2
            gvaloraux2 = gvalor2 - gvalor1
            if gvaloraux2 <= 0:
                gvaloraux2 = 0
            else:
                gvaloraux2 = gvaloraux2
            bvaloraux2 = bvalor2 - bvalor1
            if bvaloraux2 <= 0:
                bvaloraux2 = 0
            else:
                bvaloraux2 = bvaloraux2
            pixel2 = tuple ([rvaloraux2,gvaloraux2,bvaloraux2])
            imagen10.putpixel((i,j),pixel2)
            j+=1
        i+=1
    imagen9.show()
    size = (imagen9.size[0],imagen9.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen9,(0,0))
    nueva.save("resta12.png")
    imagen10.show()
    size = (imagen10.size[0],imagen10.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen10,(0,0))
    nueva.save("resta21.png")
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

def restagris (imagen1,imagen2):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta1 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen1) #Concatena la ruta de la carpeta 
    imagen1 = Image.open(ruta1) #Para buscar la imagen"""
    imagen1.show()
    ruta2 = ("C:/Users/etsza/Desktop/Imagenes/" + imagen2) #Concatena la ruta de la carpeta 
    imagen2 = Image.open(ruta2) #Para buscar la imagen"""
    imagen2.show()
    imagen9 = imagen1
    imagen10 = imagen2
    i = 0
    while i < imagen9.size[0]:
        j = 0
        while j < imagen9.size[1]:
            rvalor1, gvalor1, bvalor1 = imagen9.getpixel ((i,j))
            rvalor2, gvalor2, bvalor2 = imagen10.getpixel ((i,j))
            valor1 = (rvalor1+gvalor1+bvalor1)/3
            valor2 = (rvalor2+gvalor2+bvalor2)/3
            valor1= int(valor1)
            valor2= int (valor2)
            valoraux1 = valor1 - valor2
            if valoraux1 <= 0:
                valoraux1 = 0
            else:
                valoraux1 = valoraux1
            pixel1 = tuple ([valoraux1,valoraux1,valoraux1])
            imagen9.putpixel((i,j),pixel1)
            valoraux2 = valor2 - valor1
            if valoraux2 <= 0:
                valoraux2 = 0
            else:
                valoraux2 = valoraux2
            
            pixel2 = tuple ([valoraux2,valoraux2,valoraux2])
            imagen10.putpixel((i,j),pixel2)
            j+=1
        i+=1
    imagen9.show()
    size = (imagen9.size[0],imagen9.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen9,(0,0))
    nueva.save("restag12.png")
    imagen10.show()
    size = (imagen10.size[0],imagen10.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen10,(0,0))
    nueva.save("restag21.png")
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def binarizacion (imagen,parametro):
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
    size = (imagen7.size[0],imagen7.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen7,(0,0))
    nueva.save("bin.png")
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def inverso_binarizacion (imagen,parametro):
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
    size = (imagen7.size[0],imagen7.size[1])
    nueva = Image.new('RGB',size,"white")
    nueva.paste(imagen7,(0,0))
    nueva.save("invbin.png")
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    
def AND(imagen, imagen2):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practicas/Practica1_2/" + imagen) #Concatena la ruta de la carpeta 
    ruta2 = ("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practicas/Practica1_2/" + imagen2) #Concatena la ruta de la carpeta 
    
    img1 = cv2.imread(imagen,0)
    img2 = cv2.imread(imagen2,0)
    img_bwa = cv2.bitwise_and(img1,img2)
    
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen2 = Image.open(ruta2) #Para buscar la imagen"""
    imagen2.show()
    cv2.imshow("Bitwise AND of Image 1 and 2", img_bwa)
    
    cv2.imwrite("C:/Users/etsza/Desktop/Imagenes/AND.png",img_bwa)
    cv2.waitKey(0)
    
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

def OR(imagen, imagen2):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practicas/Practica1_2/" + imagen) #Concatena la ruta de la carpeta 
    ruta2 = ("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practicas/Practica1_2/" + imagen2) #Concatena la ruta de la carpeta 
    
    img1 = cv2.imread(imagen,0)
    img2 = cv2.imread(imagen2,0)
    img_bwa = cv2.bitwise_or(img1,img2)
    
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen2 = Image.open(ruta2) #Para buscar la imagen"""
    imagen2.show()
    cv2.imshow("Bitwise OR of Image 1 and 2", img_bwa)
    
    cv2.imwrite("C:/Users/etsza/Desktop/Imagenes/OR.png",img_bwa)
    cv2.waitKey(0)
    
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")
    