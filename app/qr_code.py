from flask import Blueprint, request, jsonify, send_from_directory, url_for
import qrcode
from PIL import Image, ImageOps
import uuid
import os
from .auth import auth
from .config import Config

qr_bp = Blueprint('qr_code', __name__)

valid_tokens = {}
used_tokens = set()

@qr_bp.route('/access')
@auth.login_required
def access():
    token = request.args.get('token')
    if not token:
        abort(400, description="Token is required")
    if token in valid_tokens and token not in used_tokens:
        used_tokens.add(token)
        filepath = valid_tokens[token]
        return send_from_directory(directory=os.path.dirname(filepath), filename=os.path.basename(filepath), as_attachment=True)
    else:
        abort(403)

@qr_bp.route('/generate/<path:filename>')
@auth.login_required
def generate(filename):
    # (The code continues with the generate function already detailed in the previous answers)
