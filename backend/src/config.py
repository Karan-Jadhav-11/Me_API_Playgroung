import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # SQLite configuration
    SQLITE_DB_PATH = os.getenv('SQLITE_DB_PATH', 'me_api.db')
    
    # Other configurations
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME', 'admin')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD', 'password')