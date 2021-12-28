from flask_app import app
from flask import render_template, redirect, request, session
from ..models import animal, doctor, owner

@app.route('/animals')
def animals():
    all_animals = animal.Animal.get_all_animals()
    return render_template('animal.html', all_animals=all_animals)

@app.route('/new/animal')
def new_animal():
    owners = owner.Owner.get_all()

    return render_template('create_animal.html', owners=owners)

@app.route('/create/animal', methods=['POST'])
def create_animal():
    print(request.form)
    if not animal.Animal.validate_animals(request.form):
        return redirect('/new/animal')
    new_animal_id = animal.Animal.create_animal(request.form)
    print(new_animal)

    return redirect('/animals')

@app.route('/single/animal/<int:id>')
def get_one_animal(id):
    print(id)
    owners = owner.Owner.get_all()
    data = {
        "id": id
    }
    print(data)
    one_animal = animal.Animal.get_one_animal(data)
    print(one_animal)
    return render_template('animal_profile.html', one_animal=one_animal, owners=owners, doctors = doctor.Doctor.get_all())

@app.route('/edit/animal/<int:id>')
def edit_animal(id):
    print(id)
    owners = owner.Owner.get_all()
    data = {
        "id": id
    }
    print(data)
    this_animal = animal.Animal.get_one_animal(data)
    print(this_animal)
    return render_template('edit_animal.html', this_animal=this_animal, owners=owners)

@app.route('/update/animal/<int:id>', methods=['POST'])
def get_one_and_update(id):
    print(id)
    data = {
        'id': id,
        'name': request.form['name'],
        'age': request.form['age'],
        'type': request.form['type'],
        'owner_id':request.form['owner_id']
    }
    print(data)
    animal.Animal.update_animal(data)
    return redirect('/animals')

@app.route('/animals/<int:animal_id>/add_doctor', methods=["POST"])
def add_doctor_to_animal(animal_id):
    data = {
        'animal_id': animal_id,
        'doctor_id': request.form['doctor_id']
    }
    new_relationship = doctor.Doctor.add_doctor(data)
    return redirect('/')
