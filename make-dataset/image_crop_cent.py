import cv2
import numpy as np
import os
import image_proc

#切り抜きサイズの指定
size_y = input("切り抜く領域の縦サイズを指定> ")
size_x = input("切り抜く領域の横サイズを指定> ")

files = os.listdir("./out_img")
count = len(files)
print(count)

for data_num in range(1,count+1):
    #画像の読み込み
    img = cv2.imread("./out_img/{}.jpg".format(data_num))

    #画像の大きさを取得
    height,width,channels = img.shape[:3]
    #print("[",height,",",width,"]")

    cent_y = int(0.25*int(size_y))
    cent_x = int(0.25*int(size_x))
    img_crop = img[cent_y:cent_y+int(size_y),cent_x:cent_x+int(size_x),:]
    cv2.imwrite("./dataset/{}.jpg".format(data_num),img_crop)

    print("cropped ",data_num,".jpg")