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
    _monday = db.Column(db.String(255), unique=False, nullable=False)
    _tuesday = db.Column(db.String(255), unique=False, nullable=False)
    _wednesday = db.Column(db.String(255), unique=False, nullable=False)
    _thursday = db.Column(db.String(255), unique=False, nullable=False)
    _friday = db.Column(db.String(255), unique=False, nullable=False)
    _saturday = db.Column(db.String(255), unique=False, nullable=False)
    _sunday = db.Column(db.String(255), unique=False, nullable=False)
    _sex = db.Column(db.String(255), unique=False, nullable=False)
    _height = db.Column(db.String(255), unique=False, nullable=False)
    _weight = db.Column(db.String(255), unique=False, nullable=False)
    _sport = db.Column(db.String(255), unique=False, nullable=False)
    _maxcal = db.Column(db.String(255), unique=False, nullable=False)
    _dob = db.Column(db.Date)
    def __init__(self, username, password, monday, tuesday, wednesday, thursday, friday, saturday, sport, sunday, sex, weight, height, maxcal ,dob = date.today()):
        self._username = username
        self._password = password
        self._monday = monday
        self._tuesday = tuesday
        self._wednesday = wednesday
        self._thursday = thursday
        self._friday = friday
        self._saturday = saturday
        self._sunday = sunday
        self._sex = sex
        self._weight = weight
        self._height = height
        self._dob = dob
        self._sport = sport
        self._maxcal = maxcal

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
    def dob(self):
        dob_string = self._dob.strftime('%m-%d-%Y')
        return dob_string
    
    # dob should be have verification for type date
    @dob.setter
    def dob(self, dob):
        self._dob = dob
    
    @property
    def age(self):
        today = date.today()
        return today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
 
    @property
    def sex(self):
        return self._sex
    
    # a setter function, allows name to be updated after initial object creation
    @sex.setter
    def sex(self, sex):
        self._sex = sex

    @property
    def weight(self):
        return self._weight
    
    # a setter function, allows name to be updated after initial object creation
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def height(self):
        return self._height
    
    # a setter function, allows name to be updated after initial object creation
    @height.setter
    def height(self, height):
        self._height = height

    @property
    def sport(self):
        return self._sport
    
    # a setter function, allows name to be updated after initial object creation
    @sport.setter
    def sport(self, sport):
        self._sport = sport
    
    @property
    def maxcal(self):
        return self._maxcal
    
    # a setter function, allows name to be updated after initial object creation
    @maxcal.setter
    def maxcal(self, maxcal):
        self._maxcal = maxcal
    
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
            "monday": self.monday,
            "tuesday": self.tuesday,
            "wednesday": self.wednesday,
            "thursday": self.thursday,
            "friday": self.friday,
            "saturday": self.saturday,
            "sunday": self.sunday,
            "sex": self.sex,
            "weight": self.weight,
            "height": self.height,
            "sport": self.sport,
            "maxcal": self.maxcal,
            "dob": self.dob,
            "age": self.age
        }



# CRUD update: updates user name, password, phone
    # returns self
    def update(self, username="", password = "", monday="", tuesday="", wednesday="", thursday="", friday="", saturday="", sunday="", sex = "", weight = "", height="", sport = "", maxcal = "", dob=""):
        """only updates values with length"""
        if len(username) > 0:
            self.username = username
        if len(password) > 0:
            self.password = password
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
        if len(sex) >= 0:
            self.sex = sex
        if len(weight) >= 0:
            self.weight = weight
        if len(height) >= 0:
            self.height = height
        if len(sport) >= 0:
            self.sport = sport
        if len(maxcal) >= 0:
            self.maxcal = maxcal
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
        u1 = test(username="James", password="1234", monday="Bench Press", tuesday="Squat", wednesday="Pullups", thursday="Situps", friday="Pushups", saturday="Run", sunday="Deadlift", sex = "male", weight= "", height="", sport = "", maxcal="", dob=date(1847, 2, 11))
        users = [u1]


        for user in users:
            try:
                '''add a few 1 to 4 notes per user'''
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.username}")