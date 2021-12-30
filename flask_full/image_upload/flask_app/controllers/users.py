from flask_app import app
from flask import render_template, redirect, request, session 
from ..models import user, image
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('log_reg.html')

@app.route('/register', methods=['POST'])
def create_user():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    pathToDefaultPic = "/static/profilePictures/blank-profile-pic.png"
    user_info = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'user_name': request.form['user_name'],
        'profile_pic': pathToDefaultPic,
        'email': request.form['email'],
        'password': pw_hash,
    }
    new_user_id = user.User.create_user(user_info)
    session['user_id'] = new_user_id
    session['user_name'] = user_info['user_name']
    return redirect('/dashboard')

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
    session['user_name'] = user_from_db.user_name
    return redirect('/dashboard')

@app.route('/user_who_posted/<int:id>')
def one_users_profile(id):
    print(id)
    data = {
        'id': id
    }
    this_user = user.User.get_one_user(data)
    print(this_user)
    return render_template('user_profile.html', this_user=this_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')