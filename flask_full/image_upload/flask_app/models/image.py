from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Image:
    db_name = "image_upload"
    def __init__(self, data):
        self.id = data['id']
        self.path = data['path']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def upload_image(cls, data):
        query = "INSERT INTO image (path) VALUES(%(path)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results
    
    @classmethod
    def get_all_images(cls):
        query = "SELECT * FROM image"
        results = connectToMySQL(cls.db_name).query_db(query)
        return results