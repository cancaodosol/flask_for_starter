#coding:utf-8

import os
import sys
from flask import Flask, jsonify
from flask import Flask, render_template
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/circle')
def index_circle():
    return render_template('canvas/circle.html')

if __name__ == "__main__":
    app.run(debug=True)