from PIL import Image
from pathlib import Path
import os

#im = Image.open('./data/src')
dir = input("画像をナンバリングしたいディレクトリ名> ")
p = Path("./{}".format(dir))
files = sorted(p.glob("*"))

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

for filename in files:
    im = Image.open(filename)
    im_new = expand2square(im, (255, 255, 255))
    im_new.save('./{}/{}.jpg'.format(dir,(str(filename).split('/')[1]).split('.')[0]), quality=95)