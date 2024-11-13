from flask import Flask,render_template
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from werkzeug.security import generate_password_hash

import os, importlib

db = SQLAlchemy()
DB_NAME  = 'database.db'


def create_database(app):
    with app.app_context():
        db.create_all()
    print("Database created")


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    
    # Loading bp
    for brp in os.listdir(os.path.dirname('./website/blueprints/')):
        if brp[0]=='_' or brp[-3:] != '.py': continue
        brp=brp[:-3]
        imported = importlib.import_module(f".{brp}", package='website.blueprints')
        if hasattr(imported, 'bp'): app.register_blueprint(getattr(imported,'bp'))

    # create_database(app)

    return app
