from flask import Flask
from flask_cors import CORS
from .config import Config
from .database.sqlite_db import sqlite_db  # Changed import
from .routes.health import health_bp
from .routes.profile import profile_bp
from .routes.projects import projects_bp
from .routes.skills import skills_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    sqlite_db.init_app(app)  # Changed from init_db(app)
    
    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(profile_bp, url_prefix='/api')
    app.register_blueprint(projects_bp, url_prefix='/api')
    app.register_blueprint(skills_bp, url_prefix='/api')
    
    return app