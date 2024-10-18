#coding:utf-8

import os
import sys
from flask import Flask, jsonify
from flask import Flask, render_template
from flask_cors import CORS

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app as service

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/circle')
def index_circle():
    return render_template('canvas/circle.html')

@app.route('/train')
def index_train():
    return render_template('canvas/train.html')

@app.route('/api/osakametro_station_coords')
def api_get_osakametro_station_coords():
    result = service.get_osakametro_station_coords()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)