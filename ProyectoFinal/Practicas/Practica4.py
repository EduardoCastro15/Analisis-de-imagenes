import sys
from PIL import Image, ImageFilter

def detector_bordes(tipo):

    if tipo == 1: #Prewitt

        factor = 6

        coeficientes_h = [ 1,  0, -1,
                           1,  0, -1, 
                           1,  0, -1]
        coeficientes_v = [-1, -1, -1, 
                           0,  0,  0, 
                           1,  1,  1]

        #coeficientes con signo contrario
        coeficientes_h1 = [-1,  0,  1,
                           -1,  0,  1, 
                           -1,  0,  1]
        coeficientes_v1 = [ 1,  1,  1, 
                            0,  0,  0, 
                           -1, -1, -1]

    elif tipo == 2: #Sobel
 
        factor = 8

        coeficientes_h = [ 1,  0, -1, 
                           2,  0, -2, 
                           1,  0, -1]
        coeficientes_v = [-1, -2, -1, 
                           0,  0,  0, 
                           1,  2,  1]

        #coeficientes con signo contrario
        coeficientes_h1 = [-1,  0,  1, 
                           -2,  0,  2, 
                           -1,  0,  1]
        coeficientes_v1 = [ 1,  2,  1, 
                            0,  0,  0, 
                           -1, -2, -1]

    elif tipo == 3: #Roberts
 
        factor = 2

        coeficientes_h = [ 0,  0, -1,
                           0,  1,  0, 
                           0,  0,  0]
        coeficientes_v = [-1,  0,  0, 
                           0,  1,  0, 
                           0,  0,  0]

        #coeficientes con signo contrario
        coeficientes_h1 = [ 0,  0,  1,
                            0, -1,  0, 
                            0,  0,  0]
        coeficientes_v1 = [ 1,  0,  0, 
                            0, -1,  0, 
                            0,  0,  0]

    else:
        #en caso de no introducir el nombre correctamente se cierra el script
        sys.exit(0)

    datos_h = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_h, factor)).getdata()
    datos_v = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_v, factor)).getdata()

    datos= []
  

    for x in range(len(datos_h)):
 
        datos.append(round(((datos_h[x] ** 2) + (datos_v[x] ** 2)) ** 0.5))

    datos_h = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_h1, factor)).getdata()
    datos_v = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_v1, factor)).getdata()
 
    datos_signo_contrario = []
 
 
    for x in range(len(datos_h)):
 
        datos_signo_contrario.append(round(((datos_h[x] ** 2) + (datos_v[x] ** 2)) ** 0.5))

   
    datos_bordes = []
 

    for x in range(len(datos_h)):
 
        datos_bordes.append(datos[x] + datos_signo_contrario[x])

    return datos_bordes 

if __name__ == "__main__":
    nombre = input("Ingresa el nombre de la imagen + extension: ")
    opc = int(input('''
        Menu principal:
            1. Aplicar filtro Prewitt
            2. Aplicar filtro Sobel
            3. Aplicar filtro Roberts
        Selecciona alguna de las opciones anteriores: '''))
    
    imagen = Image.open(nombre).convert('L')
    nueva_imagen = Image.new('L', imagen.size)
    if(opc==1):
        datos_bordes = detector_bordes(1) 
        nueva_imagen.putdata(datos_bordes)
        nueva_imagen.save('Prewitt.jpg')
    elif(opc==2):
        datos_bordes = detector_bordes(2) 
        nueva_imagen.putdata(datos_bordes)
        nueva_imagen.save('Sobel.jpg')
    elif(opc==3):
        datos_bordes = detector_bordes(3) 
        nueva_imagen.putdata(datos_bordes)
        nueva_imagen.save('Roberts.jpg')
    
    nueva_imagen.show()
    
    imagen.close()
    nueva_imagen.close()
