"""SQLalchemy models for twitoff
$FLASK_APP=twitoff.APP FLASK_ENV=development flask shell

from twitoff.models import DB, User, Tweet
t1=Tweet(text='my first tweet')
t2 =Tweet(text='my second tweet')
u1=User(username='jing')
u1.tweets.append(t1)
u1.tweets.append(t2)
DB.session.add(u1)
DB.session.commit()

"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """ twitter users that we query and store historical tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), unique=True, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """ stores tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300), nullable=False)
    # use unicode so it can store emoji and extended text
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable = False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
