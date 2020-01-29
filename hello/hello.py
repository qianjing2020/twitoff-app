""" 
$FLASK_APP=hello.py FLASK_ENV=development flask run
"""

from flask import Flask
from flask import render_template

app = Flask(__name__) # create a flask class instance 

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello') # use route() decorator to tell flask what url triggers function
@app.route('/hello/<name>')
def hello(name=None): #the function is given a name which is also used to generate url for that funciton and also return a message
    return render_template('hello.html', name=name)
