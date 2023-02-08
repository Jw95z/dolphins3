from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash




class test(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, username, password):
        self._username = username
        self._password = password

 # a getter method, extracts email from object
    @property
    def username(self):
        return self._username
    
    # a setter function, allows name to be updated after initial object creation
    @username.setter
    def username(self, username):
        self._username = username
        
    # check if uid parameter matches user id in object, return boolean
    def is_username(self, username):
        return self._username == username


# a name getter method, extracts name from object
    @property
    def password(self):
        return self._password
    
    # a setter function, allows name to be updated after initial object creation
    @password.setter
    def password(self, password):
        self._password = password

 # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            
        }



# CRUD update: updates user name, password, phone
    # returns self
    def update(self, username="", password = ""):
        """only updates values with length"""
        if len(username) > 0:
            self.username = username
        if len(password) > 0:
            self.password = password
        db.session.commit()
        return self


            