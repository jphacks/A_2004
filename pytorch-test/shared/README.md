sharedフォルダは仮想環境vagrantで立ち上げたサーバー内で使用できる共有フォルダです.

# 各ディレクトリの役割 h2
* deep:訓練用のDCGANモデルを置いてあるディレクトリ
* model_parameter:DCGANにより学習したモデルのpthファイルを置くディレクトリ
* static/png:webサイトに使用している画像を置くディレクトリ
* static/js:webサイトのアニメーションを動作させるファイルが置いてある
* static/out:生成した64枚の画像を置くディレクトリ
* templates/webサイトを構成するhtmlファイルを置くディレクトリ

# 各ファイルの役割 h2
* app.py:サーバーを立ててwebページの設定を行うpythonコード
* models_dcgan.py:学習モデルを読み込み起動する関数を書いたpythonコード
* setup.sh:仮想環境内の開発環境を設定するシェルスクリプト