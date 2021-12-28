from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import animal, doctor
import re 
class Owner:
    # class attributes/methods vs instance attributes/methods
    # this is a class attribute its affecting the class 
    db_name = "pet_clinic_schema"
    # constructor
    def __init__(self, data):
        # this is a instance attribute 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.animals = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # instance method (isnt defined with a @method)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # class methods 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM owners;"
        results = connectToMySQL(cls.db_name).query_db(query)
        owners = []
        for row in results:
            this_owner = cls(row)
            owners.append(this_owner)
            # owners.append(cls(row))
        return owners

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM owners;"
    #     results = connectToMySQL(cls.db_name).query_db(query)
    #     owners = []
    #     for row in results:
    #         this_owner = cls(row)
    #         owners.append(this_owner)
    #         # owners.append(cls(row))
    #     return owners

    @classmethod
    def get_one_owner_by_id(cls, data):
        query = "SELECT * FROM owners LEFT JOIN animals ON animals.owner_id = owners.id WHERE owners.id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(f"Results: {results}")
        this_owner = cls(results[0])
        for row in results:
            animal_info = {
                'id': row['animals.id'],
                'name': row['name'],
                'age': row['age'],
                'type': row['type'],
                'created_at': row['animals.created_at'],
                'updated_at': row['animals.updated_at'],
            }
            if row['animals.id'] is not None:
                this_animal = animal.Animal(animal_info)
                this_owner.animals.append(this_animal)
        print(f"OWNER FROM BACK: {this_owner.animals}")
        return this_owner

    @classmethod
    def create_owner(cls, data):
        query = "INSERT INTO owners (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(f"Results: {results}")
        return results

    @classmethod
    def update_owner(cls, data):
        query = "UPDATE owners SET first_name = %(first_name)s, last_name= %(last_name)s WHERE id = %(id)s "
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_owner(cls, data):
        query = "DELETE FROM owners WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def find_animals_by_owner(cls, data):
        query = "SELECT * FROM owners LEFT JOIN animals ON owners.id = animals.owner_id WHERE owners.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # owners_animals = []
        # for row in results:
        #     this_animal = cls(row)
        #     owners_animals.append(this_animal)
            # owners.append(cls(row))
        return results

    @staticmethod
    def validate_owner(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        if len(data['first_name']) <= 1:
            is_valid = False
            flash('First name must be more than one character')
        if len(data['last_name']) <= 1:
            is_valid = False
            flash('Last name must be more than one character')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid email address')
        return is_valid
