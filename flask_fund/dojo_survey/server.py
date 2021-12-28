from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "sdfdfdsfss" 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST"])         
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite-lang'] = request.form['favorite-lang']
    session['about-you'] = request.form['about-you']
    session['sport'] = request.form['sport']
    return redirect("/success")

@app.route('/success')
def success():
    return render_template('result.html')

if __name__=="__main__":   
    app.run(debug=True)   