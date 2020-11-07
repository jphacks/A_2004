# 各ソースコードの説明 h2
学習データを作成する際に作成使用したプログラムの概要を以下に示す.
* pdftojpg.py:in_pdf内のpdfデータを取得してout_imgにjpgとして出力する
* rename_image.py:指定ディレクトリ内の全ての画像データを連番でid付けする
* frip_img.py:指定したディレクトリの画像ファイルを全て上下反転、左右反転、中心を原点とした回転する
* image_crop.py:opencvにより画像内の文様部分を抜き出すプログラム(サイズは64x64推奨)
* image_crop_lib.py:image_crop.pyで使用している関数が置いてある
* image_proc:学習データの前処理を行う関数が置いてある
* look_size:画像データのサイズを確認できる
* square_size.py:長方形データを余白を補完して正方形データに変更
* togray.py:学習データをグレースケールに変更
* check_size.py:画像サイズが全て一致しているかを確認し不一致のものはサイズを変更

# 実行に必要なpythonライブラリ h2
* pip3 install numpy
* pip3 install pillow
* pip3 install pdf2image ※warningが出る可能性があるが無視して実行可能
* pip install opencv-python
* sudo apt install poppler-utils
上手くいかない場合はsudo apt --fix-broken installから行う

# pdf->jpgのデータセットの作成 h3
1. in_pdfに変換したいpdfを全ていれる
2. python3 pdftoimg.py
3. python3 image_proc.py->縦横サイズは基本的に64とし, 4種類の切り出し方によるデータがdatasetに保管される
4. (python3 frip_img.py)->入力したディレクトリ内の画像にfrip,mirror,rotateのコマンドで変化を加えて新たなディレクトリに格納する
5. (4で作成した全ての画像をdatasetに格納 mv ./ディレクトリ名/*.jpg ./dataset)
6. python3 rename_image.py->ディレクトリ名は基本的にはdatasetを指定