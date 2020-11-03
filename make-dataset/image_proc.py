import cv2
import numpy as np

def binary_threshold(img):
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #画像の２値化
    under_thresh = 220 #この値より明るい画素(背景)を白にするパラメータ
    maxValue = 255
    th, drop_back = cv2.threshold(grayed, under_thresh, maxValue, cv2.THRESH_BINARY)
    morphed = morph(drop_back)
    return morphed

#画像を平滑化する関数
def morph(img):
    kernel = np.ones((3, 3),np.uint8)
    m = cv2.GaussianBlur(img, (3, 3), 0)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, kernel, iterations=2)
    m = cv2.GaussianBlur(m, (5, 5), 0)
    return m

#img = cv2.imread("./out_img/129.jpg")
#img2 = binary_threshold(img)
#cv2.imwrite("./test.jpg",img2)