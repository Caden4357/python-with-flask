from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import owner, doctor

class Animal:
    db_name = "pet_clinic_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.owner = owner.Owner.get_one_owner_by_id({'id':data['owner_id']})
        # self.doctors = []
        # self.doctors = Animal.get_doctors_for_animal(data)
        self.owner = []
        self.doctors = []
    @classmethod
    def get_all_animals(cls):
        query = "SELECT * FROM animals JOIN owners ON owners.id = owner_id"
        results = connectToMySQL(cls.db_name).query_db(query)
        animals = []
        for animal in results:
            this_animal = cls(animal)
            # print(this_animal.owner.full_name())

            owner_info = {
                'id': animal['owners.id'],
                'first_name': animal['first_name'],
                'last_name': animal['last_name'],
                'email': animal['email'],
                'created_at': animal['created_at'],
                'updated_at': animal['updated_at'],
            }
            this_owner = owner.Owner(owner_info)
            this_animal.owner = this_owner

            animals.append(this_animal)
        return animals

    @classmethod
    def create_animal(cls, data):
        query = "INSERT INTO animals (name, age, type, owner_id) VALUES (%(name)s, %(age)s, %(type)s, %(owner_id)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_one_animal(cls, data):
        query = "SELECT * FROM animals JOIN owners on owners.id = owner_id LEFT JOIN doctors_has_animals on animals.id = doctors_has_animals.animals_id LEFT JOIN doctors on doctors.id = doctors_has_animals.doctors_id WHERE animals.id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)

        this_animal = cls(results[0])
        owner_info = {
            'id': results[0]['owners.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            'email': results[0]['email'],
            'created_at': results[0]['owners.created_at'],
            'updated_at': results[0]['owners.updated_at']
        }
        this_owner = owner.Owner(owner_info)
        this_animal.owner = this_owner
        for row in results:
            doctors_info = {
                'id': row['doctors.id'],
                'first_name': row['doctors.first_name'],
                'last_name': row['doctors.last_name'],
                'created_at': row['doctors.created_at'],
                'updated_at': row['doctors.updated_at'],
            }
            if row['doctors.id'] is not None:
                this_doctor = doctor.Doctor(doctors_info)
                this_animal.doctors.append(this_doctor)
        return this_animal

    # @classmethod
    # def get_doctors_for_animal(cls, data):
    #     query = "SELECT * FROM doctors LEFT JOIN doctors_has_animals ON doctors.id = doctors_has_animals.doctors_id WHERE doctors_has_animals.animals_id = %(id)s"
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     print(results)
            
    #     return results

    @classmethod
    def update_animal(cls, data):
        query = "UPDATE animals SET name = %(name)s, age= %(age)s, type= %(type)s, owner_id=%(owner_id)s WHERE id = %(id)s "
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @staticmethod
    def validate_animals(data):
        is_valid = True
        if len(data['name']) <= 1:
            is_valid = False
            flash('Name must be more than 1 character', "error")
        if len(data['age']) == 0:
            is_valid = False
            flash('age must be more than 1 character', "error")
        elif float(data['age']) < 0:
            is_valid = False
            flash('age must be a positive number', "error")
        if len(data['type']) <= 1:
            is_valid = False
            flash('type must be more than 1 character', "error")
        return is_valid


    # @classmethod
    # def find_animals_by_owner(cls, data):
    #     query = "SELECT * FROM animals WHERE animals.owner_id = %(id)s"
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     # owners_animals = []
    #     # for animal in results:
    #     #     this_animal = cls(animal)
    #     #     owners_animals.append(this_animal)

    #     return results