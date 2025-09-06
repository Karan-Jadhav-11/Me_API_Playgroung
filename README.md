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

 ## 📝 Resume

📄 **Karan Jadhav – Data Science Resume**  

- Bachelor of Technology in Computer Science  
- AI/ML Engineer & Data Scientist  
- Skilled in Python, Flask, TensorFlow, Scikit-learn  
- Focused on Machine Learning, Deep Learning, and Generative AI  

👉 [**Download My Resume (PDF)**](https://github.com/karanjadhav1771/me-api-playground/blob/main/assets/Karan_Jadhav_Resume.pdf](https://drive.google.com/file/d/1DcenkTGTBBuQh7yF3lfD9IjUYrr9Bw-P/view?usp=sharing))


## 🏗️ Architecture
```text
me-api-playground/
├── backend/              # Flask API
│   ├── src/
│   │   ├── models/       # Data models
│   │   ├── routes/       # API routes
│   │   ├── database/     # Database configuration
│   │   ├── utils/        # Utilities and helpers
│   │   └── config.py     # Application configuration
│   ├── seed_data.py      # Database seeding script
│   └── requirements.txt  # Python dependencies
├── frontend/             # Web interface
│   ├── templates/        # HTML templates
│   └── static/           # CSS and JavaScript
├── tests/                # Test cases
├── me_api.db             # SQLite database (auto-generated)
├── application.py        # Main application entry point
└── README.md             # This file

```
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
```
#Create .env file
echo "SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')" > .env
echo "BASIC_AUTH_USERNAME=admin" >> .env
echo "BASIC_AUTH_PASSWORD=password123" >> .env
echo "SQLITE_DB_PATH=me_api.db" >> .env
```
### Seed the database
python backend/seed_data.py

### Run the application
python application.py


📊 Database Schema
SQLite Table Structure
SQL
```
CREATE TABLE profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,          -- JSON encoded profile data
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
Profile Data Structure (JSON)
JSON
```
{
  "name": "String",
  "email": "String",
  "location": "String",
  "phone": "String",
  "title": "String",
  "bio": "String",
  "education": [
    {
      "institution": "String",
      "degree": "String",
      "year": "String",
      "cgpa": "String",
      "location": "String"
    }
  ],
  "skills": [
    {
      "name": "String",
      "proficiency": "Number",
      "category": "String"
    }
  ],
  "projects": [
    {
      "title": "String",
      "description": "String",
      "skills": ["String"],
      "technologies": ["String"],
      "achievements": ["String"],
      "links": {
        "github": "String",
        "live": "String"
      }
    }
  ],
  "work": [
    {
      "company": "String",
      "position": "String",
      "duration": "String",
      "description": "String",
      "skills": ["String"],
      "achievements": ["String"]
    }
  ],
  "certifications": [
    {
      "name": "String",
      "issuer": "String",
      "year": "String",
      "link": "String"
    }
  ],
  "links": {
    "github": "String",
    "linkedin": "String",
    "portfolio": "String",
    "resume": "String"
  }
}
```
Get Profile
```
curl -X GET http://localhost:5000/api/profile
Get Projects Filtered by Skill
```

📊 Logging
The application includes built-in logging:
```
import logging
logging.basicConfig(level=logging.INFO)
app.logger.info('Application started successfully')
Logs are output to the console and can be redirected to files in production.
```
### Known Limitations
SQLite Database: Not suitable for high-traffic production environments.

Basic Authentication: Not recommended for public-facing production apps.

File Uploads: Not supported for profile images or project media.

### Future Enhancements
[ ] Add pagination for large datasets

[ ] Implement JWT authentication

[ ] Add file upload support

[ ] Create admin dashboard

[ ] Create mobile app version


### Acknowledgments
Flask community for the excellent web framework

SQLite for the lightweight database solution

Modern CSS techniques for the responsive design

Open source contributors for various Python packages

Note: This project is designed for personal portfolio showcasing and development purposes. For production use, consider implementing additional security measures and using a more robust database system.

### 📞 Connect with Me
LinkedIn | GitHub | Email
