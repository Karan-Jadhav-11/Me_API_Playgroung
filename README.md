# Me-API Playground

A personal API playground that showcases skills, projects, and experience through a RESTful API with a modern web interface. Built with Flask, SQLite, and vanilla JavaScript.

## 🌟 Features

- **RESTful API** with comprehensive endpoints
- **Modern Web Interface** with responsive design
- **SQLite Database** for easy setup and portability
- **Skill Proficiency Visualization** with interactive charts
- **Project Portfolio** with filtering and search capabilities
- **Basic Authentication** for write operations
- **CORS Enabled** for frontend-backend communication

## 🏗️ Architecture

me-api-playground/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── profile.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── profile.py
│   │   │   ├── projects.py
│   │   │   ├── skills.py
│   │   │   └── health.py
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── sqlite_db.py    # REPLACED db.py with sqlite_db.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── helpers.py
│   │   └── config.py
│   ├── requirements.txt
│   ├── seed_data.py           # UPDATED for SQLite
│   └── run.py
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   └── templates/
│       ├── index.html
│       ├── profile.html
│       ├── projects.html
│       └── search.html
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_profile.py
│   ├── test_projects.py
│   ├── test_skills.py
│   └── test_search.py
├── .env
├── .gitignore
├── application.py
├── README.md
├── requirements.txt
└── setup.py


### Technology Stack
- **Backend**: Flask, SQLite, Python
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite with JSON storage
- **Authentication**: HTTP Basic Auth
- **Deployment**: Can be deployed on any WSGI server

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Local Development Setup

1. **Clone and setup the project**
   ```bash
   # Create project directory
   mkdir API_PLAYGRAOUND
   cd API_PLAYGRAOUND
   
   # Create virtual environment
   python -p venv python==3.12
   conda activate venv/
   
### Install dependencies
pip install -r requirements.txt

### Configure environment variables

Create .env file
echo "SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')" > .env
echo "BASIC_AUTH_USERNAME=admin" >> .env
echo "BASIC_AUTH_PASSWORD=password123" >> .env
echo "SQLITE_DB_PATH=me_api.db" >> .env

### Seed the database
python backend/seed_data.py

### Run the application
python application.py

