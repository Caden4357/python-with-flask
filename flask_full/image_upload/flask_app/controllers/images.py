from flask_app import app
import os
from flask import flash, render_template, request, redirect,url_for
from ..models import image
from werkzeug.utils import secure_filename

# Path to the uploads folder in the static folder I did it pathed to the static folder so it would be easier to access

UPLOAD_FOLDER = ('C:/Users/wilco/OneDrive/Desktop/SCHOOL/Python/flask_fullstack/image_upload/flask_app/static/uploads/')

# defining the types of files we accept
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    images=image.Image.get_all_images()
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file and allowed_file(file.filename):
            print(UPLOAD_FOLDER)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)

            path_for_file = {
                'path': "/static/uploads/" + filename
            }
            image.Image.upload_image(path_for_file)
        return redirect('/')