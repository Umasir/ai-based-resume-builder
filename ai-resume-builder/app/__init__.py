from flask import Flask
from .routes import main  # Import the 'main' blueprint

def create_app():
    app = Flask(__name__)
    
    # Register the blueprint
    app.register_blueprint(main)
    
    return app
