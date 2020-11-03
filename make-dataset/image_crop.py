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
    img_gray = cv2.imread("./out_img/{}.jpg".format(data_num))

    #画像を2値化
    image_proc.binary_threshold(img_gray)

    #画像の大きさを取得
    height,width,channels = img.shape[:3]
    #print("[",height,",",width,"]")

    #最下部付近に文様はないと仮定
    for i_height in range(int(height*0.75),0,-1):
        #中心より右側で切り取らないようにする
        for i_width in range(int(width/5),int(width/2)):
            #print(i_height,",",i_width)
            pixel_color = img_gray[i_height,i_width]
            #print(pixel_color)
            color_ave = (int(pixel_color[0])+int(pixel_color[1])+int(pixel_color[2]))/3
            #print(color_ave)
            #背景(白)でないならそこからsize*sizeでcrop
            if color_ave < 220:
                img_crop = img[i_height-int(size_y):i_height,i_width:i_width+int(size_x),:]
                try:
                    cv2.imwrite("./dataset/{}.jpg".format(data_num),img_crop)
                except:
                    cent_y = int(0.25*int(size_y))
                    cent_x = int(0.25*int(size_x))
                    img_crop = img[cent_y:cent_y+int(size_y),cent_x:cent_x+int(size_x),:]
                    cv2.imwrite("./dataset/{}.jpg".format(data_num),img_crop)
                    #print("error!")
                #print("saved!")
                break
        else:
            continue
        break
    
    print("cropped ",data_num,".jpg")