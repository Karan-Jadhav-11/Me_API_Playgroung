from setuptools import setup, find_packages

setup(
    name="me-api-playground",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.3.3",
        "Flask-PyMongo==2.3.0",
        "Flask-CORS==4.0.0",
        "python-dotenv==1.0.0",
        "pytest==7.4.0"
    ],
)