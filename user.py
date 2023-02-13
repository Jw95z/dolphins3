from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

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
            bmi = body.get('bmi')
            monday = body.get('monday')
            tuesday = body.get('tuesday')
            wednesday = body.get('wednesday')
            thursday = body.get('thursday')
            friday = body.get('friday')
            saturday = body.get('saturday')
            sunday = body.get('sunday')
            calories = body.get('calories')
            sport = body.get('sport')
            ''' #1: Key code block, setup USER OBJECT '''
            uo = test(username=username, 
                      password=password, 
                      bmi=bmi, 
                      monday=monday, 
                      tuesday=tuesday, 
                      wednesday=wednesday, 
                      thursday=thursday, 
                      friday=friday, 
                      saturday=saturday, 
                      sunday=sunday, 
                      calories=calories, 
                      sport=sport)
            
            ''' Additional garbage error checking '''
            # set password if provided
            
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
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Security, '/match')