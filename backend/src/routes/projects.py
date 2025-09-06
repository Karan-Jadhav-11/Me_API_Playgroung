from flask import Blueprint, request, jsonify
from src.models.profile import Profile

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    skill = request.args.get('skill')
    
    if skill:
        projects = Profile.get_projects_by_skill(skill)
    else:
        profile = Profile.get_profile()
        projects = profile.get('projects', []) if profile else []
    
    return jsonify(projects), 200