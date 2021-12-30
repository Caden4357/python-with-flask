from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from ..models import user

class Image:
    db_name = "image_upload"
    def __init__(self, data):
        self.id = data['id']
        self.path = data['path']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = []

    @classmethod
    def upload_image(cls, data):
        query = "INSERT INTO images (path, users_id) VALUES(%(path)s, %(users_id)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results
    
    @classmethod
    def get_all_images(cls):
        query = "SELECT * FROM images JOIN users on users.id = images.users_id"
        results = connectToMySQL(cls.db_name).query_db(query)
        images = []
        for row in results:
            this_image = cls(row)
            user_info = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'user_name': row['user_name'],
                'profile_pic': row['profile_pic'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
            }
            this_user = user.User(user_info)
            this_image.user = this_user
            images.append(this_image)
            print(this_user.id)
        return images