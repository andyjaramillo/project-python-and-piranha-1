import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index(debug=True): #debug=True prevents us from having to restart the server to see changes. REMOVE LATER.
    return render_template('index.html')
