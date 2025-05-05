from flask import Blueprint, request, jsonify, session, current_app
from models import User
from app import db, bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=["POST"])
def signup():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not all([name, email, password]):
            return jsonify({"error": "Missing required fields"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 409

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session["user_id"] = new_user.id

        return jsonify({
            "id": new_user.id,
            "name": new_user.username,
            "email": new_user.email
        }), 201

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Signup error: {e}")
        return jsonify({"error": "Server error during signup"}), 500

@auth_bp.route('/login', methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        session["user_id"] = user.id
        return jsonify({
            "id": user.id,
            "name": user.username,
            "email": user.email
        }), 200

    except Exception as e:
        current_app.logger.error(f"Login error: {e}")
        return jsonify({"error": "Server error during login"}), 500

    
