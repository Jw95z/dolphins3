from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from users import test
from __init__ import db, app
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
    class _findUsername(Resource):
        def get(self):
            usernames = []
            users = test.query.all()
            username = [user.read() for user in users]
            for i in range(len(username)):
                usernames.append({"username": username[i]['username'], "password": username[i]['password']})
            return jsonify(usernames)
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
            users = user.read()
            return jsonify(users)
    class _Calender_monday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            monday = body.get('monday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if monday is None:
                return {'message': f'Monday is missing'}, 400   
            user = test.query.filter_by(_username=username).first()
            user.monday +=  " " + monday
            db.session.commit()
            return jsonify(user.read())
    class _Calender_tuesday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            tuesday = body.get('tuesday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if tuesday is None:
                return {'message': f'Tuesday is missing'}, 400   
            user = test.query.filter_by(_username=username).first()
            user.tuesday += " " + tuesday
            db.session.commit()
            return jsonify(user.read())
    class _Calender_wednesday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            wednesday = body.get('wednesday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if wednesday is None:
                return {'message': f'Wednesday is missing'}, 400   
            user = test.query.filter_by(_username=username).first()
            user.wednesday += " " + wednesday
            db.session.commit()
            return jsonify(user.read())

    class _Calender_thursday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            thursday = body.get('thursday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if thursday is None:
                return {'message': f'Thursday is missing'}, 400   
            user = test.query.filter_by(_username=username).first()
            user.thursday += " " + thursday
            db.session.commit()
            return jsonify(user.read())
    class _Calender_friday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            friday = body.get('friday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if friday is None:
                return {'message': f'Friday is missing'}, 400   
            user = test.query.filter_by(_username=username).first()
            user.friday += " " + friday
            db.session.commit()
            return jsonify(user.read())

    class _Calender_saturday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            saturday = body.get('saturday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if saturday is None:
                return {'message': f'Saturday is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.saturday += " " + saturday
            
            db.session.commit()
            return jsonify(user.read())
    
    class _Calender_sunday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            sunday = body.get('sunday')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if sunday is None:
                return {'message': f'Sunday is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.sunday += " " + sunday
            db.session.commit()
            return jsonify(user.read())
    class _delete_monday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.monday = ""
            db.session.commit()
            return jsonify(user.read())
    class _delete_tuesday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.tuesday = ""
            db.session.commit()
            return jsonify(user.read())
    class _delete_wednesday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.wednesday = ""
            db.session.commit()
            return jsonify(user.read())
    class _delete_thursday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.thursday = ""
            db.session.commit()
            return jsonify(user.read())
    class _delete_friday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.friday = ""
            db.session.commit()
            return jsonify(user.read())
    class _delete_saturday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.saturday = ""
            db.session.commit()
            return jsonify(user.read())
    class _delete_sunday(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.sunday = ""
            db.session.commit()
            return jsonify(user.read())
        
    class _Sex(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            sex = body.get('sex')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if sex is None:
                return {'message': f'Saturday is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.sex = sex
            db.session.commit()
            return jsonify(user.read())
    class _Maxcal(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            maxcal = body.get('maxcal')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if maxcal is None:
                return {'message': f'Saturday is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.maxcal = maxcal
            db.session.commit()
            return jsonify(user.read())
    class _weight(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            weight = body.get('weight')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if weight is None:
                return {'message': f'Saturday is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.weight += weight
            db.session.commit()
            return jsonify(user.read())
    class _height(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            height = body.get('sex')
            if username is None:
                return {'message': f'User ID is missing'}, 400
            if height is None:
                return {'message': f'Saturday is missing'}, 400
            user = test.query.filter_by(_username=username).first()
            user.height += height
            db.session.commit()
            return jsonify(user.read())
        
        
        
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Security, '/match')
    api.add_resource(_Calender, '/calender')
    api.add_resource(_Calender_monday, '/monday')
    api.add_resource(_Calender_tuesday, '/tuesday')
    api.add_resource(_Calender_wednesday, '/wednesday')
    api.add_resource(_Calender_thursday, '/thursday')
    api.add_resource(_Calender_friday, '/friday')
    api.add_resource(_Calender_saturday, '/saturday')
    api.add_resource(_Calender_sunday, '/sunday')
    api.add_resource(_delete_monday, '/delete_monday')
    api.add_resource(_delete_tuesday, '/delete_tuesday')
    api.add_resource(_delete_wednesday, '/delete_wednesday')
    api.add_resource(_delete_thursday, '/delete_thursday')
    api.add_resource(_delete_friday, '/delete_friday')
    api.add_resource(_delete_saturday, '/delete_saturday')
    api.add_resource(_delete_sunday, '/delete_sunday')
    api.add_resource(_findUsername, '/username')
    api.add_resource(_Sex, '/sex')
    api.add_resource(_Maxcal, '/maxcal')
    api.add_resource(_weight, '/weight')
    api.add_resource(_height, '/height')
    
