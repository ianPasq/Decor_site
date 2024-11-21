from flask import Flask, request, jsonify, session
from __init__ import create_app, api
from models import db, User
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
import re

app.config['SECRET_KEY'] = 'very-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:passwordsafe@localhost/auth'
 
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True


app = create_app('development')
api = Api(app)
CORS(app)
app.secret_key = 'your_secret_key'
bcrypt = Bcrypt(app)
        


@app.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["password"]
 
    user_exists = User.query.filter_by(email=email).first() is not None
 
    if user_exists:
        return jsonify({"error": "Email already exists"}), 409
     
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
 
    session["user_id"] = new_user.id
 
    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })
 
@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]
  
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

if __name__ == '__main__':
    app.run(debug=True)