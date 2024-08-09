from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
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