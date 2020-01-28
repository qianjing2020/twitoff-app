''' Note: to automatic reload flask when file change, run this command line at the terminal: 
$ FLASK_APP=hello.py FLASK_ENV=development flask run --port 8080
'''

from flask import Flask, escape, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Index page"

    @app.route('/user/<username>') # pass argument in < >
    def show_user(username):
        return f'User:{username}'

    @app.route('/hello') 
    def hello():
        #deployed model goes here
        name = request.args.get("name", "Ana")
        #return f'Hello, {escape(name)}!'
        return """hello, world! """

    return app


if __name__== "__main__":
    app.run(debug=True, port = 8080)

