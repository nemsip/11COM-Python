import os
import traceback
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

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
        if request.form.get('form_id') == 'maoriForm': 
            ingoa = request.form.get('ingoa')
            whanau = request.form.get('whanau')
            marae = request.form.get('marae')
            iwi = request.form.get('iwi')
            maunga = request.form.get('maunga')
            awa = request.form.get('awa')
            waka = request.form.get('waka')
    
        elif request.form.get('form_id') == 'pakehaForm':
            name = request.form.get('name')
            family_name = request.form.get('family-name')
            home = request.form.get('home')
            ocean = request.form.get('ocean')
            mountain = request.form.get('mountain')
            river = request.form.get('river')
            ancestry = request.form.get('ancestry')
        
        return render_template('result.html',
                               # there has to be a better way to do this 😭    
                               name=name if request.form.get('form_id') == 'pakehaForm' else None,
                               family_name=family_name if request.form.get('form_id') == 'pakehaForm' else None,
                               home=home if request.form.get('form_id') == 'pakehaForm' else None,
                               ocean=ocean if request.form.get('form_id') == 'pakehaForm' else None,
                               mountain=mountain if request.form.get('form_id') == 'pakehaForm' else None,
                               river=river if request.form.get('form_id') == 'pakehaForm' else None,
                               ancestry=ancestry if request.form.get('form_id') == 'pakehaForm' else None,
                               
                               ingoa=ingoa if request.form.get('form_id') == 'maoriForm' else None,
                               whanau=whanau if request.form.get('form_id') == 'maoriForm' else None,
                               marae=marae if request.form.get('form_id') == 'maoriForm' else None,
                               iwi=iwi if request.form.get('form_id') == 'maoriForm' else None,
                               maunga=maunga if request.form.get('form_id') == 'maoriForm' else None,
                               awa=awa if request.form.get('form_id') == 'maoriForm' else None,
                               waka=waka if request.form.get('form_id') == 'maoriForm' else None)
    return render_template('index.html')

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
