from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import re
from ..models import image

# TODOLIST:
# 1.) UPDATE USER SO THEY CAN UPDATE EVERYTHING INCLUDING PASSWORD VIA EMAIL 
# 2.) 
#///////////////////////////////////////////////////////////////////

class User:
    db_name = "image_upload"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_name = data['user_name']
        self.profile_pic = data['profile_pic']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.images = []

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, user_name,profile_pic, email, password) VALUES (%(first_name)s, %(last_name)s, %(user_name)s,%(profile_pic)s, %(email)s, %(password)s)"
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

    @classmethod
    def get_by_user_name(cls, data):
        query = "SELECT * FROM users WHERE user_name = %(user_name)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return False
        return cls(results[0])

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users LEFT JOIN images ON images.users_id = users.id WHERE users.id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        this_user = cls(results[0])
        for row in results:
            image_info = {
                'id': row['images.id'],
                'path': row['path'],
                'created_at': row['images.created_at'],
                'updated_at': row['images.updated_at']
            }
            if row['images.id'] is not None:
                this_image = image.Image(image_info)
                this_user.images.append(this_image)
            print(f"this users images: {image_info}")
        return this_user
    
    @classmethod
    def update_profile_pic(cls,data):
        query="UPDATE users set profile_pic = %(profile_pic)s WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.get_one_user(user_id)

# UPDATE USER PROFILE
    # @classmethod
    # def update_profile(cls,data):
    #     query="UPDATE users set first_name=%(first_name)s,last_name=%(last_name)s, first_name=%(first_name)s profile_pic = %(profile_pic)s WHERE id = %(id)s"
    #     return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_registration(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        user_with_email = User.get_by_email({'email': data['email']})
        user_with_user_name = User.get_by_user_name({'user_name': data['user_name']})
        if len(data['first_name']) < 1:
            is_valid = False
            flash('First name must be more than 1 character')
        if len(data['last_name']) < 1:
            is_valid = False
            flash('Last name must be more than 1 character')
        if len(data['user_name']) < 2:
            is_valid = False
            flash('Username must be more than 2 character')
        elif user_with_user_name:
            is_valid = False
            flash('Username already exits, please choose a new one')
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