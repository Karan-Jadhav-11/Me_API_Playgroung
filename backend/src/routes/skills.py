from flask import Blueprint, request, jsonify
from src.models.profile import Profile

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('/skills/top', methods=['GET'])
def get_top_skills():
    limit = request.args.get('limit', 5, type=int)
    skills = Profile.get_top_skills(limit)
    return jsonify(skills), 200

@skills_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    results = Profile.search(query)
    return jsonify(results), 200