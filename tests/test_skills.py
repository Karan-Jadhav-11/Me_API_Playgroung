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
            
            # Insert test data
            test_profile = {
                "name": "Test User",
                "skills": [
                    {"name": "Python", "proficiency": 90},
                    {"name": "JavaScript", "proficiency": 85},
                    {"name": "Flask", "proficiency": 80},
                    {"name": "React", "proficiency": 75},
                    {"name": "MongoDB", "proficiency": 85},
                    {"name": "SQL", "proficiency": 70}
                ]
            }
            mongo.db.profile.insert_one(test_profile)
        yield client

def test_get_top_skills_default(client):
    response = client.get('/api/skills/top')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 5  # Default limit
    # Should be sorted by proficiency descending
    assert data[0]['name'] == "Python"
    assert data[0]['proficiency'] == 90
    assert data[1]['name'] == "JavaScript"
    assert data[1]['proficiency'] == 85

def test_get_top_skills_with_limit(client):
    response = client.get('/api/skills/top?limit=3')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 3
    assert data[0]['name'] == "Python"
    assert data[2]['name'] == "Flask"