import sys
import cv2
import numpy
import pathlib

gamma22LUT = numpy.array([pow(x/255.0 , 2.2) for x in range(256)],dtype='float32')
jpg_files = pathlib.Path('dataset').glob('*.jpg')
#print(jpg_files)
for jpg in jpg_files:
    img = cv2.imread("./dataset/" + jpg.stem + ".jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("./dataset/" + jpg.stem + ".jpg", gray)