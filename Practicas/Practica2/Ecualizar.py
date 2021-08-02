# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:37:37 2020

@author: georg
"""
from PIL import Image, ImageOps
import numpy as np
from matplotlib import pyplot as plt

def Histograma(im):
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

if __name__ == "__main__":
    im = Image.open("bosque.jpg")
    im.show()
    ecualizada = ImageOps.equalize(im)
    ecualizada.show()
    Histograma(im)
    Histograma(ecualizada)
    ecualizada.save("eq.jpg")

