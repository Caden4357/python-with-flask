from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class User:
    db_name = "users_with_flask"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(f"Results: {results}")
        return results


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return False
        return cls(results[0])

    @staticmethod
    def validate_registration(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        user_with_email = User.get_by_email({'email': data['email']})
        if len(data['first_name']) < 1:
            is_valid = False
            flash('First name must be more than 1 character')
        if len(data['last_name']) < 1:
            is_valid = False
            flash('Last name must be more than 1 character')
        if len(data['email']) == 0:
            is_valid = False
            flash('Enter an email')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid email address')
        elif user_with_email:
            is_valid = False
            flash('email already exits')
        if len(data['password']) < 6:
            is_valid = False
            flash('Password must be more than 6 characters')
        elif data['password'] != data['confirm_password']:
            flash("Password don't match")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        
        if len(data['email']) == 0:
            flash('Email is required')
            is_valid = False
        if len(data['password']) == 0:
            flash('Password is required')
            is_valid = False
        return is_valid