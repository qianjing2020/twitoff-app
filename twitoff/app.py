''' Note: to automatic reload flask when file change, run this command line at the terminal: 
$ FLASK_APP=twitoff:APP FLASK_ENV=development flask run 
'''
# from decouple import config
import uuid
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
    #create and config an instance of the flask application
    app = Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.sqlite'
    DB.init_app(app)
    
    @app.route('/')
    def index():
        rand_name = str(uuid.uuid4())
        rand_user = User(username = rand_name)
        DB.session.add(rand_user)
        DB.session.commit()
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return render_template('hello.html', title="Welcome to TwitOff!")
    
    return app


#if __name__== "__main__":
#    app.run(debug=True, port = 8080)