
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class User:
    db = "users_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    @classmethod
    def add_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(fname)s, %(lname)s, %(email)s);
                """
        
        result = connectToMySQL('users_schema').query_db(query, data)
        
        if result:
            return result
        else:
            return "Failed to add user"

    
    @classmethod
    def show_all_users(cls):
        query = """
                SELECT * 
                FROM users
                """
        
        results = connectToMySQL(cls.db).query_db(query)

        users = []
        
        for user in results:
            users.append(cls(user))
        return users



    # Create Users Models



    # Read Users Models



    # Update Users Models



    # Delete Users Models