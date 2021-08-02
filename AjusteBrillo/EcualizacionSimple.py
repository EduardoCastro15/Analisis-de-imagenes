from PIL import Image

def ecualizar(imagen):
    tiempo_de_inicio = time.time() # Cuenta los segundos de ejecucion"""
    ruta = ("C:/Users/georg/Desktop/ESCOM/6to. Semestre/AnalisisImagenes/Practica1/" + imagen) #Concatena la ruta de la carpeta
    imagen = Image.open(ruta) #Para buscar la imagen"""
    imagen.show()
    imagen3 = imagen
    i = 0
    while i < imagen3.size[0]:
        j = 0
        while j < imagen3.size[1]:
            minimo = min(imagen3.getpixel((i,j)))
            maximo = max(imagen3.getpixel((i,j)))
            origenr, origeng, origenb = imagen3.getpixel((i,j))
            finalr = (maximo - minimo) * origenr - minimo
            finalg = (maximo - minimo) * origeng - minimo
            finalb = (maximo - minimo) * origenb - minimo
            final = (finalr + finalg + finalb) / 3
            final = int (final)
            pixel = tuple ([final,final,final])
            imagen3.putpixel((i,j), pixel)
        j+=1
        i+=1
    imagen3.show()
    print("El nivel maximo de gris es: ", maximo)
    tiempo_de_terminacion = time.time() #Marca la finalizacion del programa"""
    print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")