from flask import Flask, Blueprint, request, jsonify, session
from app import create_app, db
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

auth_bp = Blueprint('auth', __name__)
 
auth_bp.config['SECRET_KEY'] = 'bearsykerr'
auth_bp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
  
bcrypt = Bcrypt(auth_bp) 
CORS(auth_bp, supports_credentials=True)
db.init_app(auth_bp)
  
with auth_bp.app_context():
    db.create_all()

class auth():

    @auth_bp.route('/sign_up', methods=["POST", "GET"])
    def signup():
        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")


        user_exists = User.query.filter_by(email=email).first() is not None

        if user_exists:
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
        })

    @auth_bp.route('/login', methods=["POST"])
    def login_user():
        data = request.json
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({"error": "Unauthorized Access"}), 401

        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Unauthorized"}), 401

        session["user_id"] = user.id

        return jsonify({
            "id": user.id,
            "email": user.email
        })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
    with app.app_context():
        db.create_all()
        
    
