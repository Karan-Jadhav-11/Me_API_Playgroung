# # ... (your existing imports)

# def seed_database():
#     app = create_app()
    
#     with app.app_context():
#         try:
#             # Sample profile data - REPLACE WITH YOUR ACTUAL INFORMATION
#             profile_data = {
#                 "name": "Karan Jadhav",  # ← Change to your name
#                 "email": "karanjadhav11@example.com",  # ← Change to your email
#                 "education": [
#                     {
#                         "institution": "Your University Name",
#                         "degree": "Bachelor of Science in Computer Science",
#                         "year": "2020-2024"
#                     }
#                 ],
#                 "skills": [
#                     {"name": "Python", "proficiency": 90},
#                     {"name": "JavaScript", "proficiency": 85},
#                     {"name": "Flask", "proficiency": 80},
#                     {"name": "React", "proficiency": 75},
#                     {"name": "MongoDB", "proficiency": 85},
#                     {"name": "SQL", "proficiency": 70},
#                     {"name": "Machine Learning", "proficiency": 80}
#                 ],
#                 "projects": [
#                     {
#                         "title": "Diamond Price Prediction",
#                         "description": "ML model to predict diamond prices based on various features",
#                         "skills": ["Python", "Machine Learning", "Flask", "Data Analysis"],
#                         "links": {
#                             "github": "https://github.com/yourusername/diamond-price-prediction",
#                             "live": "https://your-diamond-app.herokuapp.com"
#                         }
#                     },
#                     {
#                         "title": "Me-API Playground",
#                         "description": "Personal API playground to showcase skills and projects",
#                         "skills": ["Python", "Flask", "REST API", "JavaScript", "SQLite"],
#                         "links": {
#                             "github": "https://github.com/yourusername/me-api-playground"
#                         }
#                     },
#                     {
#                         "title": "E-Commerce Website",
#                         "description": "Full-stack e-commerce platform with React and Node.js",
#                         "skills": ["React", "Node.js", "Express", "MongoDB"],
#                         "links": {
#                             "github": "https://github.com/yourusername/ecommerce-app",
#                             "live": "https://your-ecommerce-app.vercel.app"
#                         }
#                     }
#                 ],
#                 "work": [
#                     {
#                         "company": "Tech Innovators Inc.",
#                         "position": "AI/ML Intern",
#                         "duration": "Summer 2023 - Present",
#                         "description": "Working on machine learning models and data pipelines for predictive analytics"
#                     },
#                     {
#                         "company": "Web Solutions Ltd.",
#                         "position": "Web Developer",
#                         "duration": "2022 - 2023",
#                         "description": "Developed responsive web applications using modern frameworks"
#                     }
#                 ],
#                 "links": {
#                     "github": "https://github.com/yourusername",
#                     "linkedin": "https://linkedin.com/in/yourprofile",
#                     "portfolio": "https://yourportfolio.com"
#                 }
#             }
            
#             # Create profile using SQLite
#             result = sqlite_db.create_profile(profile_data)
            
#             if result:
#                 print(f"✅ SQLite database seeded successfully with profile ID: {result}")
#                 print(f"✅ Database file created: me_api.db")
#             else:
#                 print("❌ Error seeding database")
                
#         except Exception as e:
#             print(f"❌ Error seeding database: {e}")


import os
import sys
from dotenv import load_dotenv

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.app import create_app
from src.database.sqlite_db import sqlite_db

# Load environment variables
load_dotenv()

def seed_database():
    app = create_app()
    
    with app.app_context():
        try:
            # YOUR ACTUAL INFORMATION - based on your resume
            profile_data = {
                "name": "Karan Jadhav",
                "email": "karanjadhav1771@gmail.com",
                "location": "Bengaluru, Karnataka",
                "phone": "+91 8262973414",
                "title": "AI/ML Engineer & Data Scientist",
                "bio": "Spearheaded the development and deployment of machine learning models using Scikit-learn, TensorFlow, and Keras. Expert in Deep Learning, NLP, and Generative AI.",
                
                "education": [
                    {
                        "institution": "Government College of Engineering Amravati",
                        "degree": "Bachelor of Technology in Computer Science",
                        "year": "2021 - 2025",
                        "cgpa": "7.54",
                        "location": "Maharashtra, India"
                    }
                ],
                
                "skills": [
                    {"name": "Python", "proficiency": 90, "category": "Programming"},
                    {"name": "SQL", "proficiency": 85, "category": "Programming"},
                    {"name": "C++", "proficiency": 80, "category": "Programming"},
                    {"name": "Machine Learning", "proficiency": 88, "category": "AI/ML"},
                    {"name": "Deep Learning", "proficiency": 85, "category": "AI/ML"},
                    {"name": "Generative AI", "proficiency": 82, "category": "AI/ML"},
                    {"name": "NLP", "proficiency": 80, "category": "AI/ML"},
                    {"name": "Predictive Analytics", "proficiency": 85, "category": "AI/ML"},
                    {"name": "EDA", "proficiency": 87, "category": "Data Analysis"},
                    {"name": "Feature Engineering", "proficiency": 86, "category": "Data Analysis"},
                    {"name": "Statistics", "proficiency": 84, "category": "Data Analysis"},
                    {"name": "Scikit-learn", "proficiency": 88, "category": "Frameworks"},
                    {"name": "TensorFlow", "proficiency": 83, "category": "Frameworks"},
                    {"name": "Keras", "proficiency": 82, "category": "Frameworks"},
                    {"name": "Flask", "proficiency": 85, "category": "Frameworks"},
                    {"name": "Git", "proficiency": 87, "category": "Tools"},
                    {"name": "Power BI", "proficiency": 80, "category": "Visualization"},
                    {"name": "Tableau", "proficiency": 78, "category": "Visualization"},
                    {"name": "Matplotlib", "proficiency": 85, "category": "Visualization"},
                    {"name": "Seaborn", "proficiency": 84, "category": "Visualization"},
                    {"name": "MongoDB", "proficiency": 80, "category": "Database"},
                    {"name": "MySQL", "proficiency": 82, "category": "Database"},
                    {"name": "PostgreSQL", "proficiency": 79, "category": "Database"}
                ],
                
                "projects": [
                    {
                        "title": "Object Classification System",
                        "description": "Developed a deep learning model using TensorFlow and Keras, achieving over 92% Training accuracy and 85% validation accuracy in classifying 47 animal species. Engineered a Flask REST API for real-time prediction and similarity search.",
                        "skills": ["Python", "TensorFlow", "Keras", "Flask", "Computer Vision", "Deep Learning"],
                        "technologies": ["Python", "TensorFlow", "Keras", "Flask", "OpenCV"],
                        "achievements": ["92%+ Training accuracy", "85% Validation accuracy", "Real-time prediction API"],
                        "links": {
                            "github": "https://github.com/karanjadhav11/object-classification-system"
                        }
                    },
                    {
                        "title": "Diabetes Patient Classification Using ML",
                        "description": "Built a predictive analytics model using Logistic Regression, Random Forest, and XGBoost, achieving over 85% accuracy for diabetes patient classification. Performed comprehensive data wrangling and feature engineering.",
                        "skills": ["Python", "Scikit-learn", "Machine Learning", "Data Analysis", "Feature Engineering"],
                        "technologies": ["Python", "Scikit-learn", "Flask", "Pandas", "Matplotlib"],
                        "achievements": ["85%+ accuracy", "Feature importance analysis", "Flask API deployment"],
                        "links": {
                            "github": "https://github.com/karanjadhav11/diabetes-classification"
                        }
                    },
                    {
                        "title": "Diamond Price Prediction Using ML",
                        "description": "Developed a machine learning model achieving 95%+ accuracy to predict diamond prices using key attributes. Designed an end-to-end data pipeline including preprocessing, model training, evaluation, and visualization.",
                        "skills": ["Python", "Machine Learning", "EDA", "Flask", "Data Visualization"],
                        "technologies": ["Python", "Scikit-learn", "Flask", "Seaborn", "Plotly"],
                        "achievements": ["95%+ accuracy", "End-to-end pipeline", "Real-time prediction API"],
                        "links": {
                            "github": "https://github.com/karanjadhav11/diamond-price-prediction"
                        }
                    }
                ],
                
                "work": [
                    {
                        "company": "Trainity",
                        "position": "Data Analytics Intern",
                        "duration": "2023 - Present",
                        "description": "Gained hands-on experience in data wrangling, EDA, and statistical analysis, leveraging SQL and Python for robust data manipulation. Created insightful dashboards and visualizations using Tableau and Power BI.",
                        "skills": ["SQL", "Python", "Data Analysis", "Tableau", "Power BI", "Data Visualization"],
                        "achievements": ["Data-driven reports", "Business insights", "Dashboard creation"]
                    }
                ],
                
                "certifications": [
                    {
                        "name": "Data Science Master",
                        "issuer": "Physics Wallah",
                        "year": "2023",
                        "link": "#"
                    },
                    {
                        "name": "Data Analytics Training",
                        "issuer": "Trainity",
                        "year": "2023",
                        "link": "#"
                    }
                ],
                
                "links": {
                    "github": "https://github.com/karanjadhav11",
                    "linkedin": "https://linkedin.com/in/karan-jadhav",
                    "portfolio": "#",
                    "resume": "#"
                }
            }
            
            # Create profile using SQLite
            result = sqlite_db.create_profile(profile_data)
            
            if result:
                print(f"✅ SQLite database seeded successfully with profile ID: {result}")
                print(f"✅ Profile Name: {profile_data['name']}")
                print(f"✅ Email: {profile_data['email']}")
                print(f"✅ Skills: {len(profile_data['skills'])} skills added")
                print(f"✅ Projects: {len(profile_data['projects'])} projects added")
                print(f"✅ Database file: me_api.db")
                
                # Verify the data was saved correctly
                saved_profile = sqlite_db.get_profile()
                if saved_profile:
                    print(f"✅ Verification: Successfully retrieved profile for {saved_profile.get('name')}")
                else:
                    print("❌ Verification: Could not retrieve saved profile")
            else:
                print("❌ Error seeding database")
                
        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    seed_database()