from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)

# Sample list of users (replace with your user management logic)
users = [{"username": "user1", "password_hash": "$2b$12$yourhashedpassword"}]

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = next((u for u in users if u["username"] == username), None)
    if user is None or not check_password_hash(user["password_hash"], password):
        abort(401, description="Authentication failed")

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})

@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)

# Implement user registration, logout, and other authentication endpoints as needed
