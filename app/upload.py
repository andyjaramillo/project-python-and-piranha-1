from contextlib import _RedirectStream
from distutils.command.config import config
from werkzeug.utils import secure_filename
import os
import site
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = 'app\static\img'

@app.route('/Blog', methods=['POST', 'GET'])
def upload_image():
    if request.method == "POST":
        image = request.files['file']

        if image.filename == '':
            print("File name is invalid")
            return redirect(request.url)

        filename = secure_filename(image.filename)

        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir.app.config["IMAGE_UPLOADS"],filename))

        return render_template("blog.html", filename=filename)
    return render_template("blog.html")
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='/img/'+filename, code=301))

   

