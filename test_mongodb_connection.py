import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

def test_mongodb_connection():
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/me_api')
    
    print("=" * 60)
    print("MongoDB Connection Test")
    print("=" * 60)
    print(f"Testing connection to: {mongo_uri}")
    print("-" * 60)
    
    # Check if password placeholder exists
    if '<password>' in mongo_uri or '<db_password>' in mongo_uri:
        print("❌ ERROR: You need to replace <password> with your actual password!")
        print("   Update your .env file with the real password")
        return False
    
    try:
        # Try to connect to MongoDB
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
        
        # Test the connection
        client.admin.command('ping')
        print("✅ SUCCESS: Connected to MongoDB!")
        
        # List databases
        dbs = client.list_database_names()
        print(f"📊 Available databases: {dbs}")
        
        return True
        
    except pymongo.errors.ServerSelectionTimeoutError:
        print("❌ FAILED: Could not connect to MongoDB.")
        print("   Possible reasons:")
        print("   - Internet connection issues")
        print("   - Wrong password in connection string")
        print("   - IP address not whitelisted in MongoDB Atlas")
        return False
        
    except pymongo.errors.ConfigurationError:
        print("❌ FAILED: Invalid MongoDB connection string format.")
        return False
        
    except pymongo.errors.OperationFailure as e:
        error_msg = str(e)
        print(f"❌ FAILED: Authentication error: {error_msg}")
        
        if "Authentication failed" in error_msg:
            print("   - Wrong username or password")
        elif "not authorized" in error_msg:
            print("   - User doesn't have permissions")
        return False
        
    except Exception as e:
        print(f"❌ FAILED: Unexpected error: {e}")
        return False

if __name__ == '__main__':
    success = test_mongodb_connection()
    print("-" * 60)
    if success:
        print("🎉 MongoDB connection test PASSED!")
    else:
        print("💥 MongoDB connection test FAILED!")
        print("\n🔧 Fix steps for MongoDB Atlas:")
        print("1. ✅ Replace <password> with your actual password in .env file")
        print("2. ✅ Whitelist your IP address in MongoDB Atlas")
        print("3. ✅ Check your username/password is correct")
        print("4. ✅ Make sure your cluster is running in MongoDB Atlas")
    print("=" * 60)