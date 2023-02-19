from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from users import test

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

class UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            username = body.get('username')
            password = body.get('password')
            monday = body.get('monday')
            tuesday = body.get('tuesday')
            wednesday = body.get('wednesday')
            thursday = body.get('thursday')
            friday = body.get('friday')
            saturday = body.get('saturday')
            sunday = body.get('sunday')
            sex = body.get('sex')
            height = body.get('height')
            weight = body.get('weight')
            sport = body.get('sport')
            maxcal = body.get('maxcal')
            dob = body.get('dob')
            ''' #1: Key code block, setup USER OBJECT '''
            uo = test(username=username, 
                      password=password, 
                      monday=monday, 
                      tuesday=tuesday, 
                      wednesday=wednesday, 
                      thursday=thursday, 
                      friday=friday, 
                      saturday=saturday, 
                      sunday=sunday,
                      sex = sex,
                      weight=weight, 
                      height = height,
                      sport = sport,
                      maxcal = maxcal,
                      dob=dob)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if dob is not None:
                try:
                    uo.dob = datetime.strptime(dob, '%Y-%m-%d').date()
                except:
                    return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 400
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {username}, either a format error or User ID {username} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = test.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    class _Security(Resource):

        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            ''' Get Data '''
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 400
            password = body.get('password')
            ''' Find user '''
            user = test.query.filter_by(_username=username).first()
            if user is None or not user.is_password(password):
                return {'message': f"Invalid user id or password"}, 400  
            ''' authenticated user '''
            return jsonify(user.read())
    class _Calender(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            return jsonify(user.read())
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Security, '/match')
    api.add_resource(_Calender, '/calender')