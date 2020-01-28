''' Note: to automatic reload flask when file change, run this command line at the terminal: 
$ FLASK_APP=hello.py FLASK_ENV=development flask run --port 8080
'''

from flask import Flask, escape, request
#The Flask class will allow us to instantiate our own Flask applications!
app = Flask(__name__)#the name of the module the execution is occurring in

@app.route('/')
def index():
    return "Index page"

@app.route('/user/<username>') # pass argument in < >
def show_user(username):
    return f'User:{username}'

@app.route('/ana') #routing requests to the base / route, this is actually a function takes a function
def hello():
    #deployed model goes here
    name = request.args.get("name", "Ana")
    #return f'Hello, {escape(name)}!'
    return """<h1><font color = "red"> Ana: </h1>
    <br>
    <h2><font color="blue"><b>hi mama silly billy goo goo!</b></font></h2>
    <br>
    <img src="http://images1.bestpetsonline.us/nlarge/baby-lionhead-bunnies_19118589.jpg" alt="Smiley face" heitht="300" width="300">
    
    
    
    """


if __name__== "__main__":
    app.run(debug=True, port = 8080)

