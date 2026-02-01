from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    # We define the table name for clarity
    __tablename__ = 'users'

    # Define the columns for the users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # This prevents the password from being accessed directly
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')
    
    # This generates the password hash when setting the password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # This verifies the password against the stored hash
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# We need to tell Flask-Login how to load a user from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))