from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import pickle
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Person(UserMixin, db.Model):
    __tablename__ = 'people'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post',backref='people',lazy=True)

    def set_password(self, password):
        return generate_password_hash(password, method='sha256')

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'password': self.password
        }
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    
    def check_password(self,password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    __tablename__  = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    complete_post = db.Column(db.String(), nullable=False)
    publisher = db.Column(db.String(),nullable=False)
    likes = db.Column(db.Integer,default=0)
    person = db.Column(db.String(),db.ForeignKey(Person.username),nullable=False)
    # people = db.relationship('Person', uselist=True)
    # likers = db.Column(db.String(), db.ForeignKey('people.username'))
    likers = db.Column(db.PickleType())

    def __init__(self,description,complete_post,publisher,likes):
        self.description = description
        self.complete_post = complete_post
        self.publisher = publisher
        self.likes = likes

    def __repr__(self):
        return '<name {}>'.format(self.description)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'complete_post': self.complete_post,
            'publisher': self.publisher,
            'likes': self.likes,
            'likers': self.likers
        }