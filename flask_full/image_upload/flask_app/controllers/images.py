from flask_app import app
import os
from flask import flash, render_template, request, redirect,url_for, session 
from ..models import image, user
from werkzeug.utils import secure_filename

# TODOLIST:
# 1.) FIX IMAGE THUMBNAIL TO NOT BE BLURRY IF ITS A BIG PICTURE EX. MOUNTAINS PIC 
# 2.) FIX IMAGE SIZE SO ITS NOT BLURRY IM THINKING ON THE DASHBOARD HAVE ALL THE IMAGES DISPLAY LIKE THUMBNAILS BUT IF YOU CLICK ON IT IT WILL DISPLAY FULL SIZE 
#///////////////////////////////////////////////////////////////////

# Path to the uploads folder in the static folder I did it pathed to the static folder so it would be easier to access
UPLOADED_FOLDER = ('C:/Users/wilco/OneDrive/Desktop/SCHOOL/python_w_flask/flask_full/image_upload/flask_app/static/uploads/')

# defining the types of files we accept
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOADED_FOLDER'] = UPLOADED_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/dashboard')
def dashboard():
    data = {
        'id':session['user_id']
    }
    all_images = image.Image.get_all_images()
    return render_template('index.html', all_images=all_images, this_user=user.User.get_one_user(data))

@app.route('/upload', methods=['POST'])
def upload_file():
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
            print(UPLOADED_FOLDER)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_FOLDER'], filename))
            print(f"this is line 34 : {UPLOADED_FOLDER}")

            info_for_file = {
                'path': "/static/uploads/" + filename,
                'users_id': session['user_id']
            }
            image.Image.upload_image(info_for_file)
        return redirect('/dashboard')