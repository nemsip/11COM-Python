# flasktest.py
# ---------------
# Resources used:
# https://www.youtube.com/watch?v=5aYpkLfkgRE (NetworkChuck)
# ---------------

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/image-search')
def imageSearch():
    return render_template('imageSearch.html')

@app.route('/image-search', methods=['GET'])
def image_search():
    query = request.args.get('query')
    api_key = '38765376-df4916e59545efa59174e1ebb'
    response = requests.get(f'https://pixabay.com/api/?key={api_key}&q={query}&per_page=20')
    data = response.json()
    return render_template('results.html', images=data['hits'])

app.run(host="0.0.0.0", port=80, debug=True)
