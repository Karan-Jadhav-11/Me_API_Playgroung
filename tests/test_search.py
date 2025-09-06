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
                "email": "test@example.com",
                "education": [
                    {
                        "institution": "Test University",
                        "degree": "Bachelor of Science in Computer Science",
                        "year": "2020-2024"
                    }
                ],
                "skills": [
                    {"name": "Python", "proficiency": 90},
                    {"name": "JavaScript", "proficiency": 85}
                ],
                "projects": [
                    {
                        "title": "Python Project",
                        "description": "A project using Python and Flask",
                        "skills": ["Python", "Flask"]
                    }
                ],
                "work": [
                    {
                        "company": "Test Company",
                        "position": "Software Developer",
                        "duration": "2023-Present",
                        "description": "Developing Python applications"
                    }
                ]
            }
            mongo.db.profile.insert_one(test_profile)
        yield client

def test_search_by_skill(client):
    response = client.get('/api/search?q=python')
    assert response.status_code == 200
    data = response.json
    assert len(data['skills']) >= 1
    assert len(data['projects']) >= 1
    assert any(skill['name'].lower() == 'python' for skill in data['skills'])

def test_search_by_project(client):
    response = client.get('/api/search?q=flask')
    assert response.status_code == 200
    data = response.json
    assert len(data['projects']) >= 1
    assert any('flask' in project['skills'] for project in data['projects'])

def test_search_by_education(client):
    response = client.get('/api/search?q=university')
    assert response.status_code == 200
    data = response.json
    assert 'education' in data['profile']
    assert len(data['profile']['education']) >= 1

def test_search_by_work(client):
    response = client.get('/api/search?q=developer')
    assert response.status_code == 200
    data = response.json
    assert 'work' in data['profile']
    assert len(data['profile']['work']) >= 1

def test_search_no_results(client):
    response = client.get('/api/search?q=nonexistent')
    assert response.status_code == 200
    data = response.json
    assert len(data['skills']) == 0
    assert len(data['projects']) == 0
    assert not any(bool(v) for v in data['profile'].values())