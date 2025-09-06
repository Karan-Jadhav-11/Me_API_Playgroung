from flask import Blueprint, request, jsonify
from src.models.profile import Profile
from src.utils.auth import requires_auth

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    profile = Profile.get_profile()
    if not profile:
        return jsonify({'error': 'Profile not found'}), 404
    return jsonify(profile), 200

@profile_bp.route('/profile', methods=['POST'])
@requires_auth
def create_profile():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = Profile.create_profile(data)
    return jsonify({'message': 'Profile created', 'id': str(result.inserted_id)}), 201

@profile_bp.route('/profile', methods=['PUT'])
@requires_auth
def update_profile():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = Profile.update_profile(data)
    if result.modified_count == 0:
        return jsonify({'error': 'Profile not found or no changes made'}), 404
    
    return jsonify({'message': 'Profile updated'}), 200