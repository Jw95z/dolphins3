from random import randrange
from datetime import date
import json
from flask_sqlalchemy import SQLAlchemy
from __init__ import db, app
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



class test(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(255), unique=False, nullable=False)
    _bmi = db.Column(db.String(255), unique=False, nullable=False)
    _monday = db.Column(db.String(255), unique=False, nullable=False)
    _tuesday = db.Column(db.String(255), unique=False, nullable=False)
    _wednesday = db.Column(db.String(255), unique=False, nullable=False)
    _thursday = db.Column(db.String(255), unique=False, nullable=False)
    _friday = db.Column(db.String(255), unique=False, nullable=False)
    _saturday = db.Column(db.String(255), unique=False, nullable=False)
    _sunday = db.Column(db.String(255), unique=False, nullable=False)
    _calories = db.Column(db.String(255), unique=False, nullable=False)
    _sport = db.Column(db.String(255), unique=False, nullable=False)
    def __init__(self, username, password, bmi, monday, tuesday, wednesday, thursday, friday, saturday, sunday, calories, sport):
        self._username = username
        self._password = password
        self._bmi = bmi
        self._monday = monday
        self._tuesday = tuesday
        self._wednesday = wednesday
        self._thursday = thursday
        self._friday = friday
        self._saturday = saturday
        self._sunday = sunday
        self._calories = calories
        self._sport = sport

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
    
    def is_password(self, password):
        return self._password == password

    @property
    def bmi(self):
        return self._bmi
    
    # a setter function, allows name to be updated after initial object creation
    @bmi.setter
    def bmi(self, bmi):
        self._bmi = bmi

    @property
    def monday(self):
        return self._monday
    
    # a setter function, allows name to be updated after initial object creation
    @monday.setter
    def monday(self, monday):
        self._monday = monday

    @property
    def tuesday(self):
        return self._tuesday
    
    # a setter function, allows name to be updated after initial object creation
    @tuesday.setter
    def tuesday(self, tuesday):
        self._tuesday = tuesday

    @property
    def wednesday(self):
        return self._wednesday
    
    # a setter function, allows name to be updated after initial object creation
    @wednesday.setter
    def wednesday(self, wednesday):
        self._wednesday = wednesday

    @property
    def thursday(self):
        return self._thursday
    
    # a setter function, allows name to be updated after initial object creation
    @thursday.setter
    def thursday(self, thursday):
        self._thursday = thursday
    
    @property
    def friday(self):
        return self._friday
    
    # a setter function, allows name to be updated after initial object creation
    @friday.setter
    def friday(self, friday):
        self._friday = friday

    @property
    def saturday(self):
        return self._saturday
    
    # a setter function, allows name to be updated after initial object creation
    @saturday.setter
    def saturday(self, saturday):
        self._saturday = saturday
    
    @property
    def sunday(self):
        return self._sunday
    
    # a setter function, allows name to be updated after initial object creation
    @sunday.setter
    def sunday(self, sunday):
        self._sunday = sunday

    @property
    def calories(self):
        return self._calories
    
    # a setter function, allows name to be updated after initial object creation
    @calories.setter
    def calories(self, calories):
        self._calories = calories

    @property
    def sport(self):
        return self._sport
    
    # a setter function, allows name to be updated after initial object creation
    @sport.setter
    def sport(self, sport):
        self._sport = sport
    
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
            "bmi": self.bmi,
            "monday": self.monday,
            "tuesday": self.tuesday,
            "wednesday": self.wednesday,
            "thursday": self.thursday,
            "friday": self.friday,
            "calories": self.calories,
            "sport": self.sport
        }



# CRUD update: updates user name, password, phone
    # returns self
    def update(self, username="", password = "", bmi="",monday="",tuesday="",wednesday="",thursday="", friday="", saturday="", sunday="", calories= "", sport=""):
        """only updates values with length"""
        if len(username) > 0:
            self.username = username
        if len(password) > 0:
            self.password = password
        if len(bmi) >= 0:
            self.bmi = bmi
        if len(monday) >= 0:
            self.monday = monday
        if len(tuesday) >= 0:
            self.tuesday = tuesday
        if len(wednesday) >= 0:
            self.wednesday = wednesday
        if len(thursday) >= 0:
            self.thursday = thursday
        if len(friday) >= 0:
            self.friday = friday
        if len(saturday) >= 0:
            self.saturday = saturday
        if len(sunday) >= 0:
            self.sunday = sunday
        if len(calories) >= 0:
            self.calories = calories
        if len(sport) >= 0:
            self.sport = sport
        db.session.commit()
        return self
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = test(username="James", password="1234", bmi="3.6", monday="Bench Press", tuesday="Squat", wednesday="Deadlift", thursday="RDLs", friday="Pushups", saturday="Pullups", sunday="Situps", calories="2140", sport="soccer")
        users = [u1]


        for user in users:
            try:
                '''add a few 1 to 4 notes per user'''
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.username}")