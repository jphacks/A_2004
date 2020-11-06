from pathlib import Path
import os
import re

dir = input("画像をナンバリングしたいディレクトリ名> ")
p = Path("./{}".format(dir))
files = sorted(p.glob("*"))#./out_img内のすべての画像をリストに取得

i=0
for file in files:
    zero_i = i#4桁にそろえる
    new_name = str(zero_i) + ".jpg"
    os.rename(file, "./{}/".format(dir) + new_name)
    # 状況を報告
    print(file,"→",new_name)
    i += 1