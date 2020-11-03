# -*- coding: utf-8 -*-

import os
import argparse

from networks import Generator

import numpy as np
from tqdm import tqdm
import torch
from torchvision.utils import save_image


def generate(latents, model_G, width, height, save_path):
    print("Generate")
    print(len(latents))
    assert len(latents) == width * height
    pred_images = model_G(latents)
    save_image(pred_images, save_path, nrow=width)

def generate_process(opt):
    print("generate_process")
    # ----- Device Setting -----
    device = torch.device("cpu")

    # ----- Output Setting -----

    img_output_dir = opt.output_dir
    if not os.path.exists(img_output_dir):
        os.mkdir(img_output_dir)

    if not os.path.exists(os.path.join(img_output_dir, "images")):
        os.mkdir(os.path.join(img_output_dir, "images"))

    if opt.save_latent is True:
        if not os.path.exists(os.path.join(img_output_dir, "latents")):
            os.mkdir(os.path.join(img_output_dir, "latents"))

    print("Output :", img_output_dir)

    # ----- Model Loading -----
    print("Use model :", opt.model)
    model_g = Generator()
    model_g.load_state_dict(torch.load(opt.model, map_location="cpu"))
    model_g.to(device)

    model_g.eval()

    if opt.mode == "normal":
        latents = [torch.randn(size=(opt.width * opt.height, opt.latent_size, 1, 1)) for i in range(opt.n_img)]
        # latents = [torch.randn(size=(opt.width * opt.height, opt.latent_size, 1, 1)]

    elif opt.mode == "use_latent":
        assert opt.latent_dir != "None", "latent source directory is not set"
        latent_paths = [os.path.join(opt.latent_dir, name) for name in os.listdir(opt.latent_dir)]
        latents = [torch.from_numpy(np.load(path)) for path in latent_paths]

    elif opt.mode == "inter":
        latent_start = torch.from_numpy(np.load(opt.start_latent))
        latent_end = torch.from_numpy(np.load(opt.end_latent))
        alphas = [float(n / opt.latent_num) for n in range(opt.n_img)]
        latents = [alpha * latent_end + (1 - alpha) * latent_start for alpha in alphas]

    print("Generate image num :", len(latents))

    # ----- Generate Step -----
    print("Start Generate Process")
    for index,latent in tqdm(enumerate(latents)):
        img_path = os.path.join(img_output_dir, "images", str(index + 1) + ".png")
        generate(latent, model_g, opt.width, opt.height, img_path)

        if opt.save_latent:
            latent_path = os.path.join(img_output_dir, "latents", str(index + 1) + ".npy")
            np.save(latent_path, latent.numpy())

    print("Finish Generate Process")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="Weight_Generator/model_G_1000.pth")
    parser.add_argument("--output_dir", default="./result")
    parser.add_argument("--save_latent", action="store_true", default=False)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--width", type=int, default=1)
    parser.add_argument("--height", type=int, default=1)
    # parser.add_argument("--mode", choice=["normal", "use_latent", "inter"], default="normal")
    parser.add_argument("--mode", default="normal")
    parser.add_argument("--n_img", type=int, default=1)

    # normal generation
    # use latent
    parser.add_argument("--latent_dir", default="None")

    # intermediate vectl
    parser.add_argument("--generate_inter", action="store_true", default=False)
    parser.add_argument("--start_latent", type=str, default=".")
    parser.add_argument("--end_latent", type=str, default=".")


    opt = parser.parse_args()
    print(opt)
    # generate(opt)
    # nz = 4096
    # check_z = torch.randn(4096, nz, 1, 1)
    # check_z = torch.randn(size=(nz, 1, 1))
    # print(check_z.shape)
    generate(opt)
    # latent = torch.randn(size=(self.latent_size, 1, 1))
    # generate(check_z,"Weight_Generator/model_G_1000.pth",64,64,"./result")
    # latents, model_G, width, height, save_path