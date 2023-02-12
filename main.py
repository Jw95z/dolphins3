import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from volumes.__init__ import app, db  # Definitions initialization
from model.jokes import initJokes
import os
# from model.users import initUsers

# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api 
# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(app_projects) # register app pages
@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.before_first_request
def activate_job():
    initJokes()


# this runs the application on the development server
if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    dbfile = os.path.join(basedir, 'sqlite.db')
    print(dbfile)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volumes/sqlite.db'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db.init_app(app) 
    db.app = app 
    # db.create_all() 
    app.run(host='127.0.0.1', debug=True, port=5000)


# db.init_app(app) 
# db.app = app 
# db.create_all() 