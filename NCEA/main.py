from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        family_name = request.form.get('family-name')
        home = request.form.get('home')
        ocean = request.form.get('ocean')
        mountain = request.form.get('mountain')
        river = request.form.get('river')
        ancestry = request.form.get('ancestry')
        
        ingoa = request.form.get('ingoa')
        whanau = request.form.get('whanau')
        marae = request.form.get('marae')
        iwi = request.form.get('iwi')
        maunga = request.form.get('maunga')
        awa = request.form.get('awa')
        waka = request.form.get('waka')
        
        # form.get
        return render_template('result.html',
                               name=name,
                               family_name=family_name,
                               home=home, ocean=ocean,
                               mountain=mountain,
                               river=river,
                               ancestry=ancestry,
                               
                               ingoa=ingoa,
                               whanau=whanau,
                               marae=marae, iwi=iwi,
                               maunga=maunga,
                               awa=awa,
                               waka=waka)
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('sys/404.html', e=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('sys/500.html', e=e), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('sys/403.html', e=e), 403

if __name__ == '__main__':
    app.run(port=80, debug=True)