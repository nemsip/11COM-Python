from flask import Flask, render_template
import requests
import json
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('`index`.html')

@app.route('/work-hours')
def work_hours():
    return """<h1>Work Hours</h1><p style="color: #D2691E;">Monday - Friday: 5PM - 7PM (GMT+12)<br>Saturday - Sunday: 10AM - 5PM</p>"""

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

@app.route('/about')
def about():
    return """
    <h1>About Me</h1>
    <p>I am a student at the Pakuranga college of studying Computer Science.<br><br>My hobbies are coding, red teaming and designing things for the betterment of the security of the digital world :)<br<br>My Favorite subject is Computer Studies and Music 🎵🎶</p>"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)


