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
pip install torch==1.4.0 torchvision==0.5.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install flask
pip install future --upgrade
# 通信の設定 
sudo systemctl stop firewalld.service
sudo systemctl mask firewalld.service
sudo systemctl list-unit-files | grep firewalld