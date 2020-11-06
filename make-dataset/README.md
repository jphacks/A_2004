pdftojpg.py:in_pdf内のpdfデータを取得してout_imgにjpgとして出力する
rename_image.py:out_img内の全ての画像データを4桁の連番でid付けする
frip_img.py:指定したディレクトリの画像ファイルを全て上下反転、左右反転、中心を原点とした回転する
image_crop.py:opencvにより画像内の文様部分を抜き出すプログラム(64x64推奨)
実行に必要なpythonライブラリ
    pip3 install numpy
    pip3 install pillow
    pip3 install pdf2image ※warningが出る可能性があるが無視して実行可能
    pip install opencv-python
    sudo apt install poppler-utils
        上手くいかない場合はsudo apt --fix-broken installから行う

pdf->jpgのデータセットを作る一連の流れ
    1.in_pdfに変換したいpdfを全ていれる
    2.python3 pdftoimg.py
        ->サイズを聞かれるが200~300付近がおすすめ
    3.python3 image_proc.py
        ->縦横サイズは基本的に64とし、4種類の切り出し方によるデータがdatasetに保管される
    (4.python3 frip_img.py)
        ->入力したディレクトリ内の画像にfrip,mirror,rotateのコマンドで変化を加えて新たなディレクトリに格納する
    (5.4で作成した全ての画像をdatasetに格納 mv ./ディレクトリ名/*.jpg ./dataset)
    6.python3 rename_image.py
        ->ディレクトリ名は基本的にはdatasetを指定