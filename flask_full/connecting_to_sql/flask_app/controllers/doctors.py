from flask_app import app
import json
from flask import render_template, redirect, request, session
from ..models import owner,animal, doctor

@app.route('/new/doctor')
def new_doctor():
    return render_template('new_doctor.html')

@app.route('/create/doctor', methods=['POST'])
def create_doctor():
    doctor.Doctor.create_doctor(request.form)
    return redirect('/')

