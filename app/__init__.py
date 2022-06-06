import os
import sys
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

@app.route('/')
def index(debug=True): #debug=True prevents us from having to restart the server to see changes. REMOVE LATER.
    return render_template('index.html')

@app.route('/blog/')
def blog(debug=True): 
    return render_template('blog.html')

@app.route('/aboutus/')
def aboutUs(): 
    return render_template('aboutUs.html', pagetitle = 'About Us')

@app.route('/contact-us/')
def contactUs(): 
    return render_template('contactPage.html')

@app.route('/hobbies/')
def hobbies(): 
    return render_template('hobbies.html')

