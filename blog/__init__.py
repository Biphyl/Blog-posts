from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '704646bd9b607c04e365e4ec63be2502'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# 'postgresql+psycopg2://biron:Biron4745@localhost/blog'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from . import routes