from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from main import main_blueprint
from auth import auth_blueprint
from posts import post_blueprint
from models import db
from models import Person,Post
from flask_login import LoginManager

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all() 

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return Person.query.filter_by(username=username).first()

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
