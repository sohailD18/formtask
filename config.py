import os

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",  # Change if necessary
    "database": "form_db"
}

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
SECRET_KEY = "your_secret_key"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
