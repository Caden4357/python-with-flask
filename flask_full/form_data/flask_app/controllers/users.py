from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    all_users = User.get_all()
    return render_template('index.html', all_users=all_users)


# @app.route('/users')
# def users():
#     return jsonify(User.get_all_json())

@app.route('/create/user', methods=['POST'])
def create_user():
    user_name = request.form['user_name']
    email = request.form['email']
    if user_name and email:
        User.save(request.form)
        return jsonify({
            'user_name': user_name,
            'email': email,
            "message":"Success"
            })
    return jsonify({'error': "Missing Data!"})



