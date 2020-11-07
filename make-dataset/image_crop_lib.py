import cv2
import numpy as np
import os
import image_proc
import pathlib

def crop_left(size_y,size_x,img,img_gray,base):
    #画像の大きさを取得
    height,width,channels = img.shape[:3]
    #print("[",height,",",width,"]")

    #最下部付近に文様はないと仮定
    for i_height in range(int(height*0.8),int(height*0.5),-1):
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
                    cv2.imwrite("./dataset/{}-left.jpg".format(base),img_crop)
                except:
                    cent_y = int(0.25*int(size_y))
                    cent_x = int(0.25*int(size_x))
                    img_crop = img[cent_y:cent_y+int(size_y),cent_x:cent_x+int(size_x),:]
                    cv2.imwrite("./dataset/{}-left.jpg".format(base),img_crop)
                    #print("error!")
                #print("saved!")
                break
        else:
            continue
        break

def crop_right(size_y,size_x,img,img_gray,base):
    #画像の大きさを取得
    height,width,channels = img.shape[:3]
    #print("[",height,",",width,"]")

    #最下部付近に文様はないと仮定
    for i_height in range(int(height*0.8),int(height*0.5),-1):
        #中心より左側で切り取らないようにする
        for i_width in range(int(width*0.8),int(width/2),-1):
            #print(i_height,",",i_width)
            pixel_color = img_gray[i_height,i_width]
            #print(pixel_color)
            color_ave = (int(pixel_color[0])+int(pixel_color[1])+int(pixel_color[2]))/3
            #print(color_ave)
            #背景(白)でないならそこからsize*sizeでcrop
            if color_ave < 220:
                img_crop = img[i_height-int(size_y):i_height,i_width-int(size_x):i_width,:]
                try:
                    cv2.imwrite("./dataset/{}-right.jpg".format(base),img_crop)
                except:
                    cent_y = int(0.25*int(size_y))
                    cent_x = int(0.25*int(size_x))
                    img_crop = img[cent_y:cent_y+int(size_y),cent_x:cent_x+int(size_x),:]
                    cv2.imwrite("./dataset/{}-right.jpg".format(base),img_crop)
                    #print("error!")
                #print("saved!")
                break
        else:
            continue
        break

def crop_left_upper(size_y,size_x,img,img_gray,base):
    #画像の大きさを取得
    height,width,channels = img.shape[:3]
    #print("[",height,",",width,"]")

    #最上部付近に文様はないと仮定
    for i_height in range(int(height*0.2),int(height*0.5)):
        #中心より右側で切り取らないようにする
        for i_width in range(int(width/5),int(width/2)):
            #print(i_height,",",i_width)
            pixel_color = img_gray[i_height,i_width]
            #print(pixel_color)
            color_ave = (int(pixel_color[0])+int(pixel_color[1])+int(pixel_color[2]))/3
            #print(color_ave)
            #背景(白)でないならそこからsize*sizeでcrop
            if color_ave < 220:
                img_crop = img[i_height:i_height+int(size_y),i_width:i_width+int(size_x),:]
                try:
                    cv2.imwrite("./dataset/{}-left-upper.jpg".format(base),img_crop)
                except:
                    cent_y = int(0.25*int(size_y))
                    cent_x = int(0.25*int(size_x))
                    img_crop = img[cent_y:cent_y+int(size_y),cent_x:cent_x+int(size_x),:]
                    cv2.imwrite("./dataset/{}-left-upper.jpg".format(base),img_crop)
                    #print("error!")
                #print("saved!")
                break
        else:
            continue
        break

def crop_right_upper(size_y,size_x,img,img_gray,base):
    #画像の大きさを取得
    height,width,channels = img.shape[:3]
    #print("[",height,",",width,"]")

    #最上部付近に文様はないと仮定
    for i_height in range(int(height*0.2),int(height*0.5)):
        #中心より左側で切り取らないようにする
        for i_width in range(int(width*0.8),int(width/2),-1):
            #print(i_height,",",i_width)
            pixel_color = img_gray[i_height,i_width]
            #print(pixel_color)
            color_ave = (int(pixel_color[0])+int(pixel_color[1])+int(pixel_color[2]))/3
            #print(color_ave)
            #背景(白)でないならそこからsize*sizeでcrop
            if color_ave < 220:
                img_crop = img[i_height:i_height+int(size_y),i_width-int(size_x):i_width,:]
                try:
                    cv2.imwrite("./dataset/{}-right-upper.jpg".format(base),img_crop)
                except:
                    cent_y = int(0.25*int(size_y))
                    cent_x = int(0.25*int(size_x))
                    img_crop = img[cent_y:cent_y+int(size_y),cent_x:cent_x+int(size_x),:]
                    cv2.imwrite("./dataset/{}-right-upper.jpg".format(base),img_crop)
                    #print("error!")
                #print("saved!")
                break
        else:
            continue
        break