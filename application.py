# from flask import Flask, render_template, jsonify
# import os
# import sys

# # Add backend to path
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# # Import backend components
# from backend.src.database.sqlite_db import sqlite_db
# from backend.src.routes.health import health_bp
# from backend.src.routes.profile import profile_bp
# from backend.src.routes.projects import projects_bp
# from backend.src.routes.skills import skills_bp

# # Create app
# app = Flask(__name__, 
#             template_folder='frontend/templates',
#             static_folder='frontend/static')

# # Configure app
# app.config['SQLITE_DB_PATH'] = 'me_api.db'
# app.config['SECRET_KEY'] = 'your-secret-key'  # From .env

# # Initialize database
# sqlite_db.init_app(app)

# # Register blueprints
# app.register_blueprint(health_bp)
# app.register_blueprint(profile_bp, url_prefix='/api')
# app.register_blueprint(projects_bp, url_prefix='/api')
# app.register_blueprint(skills_bp, url_prefix='/api')

# # Frontend routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

# @app.route('/projects')
# def projects():
#     return render_template('projects.html')

# @app.route('/search')
# def search():
#     return render_template('search.html')

# if __name__ == '__main__':
#     print("🚀 Starting Me-API Playground...")
#     print("📊 Database: me_api.db")
#     print("🌐 Server: http://localhost:5000")
#     print("📋 API: http://localhost:5000/api/profile")
#     print("❤️ Health: http://localhost:5000/health")
#     app.run(debug=True, host='0.0.0.0', port=5000)



from flask import Flask, render_template, jsonify
import os
import sys

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Import backend components
from backend.src.database.sqlite_db import sqlite_db
from backend.src.models.profile import Profile

# Create app
app = Flask(__name__, 
            template_folder='frontend/templates',
            static_folder='frontend/static')

# Configure app
app.config['SQLITE_DB_PATH'] = 'me_api.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Initialize database
sqlite_db.init_app(app)

# API Routes
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/profile')
def get_profile_api():
    profile = Profile.get_profile()
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    return jsonify(profile)

@app.route('/api/projects')
def get_projects_api():
    profile = Profile.get_profile()
    if not profile or 'projects' not in profile:
        return jsonify([])
    return jsonify(profile.get('projects', []))

@app.route('/api/skills/top')
def get_top_skills_api():
    skills = Profile.get_top_skills(limit=10)
    return jsonify(skills)

@app.route('/api/search')
def search_api():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    results = Profile.search(query)
    return jsonify(results)

# Frontend Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    print("🚀 Starting Me-API Playground...")
    print("📊 Database: me_api.db")
    print("🌐 Server: http://localhost:5000")
    print("👤 Profile: http://localhost:5000/profile")
    print("🚀 Projects: http://localhost:5000/projects")
    print("🔍 Search: http://localhost:5000/search")
    print("❤️ Health: http://localhost:5000/health")
    app.run(debug=True, host='0.0.0.0', port=5000)