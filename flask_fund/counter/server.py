from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "CadensSecretKey"

@app.route('/')         
def index():
    if "count" not in session:
        session['count'] = 0
    return render_template("index.html")

@app.route('/add_one')
def add_one():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return redirect('/')

@app.route('/add_two')
def add_two():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 2
    return redirect('/')

@app.route('/any_number', methods=['POST'])
def any_number():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += int(request.form['number'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    