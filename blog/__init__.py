from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '704646bd9b607c04e365e4ec63be2502'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# 'postgresql+psycopg2://biron:Biron4745@localhost/blog'

db = SQLAlchemy(app)


from . import routes