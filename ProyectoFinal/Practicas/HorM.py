import cv2 as cv
import numpy as np
input_image = np.array((
    [0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ],
    [0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ],
    [0  , 0  , 0  , 255, 0  , 255, 0  , 0  ],
    [0  , 0  , 255, 255, 255, 255, 255, 0  ],
    [0  , 0  , 0  , 255, 0  , 255, 0  , 0  ],
    [0  , 0  , 255, 255, 255, 255, 255, 0  ],
    [0  , 0  , 255, 255, 0  , 255, 0  , 0  ],
    [0  , 0  , 255, 0  , 0  , 0  , 0  , 0  ],
    [0  , 0  , 255, 0  , 0  , 0  , 0  , 0  ]), dtype="uint8")
rate = 50

kernel = np.array((
        [-1, 1,-1],
        [ 1, 1, 1],
        [-1, 1,-1]), dtype="int") #cruz
kernel1 = np.array((
        [ 0,-1, 0],
        [-1, 1,-1],
        [ 1, 1, 1]), dtype="int") #extremos
kernel2 = np.array((
        [ 1,-1, 0],
        [ 1, 1,-1],
        [ 1,-1, 0]), dtype="int") #extremos
kernel3 = np.array((
        [ 1, 1, 1],
        [-1, 1,-1],
        [ 0,-1, 0]), dtype="int") #extremos
kernel4 = np.array((
        [ 0,-1, 1],
        [-1, 1, 1],
        [ 0,-1, 1]), dtype="int") #extremos
kernel5 = np.array((
        [ 1,-1, 1],
        [ 1, 1, 1],
        [ 1,-1, 1]), dtype="int") #uniones
kernel6 = np.array((
        [ 1, 1, 1],
        [-1, 1,-1],
        [ 1, 1, 1]), dtype="int") #uniones

output_image = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel)
output_image1 = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel1)
output_image2 = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel2)
output_image3 = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel3)
output_image4 = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel4)
output_image5 = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel5)
output_image6 = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel6)

input_image = cv.resize(input_image, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image = cv.resize(output_image, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image1 = cv.resize(output_image1, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image2 = cv.resize(output_image2, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image3 = cv.resize(output_image3, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image4 = cv.resize(output_image4, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image5 = cv.resize(output_image5, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
output_image6 = cv.resize(output_image6, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)


dst = cv.add(output_image, output_image1)
dst = cv.add(dst, output_image2)
dst = cv.add(dst, output_image3)
dst = cv.add(dst, output_image4)
dst = cv.add(dst, output_image5)
dst = cv.add(dst, output_image6)

cv.imshow("Original", input_image)
cv.imshow('dst',dst)

cv.waitKey(0)
cv.destroyAllWindows()