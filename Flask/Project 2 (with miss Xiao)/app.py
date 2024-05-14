from flask import Flask, render_template
import requests
import json
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return "<h1>Contact Me</h1><h3><a href='mailto:p9ip2qbry@mozmail.com'>Email</a></h3><p>"

@app.route('/generator')
def generator():
    return random.choice(["Hello",
                          "Hola",
                          "Bonjour",
                          "Ciao",
                          "Namaste",
                          "Konnichiwa",
                          "Guten Tag",
                          "Olá",
                          "Aloha",
                          "Shalom",
                          "Salaam",
                          "Zdravstvuyte",
                          "Hallo",
                          "Hej",
                          "Hoi",
                          "Salut",
                          "Halo"])

@app.route('/my-time-zone')
def time():
    now = datetime.now()
    currentdate = now.strftime("%d/%m/%Y")
    return f"Today's date is {currentdate}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)


