# -*- coding: utf-8 -*-
# The class containing the model
# import torch
# from PIL import Image
# from torchvision import transforms
import torch
from torch import nn, optim
from torchvision.utils import save_image
from torch.utils.data import Dataset, DataLoader, TensorDataset
from torchvision import transforms, datasets
import tqdm
from statistics import mean
import statistics
from PIL import Image
from torchvision import transforms
import datetime
import time

def test(flag):
    # str_test = "hello2"
    # 潜在特徴100次元ベクトルz
    nz = 100
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    # print('using device:', device)
    # シード値の決定
    dt_now = int(time.time())
    
    torch.manual_seed(dt_now)
    torch.cuda.manual_seed(dt_now)
    ### 訓練関数の作成 ###
    # print("訓練関数の作成")
    model_G = Generator().to(device)
    make_file_num = 64
    z = torch.randn(make_file_num, nz, 1, 1).to(device)
    if flag == 0:
        model_path = 'model_parameter/G_0770.pth'
        print("Load model: " + model_path)
    elif flag == 1:
        model_path = 'model_parameter/G_0100.pth'
        print("Load model: " + model_path)
    else:
        print("Error")
    model_G.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    fake_img = model_G(z)
    for index in range(0,make_file_num):
        # dt_now = datetime.datetime.now()
        # timestamp = str(dt_now).replace('.', "")
        # timestamp = str(dt_now).strip()
        #timestamp = str(dt_now).replace(' ','_')
        #timestamp = timestamp.replace(':','_')
        #timestamp = timestamp.replace('.','')
        # timestamp = str(dt_now).replace(' ', '')
        #print(timestamp)
        #filename = str(timestamp) + ".jpg"
        filename = str(index) + ".jpg"
        filename_path = "static/out/" + filename
        returen_filename_path = "out/" + filename
        # print("save file name: " + filename)
        save_image(fake_img[index],filename_path)
    # print(type(fake_img))

    # return fake_img
    # return returen_filename_path

### Generatorの作成 ###
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.main = nn.Sequential(

            nn.ConvTranspose2d(100, 256, 4, 1, 0, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),

            nn.ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),

            nn.ConvTranspose2d(128, 64, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),

            nn.ConvTranspose2d(64, 32, 4, 2, 1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),

            nn.ConvTranspose2d(32, 3, 4, 2, 1, bias=False),
            nn.Tanh()
        )

    def forward(self, x):
        return self.main(x)