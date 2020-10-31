from PIL import Image,ImageOps
import random
import glob
import os
import os.path

dir_name = input('画像ファイルのあるディレクトリの名前> ')
Image_path_list = glob.glob('./{}/*.*'.format(dir_name))
#print(Image_path_list)
while True:
    command = input('{}フォルダ内にある画像に行う操作> '.format(dir_name))
    if 'help' in command:
        print('frip,mirror,rotateのどれかを命令してください')
    elif command == 'frip' or command == 'mirror' or command == 'rotate':
        break
    elif command == 'rotate':
        angle = input('回転する角度> ')
        if angle in 'random':
            angle = random.randrange(360)
        break

try:
    if os.path.isdir('./{}_{}'.format(command,dir_name)) == False:
        os.mkdir('./{}_{}'.format(command,dir_name))

    angle = 0
    for image_path in Image_path_list:
        Imag = Image.open(image_path)
        if command in 'frip':
            Imag_change = ImageOps.flip(Imag)
            Imag_change.save('./{}_{}/{}_{}'.format(command,dir_name,command,image_path.split('/')[-1]))
        elif command in 'mirror':
            Imag_change = ImageOps.mirror(Imag)
            Imag_change.save('./{}_{}/{}_{}'.format(command,dir_name,command,image_path.split('/')[-1]))
        elif command in 'rotate':
            if angle == 0:
                angle = input('回転する角度> ')
                if angle in 'random':
                    angle = random.randrange(1,360)
            Imag_change = Imag.rotate(int(angle),expand=True)
            Imag_change.save('./{}_{}/{}_{}'.format(command,dir_name,command,image_path.split('/')[-1]))

except Exception as e:
    print('予期せぬエラーが発生しました')
    print('エラー内容:',e)