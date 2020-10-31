sudo dpkg --configure -a
sudo apt install python3-pip
sudo apt install python-pip
sudo apt update
sudo pip install --upgrade pip
pip install numpy
pip install Click==7.0
pip install Flask==1.1.1
pip install itsdangerous==1.1.0
pip install Jinja2==2.10.3
pip install MarkupSafe==1.1.1
pip install Werkzeug==0.16.0
pip install gunicorn==19.10.0
pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip install flask
pip install future --upgrade
# 通信の設定 
sudo systemctl stop firewalld.service
sudo systemctl mask firewalld.service
sudo systemctl list-unit-files | grep firewalld
# pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
# pip install torch==1.4.0+cpu
# pip install torchvision==0.5.0+cpu