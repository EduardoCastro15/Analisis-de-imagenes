# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:27:14 2020

@author: georg
"""
from PIL import Image
import time
import numpy as np
from matplotlib import pyplot as plt

def histograma(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/CkriZz/Pictures/" + im)
    im = Image.open(ruta)
    im.show()
    im = im.convert('L')
    im9 = im
    [ren, col] = im9.size
    total = ren * col
    a = np.asarray(im9, dtype = np.float32)
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
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')