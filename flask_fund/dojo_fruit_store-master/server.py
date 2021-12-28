from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    # order= [
    #     {'first_name': request.form['first_name']},
    #     {'last_name': request.form['last_name']},
    #     {'strawberry': request.form['strawberry']},
    #     {'raspberry': request.form['raspberry']},
    #     {'apple': request.form['apple']}
    # ]
    first_name = request.form['first_name']
    count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    order = request.form
    print("Charging " + request.form['first_name'] + " For " + str(count) + " Fruits")
    print(f'Charging {first_name}  For  {count} Fruits')

    return render_template("checkout.html", order=order, count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    