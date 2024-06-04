from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile-form')
def profile_form():
    return render_template('profile-form.html')

@app.route('/profile-result')
def profile_result():
    fname=request.args.get('fname')
    lname=request.args.get('lname')
    age=int(request.args.get('age'))
    return render_template('profile-result.html', fname=fname, lname=lname, age=age)
    
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('/sys/405.html'), 405
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('/sys/404.html'), 404

@app.route("/calculate")
def calculate():
    return render_template('calc-in.html')

@app.route("/calc-out")
def calc_out():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    oper = request.args.get('operation')

    return render_template('calc-out.html', num1=num1, num2=num2, oper=oper) #, result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)