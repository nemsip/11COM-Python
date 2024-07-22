from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        achieved = int(request.form['achieved'])
        merit = int(request.form['merit'])
        excellence = int(request.form['excellence'])
        print(f"Achieved: {achieved}, Merit: {merit}, Excellence: {excellence}") # debugging because was not work
        return render_template('result.html', achieved=achieved, merit=merit, excellence=excellence)
    return render_template('index.html')

# Error Routing

@app.errorhandler(404)
def page_not_found(e):
    return render_template('sys/404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('sys/500.html', e=e), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('sys/403.html'), 403

if __name__ == '__main__':
    app.run(debug=True, port=80)