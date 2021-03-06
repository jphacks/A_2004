import numpy as np
import PIL
import pathlib
import pdf2image
#import rename_image

#image_size = input("生成画像のサイズ>")

pdf_files = pathlib.Path('in_pdf').glob('*.pdf')
img_dir = pathlib.Path('out_img')

for pdf_file in pdf_files:
    base = pdf_file.stem
    print(pdf_file)
    images = pdf2image.convert_from_path(pdf_file,dpi=160)
    for index, image in enumerate(images):
        #print(image.stem)
        print(index)
        image.save(img_dir/pathlib.Path(base + '-{}.jpg'.format(index + 1)),'jpeg')

#rename_image.rename_img()