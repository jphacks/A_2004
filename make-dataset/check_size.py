import cv2
import glob

size = input("チェックサイズ> ")
size = int(size)

files = glob.glob("./dataset/*.jpg")
for i, filename in enumerate(files):
    img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    if height != size or width != size:
        print("MISS SIZE ",filename)
        img2 = cv2.resize(img, (size, size),interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, img2)

print("checked.")