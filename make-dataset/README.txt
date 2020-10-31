pdftojpg.py:in_pdf内のpdfデータを取得してout_imgにjpgとして出力する
rename_image.py:out_img内の全ての画像データを4桁の連番でid付けする
frip_img.py:指定したディレクトリの画像ファイルを全て上下反転、左右反転、中心を原点とした回転する
実行に必要なpythonライブラリ
    pip3 install numpy
    pip3 install pillow
    pip3 install pdf2image ※warningが出る可能性があるが無視して実行可能
    sudo apt install poppler-utils
        上手くいかない場合はsudo apt --fix-broken installから行う