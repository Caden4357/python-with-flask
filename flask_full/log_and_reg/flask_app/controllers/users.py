from flask_app import app
from flask import render_template, redirect, request, session 
from ..models import user
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create_owner():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    user_info = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    new_user_id = user.User.create_user(user_info)
    session['user_id'] = new_user_id
    return redirect('/results')

@app.route('/results')
def results_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/login' , methods=['POST'])
def login():
    if not user.User.validate_login(request.form):
        return redirect('/')

    data = {
        'email': request.form['email']
        
    }
    user_from_db = user.User.get_by_email(data)
    if not user_from_db:
        flash('Invalid email/password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        return redirect('/')
    session['user_id'] = user_from_db.id
    return redirect('/results')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')