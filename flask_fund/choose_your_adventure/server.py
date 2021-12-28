from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/left')
def left():
    return render_template("left_room.html")

@app.route('/right')
def right():
    return render_template("right_room.html")

@app.route('/red_door')
def red_door():
    return render_template("winning.html")

@app.route('/black_door')
def black_door():
    return render_template("black_door.html")

app.run(debug=True)
