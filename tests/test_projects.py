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
                "projects": [
                    {
                        "title": "Python Project",
                        "description": "A project using Python",
                        "skills": ["Python", "Flask"]
                    },
                    {
                        "title": "JavaScript Project",
                        "description": "A project using JavaScript",
                        "skills": ["JavaScript", "React"]
                    }
                ]
            }
            mongo.db.profile.insert_one(test_profile)
        yield client

def test_get_all_projects(client):
    response = client.get('/api/projects')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2
    assert data[0]['title'] == "Python Project"
    assert data[1]['title'] == "JavaScript Project"

def test_get_projects_by_skill(client):
    response = client.get('/api/projects?skill=Python')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 1
    assert data[0]['title'] == "Python Project"
    assert "Python" in data[0]['skills']

def test_get_projects_by_nonexistent_skill(client):
    response = client.get('/api/projects?skill=Ruby')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 0