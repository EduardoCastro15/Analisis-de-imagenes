from PIL import Image

def abrir_imagen(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen)
    imagen.show()
    
def escala_de_grises(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen)
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
    
def escala_de_grises_max(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
    imagen.show()
    imagen3 = imagen
    i = 0
    while i < imagen3.size[0]:
        j = 0
        while j < imagen3.size[1]:
            maximo = max(imagen3.getpixel((i,j)))
            pixel = tuple ([maximo,maximo,maximo])
            imagen3.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen3.show()
    print("El nivel maximo de gris es: ", maximo)
    
def escala_de_grises_min(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
    imagen.show()
    imagen4 = imagen
    i = 0
    while i < imagen4.size[0]:
        j = 0
        while j < imagen4.size[1]:
            minimo = min(imagen4.getpixel((i,j)))
            pixel = tuple ([minimo,minimo,minimo])
            imagen4.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen4.show()
    print("El nivel minimo de gris es: ", minimo)
    
def negativo_color(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
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
    
def negativo_gris(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
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

def blanco_negro (imagen,parametro):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
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
    
def rojo(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
    imagen.show()
    imagen8 = imagen
    i = 0
    while i < imagen8.size[0]:
        j = 0
        while j < imagen8.size[1]:
            r, g, b = imagen8.getpixel((i,j))
            rojo = int (r)
            pixel = tuple ([rojo,0,0])
            imagen8.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen8.show()
    
def verde(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
    imagen.show()
    imagen8 = imagen
    i = 0
    while i < imagen8.size[0]:
        j = 0
        while j < imagen8.size[1]:
            r, g, b = imagen8.getpixel((i,j))
            verde = int (g)
            pixel = tuple ([0,verde,0])
            imagen8.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen8.show()
    
def azul(imagen):
    imagen = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Para buscar la imagen"""
    imagen.show()
    imagen8 = imagen
    i = 0
    while i < imagen8.size[0]:
        j = 0
        while j < imagen8.size[1]:
            r, g, b = imagen8.getpixel((i,j))
            azul = int (b)
            pixel = tuple ([0,0,azul])
            imagen8.putpixel((i,j), pixel)
            j+=1
        i+=1
    imagen8.show()
    
def sumacolor(imagen1,imagen2):
    imagen1 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen1) #Para buscar la imagen"""
    imagen1.show()
    imagen2 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen2) #Para buscar la imagen"""
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
    imagen10.show()

def sumagris (imagen1,imagen2):
    imagen1 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen1) #Para buscar la imagen"""
    imagen1.show()
    imagen2 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen2) #Para buscar la imagen"""
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
            valoraux2 = valor2 + valor1
            if valoraux2 >= 255:
                valoraux2 = 255
            else:
                valoraux2 = valoraux2
            
            pixel2 = tuple ([valoraux2,valoraux2,valoraux2])
            imagen10.putpixel((i,j),pixel2)
            j+=1
        i+=1
    imagen9.show()
    imagen10.show()
    
def restacolor (imagen1,imagen2):
    imagen1 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen1) #Para buscar la imagen"""
    imagen1.show()
    imagen2 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen2) #Para buscar la imagen"""
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
    imagen10.show()

def restagris (imagen1,imagen2):
    imagen1 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen1) #Para buscar la imagen"""
    imagen1.show()
    imagen2 = Image.open("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen2) #Para buscar la imagen"""
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
    imagen10.show()
    