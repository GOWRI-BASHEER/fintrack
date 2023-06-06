from flask import Flask, render_template
from PIL import Image
import PIL
import base64
import io
import requests
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello_world():

    URL = 'http://www.w3schools.com/css/trolltunga.jpg'

    with urllib.request.urlopen(URL) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())


    # img = Image.open('temp.jpg')

    # img.show()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')