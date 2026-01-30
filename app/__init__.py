from flask import Flask

def create_app():
    # Initialize Flask object
    app = Flask(__name__)

    # Configuration
    # Limit uploads to 16MB to prevent any crash
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # Define where uploads will be stored
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Import and register blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app