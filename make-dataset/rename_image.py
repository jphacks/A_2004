from pathlib import Path
import os
import re

def rename_img():
    p = Path("./out_img")
    files = sorted(p.glob("*"))#./out_img内のすべての画像をリストに取得

    i=0
    for file in files:
        zero_i = "{0:04d}".format(i)#4桁にそろえる
        new_name = zero_i + ".jpg"
        os.rename(file, "./out_img/" + new_name)
        # 状況を報告
        print(file,"→",new_name)
        i += 1