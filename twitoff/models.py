"""SQLalchemy models for twitoff
$FLASK_APP=twitoff.APP FLASK_ENV=development flask shell
from twitoff.models import DB, User, Tweet
u1=User(username='elonmusk')
t1=Tweet(text='this is a tweet')
DB.session.add(u1)
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """ twitter users that we query and store historical tweets"""
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)

class Tweet(DB.Model):
    """ stores tweets"""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280), nullable=False)
    # use unicode so it can store emoji and extended text
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable = False)
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))