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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
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

@app.route('/introduce')
def introduce():
    return render_template('introduce.html')

@app.route('/infer', methods=['POST'])
def success():
    if request.method == 'POST':
        flag = 0
        models_dcgan.test(flag)
        # filename = models_dcgan.test()
        # return render_template('inference.html', name=inference, confidence=confidence)
        # return render_template('inference.html', generated_image=filename)
        # r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        # r.headers["Pragma"] = "no-cache"
        # r.headers["Expires"] = "0"
        # r.headers['Cache-Control'] = 'public, max-age=0'
        # return r
        return render_template('inference.html')

@app.route('/infer2', methods=['POST'])
def success2():
    if request.method == 'POST':
        flag = 1
        models_dcgan.test(flag)
        # filename = models_dcgan.test()
        # return render_template('inference.html', name=inference, confidence=confidence)
        # return render_template('inference.html', generated_image=filename)
        # r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        # r.headers["Pragma"] = "no-cache"
        # r.headers["Expires"] = "0"
        # r.headers['Cache-Control'] = 'public, max-age=0'
        # return r
        return render_template('inference.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
