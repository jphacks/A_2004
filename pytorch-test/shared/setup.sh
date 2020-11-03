sudo dpkg --configure -a
sudo apt install python3-pip
sudo apt install python-pip
sudo apt update
sudo pip install --upgrade pip
pip3 install numpy
pip3 install Click==7.0
pip3 install Flask==1.1.1
pip3 install itsdangerous==1.1.0
pip3 install Jinja2==2.10.3
pip3 install MarkupSafe==1.1.1
pip3 install Werkzeug==0.16.0
pip3 install gunicorn==19.10.0
pip3 install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip3 install flask
pip3 install datetime
pip3 install future --upgrade
# 通信の設定 
sudo systemctl stop firewalld.service
sudo systemctl mask firewalld.service
sudo systemctl list-unit-files | grep firewalld
# pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
# pip install torch==1.4.0+cpu
# pip install torchvision==0.5.0+cpu
#meno