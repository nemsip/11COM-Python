import os
import traceback
from datetime import datetime
import re
import sqlite3

import bcrypt
import dotenv
from flask import (Flask, flash, redirect, render_template, request,
                   session)
from groq import Groq

dotenv.load_dotenv()

app = Flask(__name__, static_url_path='/static')

app.secret_key = 'skibidi'
app.config['SESSION_TYPE'] = 'filesystem'


def log_error(error):
    try:
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
        log_file = os.path.join(log_dir, 'latest.log')

        os.makedirs(log_dir, exist_ok=True)

        if os.path.exists(log_file):
            timestamp = datetime.fromtimestamp(os.path.getmtime(log_file)).strftime('%Y%m%d_%H%M%S')
            os.rename(log_file, os.path.join(log_dir, f'error_{timestamp}.log'))

        with open(log_file, 'w') as f:
            f.write(f"Error occurred at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Error: {error}\n\n")
            f.write(traceback.format_exc())
            f.write("\n")
    except Exception as log_exception:
        print(f"Failed to log error: {log_exception}")


@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('logged_in'):
        flash(f'Logged in as {session["username"]}')
    return render_template('index.html')


def get_translation(text):
    client = Groq(api_key=os.getenv('groq_api'))

    system_prompt = {
        "role": "system",
        "content": "You are a Translator that translates english new zealand place names and mountain into their traditional name in the Maori Language. For example, Auckland is Tāmaki Makaurau, and Mount Wellington is Maungarei. You reply with JUST the translated name. If you don't know the name, reply with \"Error\". Don't add any extra text. Do not say anything along the lines of \"Please provide the English name of the place or mountain you'd like me to translate or Please go ahead and provide the English name of the place or mountain you'd like me to translate.\", the only accepted output is the translated name if applicable, if not, to say Error. Only reply with the translated name. Do not hallucinate, which means do not make up a name that doesn't exist. If the name is not in the Maori language or you don't know, reply with \"Error\". If the name is not in english and is in Maori, do not translate. If the name is in both languages or a mix of both, translate what isn't maori already into Maori. Do not translate the name into any other language other than Maori."
    }

    chat_history = [system_prompt]
    chat_history.append({"role": "user", "content": text})

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=50,
        temperature=1.2
    )

    result = response.choices[0].message.content.strip()

    if result == "Error":
        result = text

    return result


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        ethnicity = request.form.get('ethnicity')
        if ethnicity == 'maori':
            ingoa = request.form.get('ingoa')
            whanau = request.form.get('whanau')
            marae = request.form.get('marae')
            iwi = request.form.get('iwi')
            maunga = request.form.get('maunga')
            awa = request.form.get('awa')
            waka = request.form.get('waka')

            maungaTranslated = get_translation(maunga)

        elif ethnicity == 'pakeha':
            name = request.form.get('name')
            family_name = request.form.get('family-name')
            home = request.form.get('home')
            river = request.form.get('river')
            mountain = request.form.get('mountain')

            homeTranslated = get_translation(home)
            mtTranslated = get_translation(mountain)

        return render_template(
            'result.html',
            name=name if request.form.get('ethnicity') == 'pakeha' else None,
            family_name=family_name if request.form.get('ethnicity') == 'pakeha' else None,
            homeTranslated=homeTranslated if request.form.get('ethnicity') == 'pakeha' else None,
            river=river if request.form.get('ethnicity') == 'pakeha' else None,
            mtTranslated=mtTranslated if request.form.get('ethnicity') == 'pakeha' else None,
            ingoa=ingoa if request.form.get('ethnicity') == 'maori' else None,
            whanau=whanau if request.form.get('ethnicity') == 'maori' else None,
            marae=marae if request.form.get('ethnicity') == 'maori' else None,
            iwi=iwi if request.form.get('ethnicity') == 'maori' else None,
            maungaTranslated=maungaTranslated if request.form.get('ethnicity') == 'maori' else None,
            awa=awa if request.form.get('ethnicity') == 'maori' else None,
            waka=waka if request.form.get('ethnicity') == 'maori' else None,
            ethnicity=ethnicity
        )
    return render_template('generate.html')


@app.route('/learn')
def about_pepeha():
    return render_template('about-pepeha.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and not session.get('logged_in'):
        username = request.form.get('username')
        password = request.form.get('password')
    
        with sqlite3.connect('./db/login.db') as con:
            pass
    return render_template('auth/login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        
        # validating
        username_regex = re.compile(r'^[a-zA-Z0-9_]{4,32}$')
        if not username_regex.match(username):
            flash('Username must be between 4 and 32 characters and can only contain letters, numbers, and underscores.')

        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        if not password_regex.match(password):
            flash('Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, one number, and one special character.')

        if password != confirm_password:
            flash('Passwords do not match.')
        
        hpass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        with sqlite3.connect('./db/login.db') as con:
            cur = con.cursor()  
            cur.execute("SELECT * FROM users WHERE username = ?", (username,))
            if cur.fetchone():
                flash('Username already exists.')
            else:
                cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hpass))
                con.commit()
                session['logged_in'] = True
                session['username'] = username
                return redirect('/login')
    return render_template('auth/signup.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('sys/404.html', e=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    try:
        log_error(e)
    except Exception as logging_error:
        print(f"Error while logging: {logging_error}")
    return render_template('sys/500.html', e=e), 500


@app.errorhandler(403)
def forbidden(e):
    return render_template('sys/403.html', e=e), 403


if __name__ == '__main__':
    app.run(port=80, debug=True)