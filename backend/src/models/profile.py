
from datetime import datetime
from ..database.sqlite_db import sqlite_db

class Profile:
    @staticmethod
    def get_profile():
        try:
            profile = sqlite_db.get_profile()
            if not profile:
                print("❌ No profile found in database")
                return None
            print(f"✅ Retrieved profile: {profile.get('name', 'Unknown')}")
            return profile
        except Exception as e:
            print(f"❌ Error retrieving profile: {e}")
            return None
    
    @staticmethod
    def create_profile(profile_data):
        try:
            result = sqlite_db.create_profile(profile_data)
            if result:
                print(f"✅ Profile created with ID: {result}")
            return result
        except Exception as e:
            print(f"❌ Error creating profile: {e}")
            return None
    
    @staticmethod
    def update_profile(update_data):
        try:
            return sqlite_db.update_profile(update_data)
        except Exception as e:
            print(f"❌ Error updating profile: {e}")
            return False
    
    @staticmethod
    def get_projects_by_skill(skill):
        profile = Profile.get_profile()
        if not profile or 'projects' not in profile:
            return []
        
        return [project for project in profile['projects'] 
                if 'skills' in project and skill.lower() in [s.lower() for s in project['skills']]]
    
    @staticmethod
    def get_top_skills(limit=10):
        profile = Profile.get_profile()
        if not profile or 'skills' not in profile:
            return []
        
        skills = profile['skills']
        # Sort by proficiency if available
        if isinstance(skills[0], dict) and 'proficiency' in skills[0]:
            skills.sort(key=lambda x: x.get('proficiency', 0), reverse=True)
        elif isinstance(skills[0], dict) and 'name' in skills[0]:
            skills.sort(key=lambda x: x.get('name', ''))
        
        return skills[:limit]
    
    @staticmethod
    def search(query):
        profile = Profile.get_profile()
        if not profile:
            return {'profile': {}, 'projects': [], 'skills': []}
        
        results = {
            'profile': {},
            'projects': [],
            'skills': []
        }
        
        query = query.lower()
        
        # Search in basic profile fields
        for field in ['name', 'email', 'bio', 'title']:
            if field in profile and profile[field] and isinstance(profile[field], str):
                if query in profile[field].lower():
                    results['profile'][field] = profile[field]
        
        # Search in education
        if 'education' in profile and profile['education']:
            edu_matches = []
            for edu in profile['education']:
                for key, value in edu.items():
                    if isinstance(value, str) and query in value.lower():
                        edu_matches.append(edu)
                        break
            if edu_matches:
                results['profile']['education'] = edu_matches
        
        # Search in work experience
        if 'work' in profile and profile['work']:
            work_matches = []
            for job in profile['work']:
                for key, value in job.items():
                    if isinstance(value, str) and query in value.lower():
                        work_matches.append(job)
                        break
            if work_matches:
                results['profile']['work'] = work_matches
        
        # Search in projects
        if 'projects' in profile:
            for project in profile['projects']:
                for key, value in project.items():
                    if isinstance(value, str) and query in value.lower():
                        results['projects'].append(project)
                        break
                    elif key == 'skills' and isinstance(value, list):
                        for skill in value:
                            if query in skill.lower():
                                results['projects'].append(project)
                                break
        
        # Search in skills
        if 'skills' in profile:
            for skill in profile['skills']:
                skill_name = skill['name'] if isinstance(skill, dict) else skill
                if query in str(skill_name).lower():
                    results['skills'].append(skill)
        
        return results