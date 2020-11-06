import cv2
import numpy as np
import os

im_name = input("画像名>")
img = cv2.imread("./out_img/{}.jpg".format(im_name))

#画像の大きさを取得
height,width,channels = img.shape[:3]
print("[",height,",",width,"]")