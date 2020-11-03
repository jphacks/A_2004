# -*- coding: utf-8 -*-

import torch
from torch import nn, optim
from torchvision.utils import save_image
from torch.utils.data import Dataset, DataLoader, TensorDataset
from torchvision import transforms, datasets
import tqdm
from statistics import mean
import statistics

### データの読み込み ###
# datasetrの準備
dataset = datasets.ImageFolder("sample-data/",
    transform=transforms.Compose([
        transforms.ToTensor()
]))

batch_size = 64

# dataloaderの準備
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

### Generatorの作成 ###
class Generator(nn.Module):
    def __init__(self):
        super(Generator,self).__init__()
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


### Discriminatorの作成 ###
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator,self).__init__()
        self.main = nn.Sequential(

            nn.Conv2d(3, 32, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(32, 64, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(64, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(128, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(256, 1, 4, 1, 0, bias=False),
        )

    def forward(self, x):
        return self.main(x).squeeze()

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('using device:', device)

### 訓練関数の作成 ###
model_G = Generator().to(device)
model_D = Discriminator().to(device)

params_G = optim.Adam(model_G.parameters(),
    lr=0.0002, betas=(0.5, 0.999))
params_D = optim.Adam(model_D.parameters(),
    lr=0.0002, betas=(0.5, 0.999))

# 潜在特徴100次元ベクトルz
nz = 100

# ロスを計算するときのラベル変数
ones = torch.ones(batch_size).to(device) # 正例 1
zeros = torch.zeros(batch_size).to(device) # 負例 0
loss_f = nn.BCEWithLogitsLoss()

# 途中結果の確認用の潜在特徴z
check_z = torch.randn(batch_size, nz, 1, 1).to(device)

# エラー推移
result = {}
result["log_loss_G"] = []
result["log_loss_D"] = []

# 訓練関数
def train_dcgan(model_G, model_D, params_G, params_D, data_loader):
    log_loss_G, log_loss_D = [], []
    for real_img, _ in tqdm.tqdm(data_loader):
        batch_len = len(real_img)


        # == Generatorの訓練 ==
        # 偽画像を生成
        z = torch.randn(batch_len, nz, 1, 1).to(device)
        fake_img = model_G(z)

        # 偽画像の値を一時的に保存 => 注(１)
        fake_img_tensor = fake_img.detach()

        # 偽画像を実画像（ラベル１）と騙せるようにロスを計算
        out = model_D(fake_img)
        loss_G = loss_f(out, ones[: batch_len])
        log_loss_G.append(loss_G.item())

        # 微分計算・重み更新 => 注（２）
        model_D.zero_grad()
        model_G.zero_grad()
        loss_G.backward()
        params_G.step()


        # == Discriminatorの訓練 ==
        # sample_dataの実画像
        real_img = real_img.to(device)

        # 実画像を実画像（ラベル１）と識別できるようにロスを計算
        real_out = model_D(real_img)
        loss_D_real = loss_f(real_out, ones[: batch_len])

        # 計算省略 => 注（１）
        fake_img = fake_img_tensor

        # 偽画像を偽画像（ラベル０）と識別できるようにロスを計算
        fake_out = model_D(fake_img_tensor)
        loss_D_fake = loss_f(fake_out, zeros[: batch_len])

        # 実画像と偽画像のロスを合計
        loss_D = loss_D_real + loss_D_fake
        log_loss_D.append(loss_D.item())

        # 微分計算・重み更新 => 注（２）
        model_D.zero_grad()
        model_G.zero_grad()
        loss_D.backward()
        params_D.step()

    result["log_loss_G"].append(statistics.mean(log_loss_G))
    result["log_loss_D"].append(statistics.mean(log_loss_D))
    print("log_loss_G =", result["log_loss_G"][-1], ", log_loss_D =", result["log_loss_D"][-1])

    return mean(log_loss_G), mean(log_loss_D)

### DCGANの訓練スタート ###
for epoch in range(20):
    train_dcgan(model_G, model_D, params_G, params_D, data_loader)
    
    # 訓練途中のモデル・生成画像の保存
    if epoch % 10 == 0:
        torch.save(
            model_G.state_dict(),
            "Weight_Generator/G_{:03d}.pth".format(epoch),
            pickle_protocol=2)
        torch.save(
            model_D.state_dict(),
            "Weight_Discriminator/D_{:03d}.pth".format(epoch),
            pickle_protocol=2)

        generated_img = model_G(check_z)
        save_image(generated_img,"Generated_Image/{:03d}.jpg".format(epoch))

make_file_num = 1
z = torch.randn(make_file_num, nz, 1, 1).to(device)
fake_img = model_G(z)
save_image(fake_img,"gen.jpg")
