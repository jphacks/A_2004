import cv2
import glob

files = glob.glob("*.jpg")
for i, filename in enumerate(files):
    img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    width = 200
    height = 200
    img2 = cv2.resize(img, (width, height))
    cv2.imwrite(filename, img2)

print("resized.")