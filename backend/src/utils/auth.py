from flask import request, jsonify
from functools import wraps
from src.config import Config

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == Config.BASIC_AUTH_USERNAME and auth.password == Config.BASIC_AUTH_PASSWORD):
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated