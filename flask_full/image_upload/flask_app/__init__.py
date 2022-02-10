import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
# app.secret_key = "scdfsfdssxcvd"
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
mail = Mail(app)