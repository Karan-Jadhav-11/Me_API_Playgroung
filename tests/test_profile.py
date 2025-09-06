import pytest
from src.app import create_app
from src.database.db import mongo

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_me_api'
    
    with app.test_client() as client:
        with app.app_context():
            # Clear test database
            mongo.db.profile.delete_many({})
        yield client

def test_get_profile_empty(client):
    response = client.get('/api/profile')
    assert response.status_code == 404

def test_create_and_get_profile(client):
    # Create profile
    profile_data = {
        "name": "Test User",
        "email": "test@example.com",
        "skills": ["Python", "JavaScript"]
    }
    
    response = client.post('/api/profile', json=profile_data)
    assert response.status_code == 201
    
    # Get profile
    response = client.get('/api/profile')
    assert response.status_code == 200
    data = response.json
    assert data['name'] == "Test User"
    assert data['email'] == "test@example.com"