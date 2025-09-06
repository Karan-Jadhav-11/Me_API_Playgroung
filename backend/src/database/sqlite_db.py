import sqlite3
import json
from datetime import datetime

class SQLiteDB:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        self.db_path = app.config.get('SQLITE_DB_PATH', 'me_api.db')
        self._init_db()
    
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create profile table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS profile (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
    
    def get_profile(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT data FROM profile ORDER BY id DESC LIMIT 1')
                result = cursor.fetchone()
                
                if result:
                    return json.loads(result[0])
                return None
        except Exception as e:
            print(f"Error getting profile: {e}")
            return None
    
    def create_profile(self, profile_data):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Clear existing data
                cursor.execute('DELETE FROM profile')
                
                # Insert new data
                cursor.execute(
                    'INSERT INTO profile (data) VALUES (?)',
                    (json.dumps(profile_data),)
                )
                
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            print(f"Error creating profile: {e}")
            return None
    
    def update_profile(self, update_data):
        try:
            current_profile = self.get_profile()
            if not current_profile:
                return False
            
            # Merge updates
            for key, value in update_data.items():
                current_profile[key] = value
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'UPDATE profile SET data = ?, updated_at = CURRENT_TIMESTAMP WHERE id = (SELECT id FROM profile ORDER BY id DESC LIMIT 1)',
                    (json.dumps(current_profile),)
                )
                
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating profile: {e}")
            return False

# Create global instance
sqlite_db = SQLiteDB()