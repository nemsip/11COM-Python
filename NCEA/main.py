from flask import Flask, render_template, request
import os
import datetime

app = Flask(__name__)

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
    error_message = str(e)
    log_path = "/logs/latest.log"
    log_dir = os.path.dirname(log_path)
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    if os.path.exists(log_path):
        # dunno of this works and im too scared to test it
        log_time = datetime.datetime.fromtimestamp(os.path.getctime(log_path)).strftime("%Y-%m-%d_%H-%M-%S")
        log_name = f"log_{log_time}.log"
        os.rename(log_path, os.path.join(log_dir, log_name))
    
    with open(log_path, "w") as log_file:
        log_file.write(error_message)
    
    return render_template('sys/500.html', e=e), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('sys/403.html', e=e), 403

if __name__ == '__main__':
    app.run(port=80, debug=True)