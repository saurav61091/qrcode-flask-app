from flask import Flask
from .auth import auth_bp
from .qr_code import qr_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp)
    app.register_blueprint(qr_bp)

    return app
