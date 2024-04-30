import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    UPLOAD_FOLDER = 'static/qrcodes'
    BASE_DIRECTORY = 'path/to/documents'
    LOGO_PATH = 'static/logo.png'
