import email
from this import s
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Employee:
    db_name="employee_test"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM employees"
        results = connectToMySQL(cls.db_name).query_db(query)
        employees = []
        for employee in results:
            employees.append(cls(employee))
        return employees
    @classmethod
    def get_in_order_by_id(cls):
        query = "SELECT * FROM employees ORDER BY id"
        results = connectToMySQL(cls.db_name).query_db(query)
        employees = []
        for employee in results:
            employees.append(cls(employee))
        return employees
    
    @classmethod
    def search_for_employees(cls, data):
        # print(data['search_word'])
        query = "SELECT * FROM employees WHERE name LIKE %(search_word)s OR email LIKE %(search_word)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        employees = []
        for employee in results:
            employees.append(cls(employee))
        return employees


