from flask_app import app
import json
import jsonpickle
from flask import render_template, redirect, request, session
from ..models import owner,animal


@app.route('/')
def index():
    owners = owner.Owner.get_all()
    print(owners)
    return render_template('index.html', owners=owners)

@app.route('/single/owner/<int:id>')
def get_one_owner(id):
    print(id)
    data = {
        "id": id
    }
    print(data)
    this_owner = owner.Owner.get_one_owner_by_id(data)
    # this_owners_animals = animal.Animal.find_animals_by_owner(data)
    # this_owners_animals = owner.Owner.find_animals_by_owner(data)
    print(f"OWNER!!: {this_owner.full_name()}")
    # print(this_owners_animals)
    # this_ownerJSONdata = jsonpickle.encode(this_owner, indent=4)
    # session['this_owner'] = this_ownerJSONdata
    return render_template('one_owner.html', this_owner=this_owner)

@app.route('/new/owner')
def new_owner():
    return render_template('create_owner.html')

@app.route('/create/owner', methods=['POST'])
def create_owner():
    if not owner.Owner.validate_owner(request.form):
        return redirect('/new/owner')
    owner_id = owner.Owner.create_owner(request.form)
    return redirect('/')

@app.route('/update/user/<int:id>', methods=['POST'])
def update_owner(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
    }
    owner.Owner.update_owner(data)
    return redirect('/')

@app.route('/delete/owner/<int:id>')
def delete_owner(id):
    data = {
        "id": id
    }
    owner.Owner.delete_owner(data)
    return redirect('/')

