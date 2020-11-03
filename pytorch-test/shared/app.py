# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
# from models import MobileNet
import os
from math import floor
# from torch import nn, optim
# from torchvision.utils import save_image
# from torch.utils.data import Dataset, DataLoader, TensorDataset
# from torchvision import transforms, datasets
# import tqdm
# from statistics import mean
# import statistics
# from PIL import Image
# from torchvision import transforms
# from models_dcgan import Generator
import models_dcgan

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

# model = MobileNet()
# model = Generator()



# save_image(fake_img,"gen_490.jpg")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/see_other')
def see_other():
    return render_template('see_other.html')

@app.route('/infer', methods=['POST'])
def success():
    if request.method == 'POST':
        filename = models_dcgan.test()
        # f = request.files['file']
        # saveLocation = f.filename
        # f.save(saveLocation)
        # inference, confidence = model.infer(saveLocation)
        # make a percentage with 2 decimal points
        # confidence = floor(confidence * 10000) / 100
        # delete file after making an inference
        # os.remove(saveLocation)
        # respond with the inference
        # return render_template('inference.html', name=inference, confidence=confidence)
        return render_template('inference.html', generated_image=filename)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
