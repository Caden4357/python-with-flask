from flask import Flask, render_template, redirect, session, request
from flask import flash
import random
from datetime import datetime
app=Flask(__name__)
app.secret_key = "terces yek"
@app.route('/')
def index():
    if 'total_gold' and 'activities' and 'moves' not in session:
        session['total_gold'] = 0 
        session['activities'] = ""
        session['moves'] = 5 
    if session['moves'] <= 0:
        if session['total_gold'] >= 25:
            flash("Yay you won!")
        else:
            flash("Sorry you lost you need 250 or more gold!")
    return render_template('index.html', message=session['activities'], moves =session['moves'])



@app.route('/process_money', methods=['POST'])
def process_money():
    my_gold = session['total_gold']
    location = request.form['building']
    activities = session['activities'] 
    time_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if session['moves'] == 0:
        return redirect('/reset')
    if location == "farm":
        gold_this_turn = random.randint(10,20)
    elif location == "cave":
        gold_this_turn = random.randint(5,10)
    elif location == "house":
        gold_this_turn = random.randint(2,5)
    else:
        gold_this_turn = random.randint(-50,50)
    my_gold += gold_this_turn
    session['total_gold'] = my_gold
    if gold_this_turn >= 0:
        new_str = f"<p class='text-primary'>You earned {gold_this_turn} from {location} ({time_formatted})</p>"
        activities += new_str
        session['activities'] = activities
    else:
        new_str = f"<p class='text-danger'>Oh no! you lost {gold_this_turn} from {location} ({time_formatted})</p>"
        activities += new_str
        session['activities'] = activities
    session['moves'] -= 1
    if session['moves'] == 0:
        return redirect('/')
    return redirect('/')




@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)