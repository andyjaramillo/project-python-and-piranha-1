import os
import site
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Portfolio Site", url=os.getenv("URL"))

@app.route('/Blog')
def Blog_site():
    return render_template('blog.html', title="Blog page", url=os.getenv("URL"))

@app.route('/Home')
def Home_site():
    return render_template('index.html', title="Home page", url=os.getenv("URL"))

@app.route('/About')
def About_site():
    return render_template('About.html', title="About page", url=os.getenv("URL"))
