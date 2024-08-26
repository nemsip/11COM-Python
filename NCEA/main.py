import os
import traceback
from flask import Flask, render_template, request, flash, sessions, redirect
import re
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'skibidi'

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
def home():
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
            
        elif ethnicity == 'pakeha':
            name = request.form.get('name')
            family_name = request.form.get('family-name')
            home = request.form.get('home')
            ocean = request.form.get('ocean')
            mountain = request.form.get('mountain')
            river = request.form.get('river')
            ancestry = request.form.get('ancestry')
            
            # ok so it doesnt even work
            try:
                print("name: ", name)
            except:
                print("ldjlkjdfg") 
        
        return render_template('result.html',
                               # there has to be a better way to do this 😭    
                               name=name if request.form.get('ethnicity') == 'pakeha' else None,
                               family_name=family_name if request.form.get('ethnicity') == 'pakeha' else None,
                               home=home if request.form.get('ethnicity') == 'pakeha' else None,
                               ocean=ocean if request.form.get('ethnicity') == 'pakeha' else None,
                               mountain=mountain if request.form.get('ethnicity') == 'pakeha' else None,
                               river=river if request.form.get('ethnicity') == 'pakeha' else None,
                               ancestry=ancestry if request.form.get('ethnicity') == 'pakeha' else None,
                               
                               ingoa=ingoa if request.form.get('ethnicity') == 'maori' else None,
                               whanau=whanau if request.form.get('ethnicity') == 'maori' else None,
                               marae=marae if request.form.get('ethnicity') == 'maori' else None,
                               iwi=iwi if request.form.get('ethnicity') == 'maori' else None,
                               maunga=maunga if request.form.get('ethnicity') == 'maori' else None,
                               awa=awa if request.form.get('ethnicity') == 'maori' else None,
                               waka=waka if request.form.get('ethnicity') == 'maori' else None,
                               
                               ethnicity=ethnicity)
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # sql query to check if user exists
        # validate user
        # validate pwd
        # login success
        
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
        
        # sql query to check if user already exists
        # add user to db
        # signup success
        # login user

    return render_template('auth/signup.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('sys/404.html', e=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    print("500 error triggered")  # FOR DEBUGUGGIN
    try:
        log_error(e)
    except Exception as logging_error:
        print(f"Error while logging: {logging_error}")
    return render_template('sys/500.html', e=e), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('sys/403.html', e=e), 403

# server error logging works if the server is running without debug mode
if __name__ == '__main__':
    app.run(port=80, debug=True)
