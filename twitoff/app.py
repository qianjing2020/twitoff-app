''' Note: to automatic reload flask when file change, run this command line at the terminal: 
$ FLASK_APP=twitoff:APP FLASK_ENV=development flask run 
'''
from decouple import config # This will get defined variables from .env file
import uuid
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
    #create and config an instance of the flask application
    app = Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['ENV']= config('ENV') # remove before deploying
    DB.init_app(app)
    
    @app.route('/')
    def index():
        rand_name = str(uuid.uuid4())
        rand_user = User(name = rand_name)
        DB.session.add(rand_user)
        DB.session.commit()
        return 'Index Page'

    @app.route('/hello')
    def hello():
        users = User.query.all()
        return render_template('base.html', title="Home", users=users)
    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset', users=[])
        
    return app


#if __name__== "__main__":
#    app.run(debug=True, port = 8080)