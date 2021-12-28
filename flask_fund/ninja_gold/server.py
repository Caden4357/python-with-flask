from flask import Flask, request, redirect, render_template, session
import random
app = Flask(__name__)
app.secret_key = "srecet yek"

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    if 'messages' not in session:
        session['messages'] = []
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def proccess_money():
    if request.form['building'] == "farm":
        session['amount'] = random.randint(10,20)
        session['count'] += session['amount']
    elif request.form['building'] == "cave":
        session['amount'] = random.randint(5,10)
        session['count'] += session['amount']
    elif request.form['building'] == "house":
        session['amount'] = random.randint(2,5)
        session['count'] += session['amount']
    elif request.form['building'] == "casino":
        session['amount'] = random.randint(-50,50)
        session['count'] += session['amount']
    if session['amount'] > 0:
        session['messages'].append(f"You earned {session['amount']} gold from {request.form['building']} ")
    else: 
        session['messages'].append(f"You lost {session['amount']} gold from {request.form['building']} ")
    print(session['messages'])
    return redirect('/')

@app.route('/reset')
def reset_gold():
    session.clear()
    return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)   
