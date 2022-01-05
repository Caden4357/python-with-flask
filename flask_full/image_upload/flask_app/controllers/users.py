from flask_app import app, mail
import os
from flask import render_template, redirect, request, session, url_for
from ..models import user, image
from flask import flash
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from flask_mail import Message
bcrypt = Bcrypt(app)

# Path to the uploads folder in the static folder I did it pathed to the static folder so it would be easier to access
UPLOAD_FOLDER = ('C:/Users/wilco/OneDrive/Desktop/SCHOOL/python_w_flask/flask_full/image_upload/flask_app/static/profilePictures/')

# defining the types of files we accept
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')

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

@app.route('/profile/<int:id>')
def one_users_profile(id):
    print(id)
    data = {
        'id': id
    }
    this_user = user.User.get_one_user(data)
    print(this_user)
    return render_template('user_profile.html', this_user=this_user)

@app.route("/change_profile_pic/<int:id>")
def change_profile_pic(id):
    data = {
        'id': id
    }
    this_user=user.User.get_one_user(data)
    print(this_user)
    return render_template('update_profile.html', this_user=this_user)

@app.route('/update/profile_pic/<int:id>', methods=['POST'])
def upload_profile_pic(id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/dashboard')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/dashboard')
        if file and allowed_file(file.filename):
            print(UPLOAD_FOLDER)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(f"this is line 34 : {UPLOAD_FOLDER}")
            data = {
                'id':id,
                'profile_pic': "/static/profilePictures/" + filename,
            }
            user.User.update_profile_pic(data)
        return redirect('/dashboard')

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("password reset request", sender='noreply@demo.com', recipients=[user.email])
    print("this is email " + user.email)
    msg.body = f'''To reset your password click the link:
{url_for('reset_token', token=token, _external=True)}
'''
    mail.send(msg)

@app.route('/reset_password')
def reset_request():
    return render_template('reset_password.html')
    
@app.route('/req/reset_password', methods=['POST'])
def reset_password_form():
    data ={
        'email': request.form['email']
    }
    this_user = user.User.get_by_email(data)
    if not this_user:
        flash("No account with that email sign up")
    else:
        send_reset_email(this_user)
        flash('An email has been set with instructions to reset password')
    return redirect('/')


@app.route('/req/reset_password/<token>', methods=['POST'])
def reset_token(token):
    this_user = user.User.verify_reset_token(token)
    return render_template('reset_password_form.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')