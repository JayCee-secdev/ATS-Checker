from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate() # <--- 1. Create the Migrate instance here

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'dev-key-please-change-me'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///raccoon.db'
    
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db) # <--- 3. Initialize it with app and db

    from app.routes import main
    app.register_blueprint(main)
    
    from app import models # Ensure models are imported for migrations

    return app