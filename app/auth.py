from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
import bcrypt

auth_bp = Blueprint('auth', __name__)
auth = HTTPBasicAuth()

users = {
    "admin": bcrypt.hashpw("secret".encode('utf-8'), bcrypt.gensalt())
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return bcrypt.checkpw(password.encode('utf-8'), users[username])
    return False
