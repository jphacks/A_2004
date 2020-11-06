import cv2
import numpy as np
import os
import image_proc
import pathlib
import image_crop_lib

#切り抜きサイズの指定
size_y = input("切り抜く領域の縦サイズを指定> ")
size_x = input("切り抜く領域の横サイズを指定> ")

#num = input("切り取り方を1~4で選択> ")
jpg_files = pathlib.Path('out_img').glob('*.jpg')

print("now cropping")
for jpg_file in jpg_files:
    base = jpg_file.stem
    img = cv2.imread("./out_img/{}.jpg".format(base))
    img_gray = cv2.imread("./out_img/{}.jpg".format(base))
    #画像を2値化
    image_proc.binary_threshold(img_gray)
    #if num == '1':
    image_crop_lib.crop_left(size_y,size_x,img,img_gray,base)
    #elif num == '2':
    image_crop_lib.crop_right(size_y,size_x,img,img_gray,base)
    #elif num == '3':
    image_crop_lib.crop_left_upper(size_y,size_x,img,img_gray,base)
    #else:
    image_crop_lib.crop_right_upper(size_y,size_x,img,img_gray,base)
print("cropped")