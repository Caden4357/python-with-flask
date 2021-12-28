from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    times = 3
    return render_template("index.html", times=times)

@app.route('/play/<int:times>')
def playground(times):
    times=times
    return render_template("play.html", times=times, color="blue")

@app.route('/play/<int:times>/<string:color>')
def playground2(times, color):
    times=times
    return render_template("play.html", times=times, color=color)
if __name__=="__main__":
    app.run(debug=True) # run our server