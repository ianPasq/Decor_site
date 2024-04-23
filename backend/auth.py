from flask import Flask, request, jsonify, session
from __init__ import app 
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'
bcrypt = Bcrypt(app)
api = Api(app)

class AuthRoutes():
    @app.route('/login', methods=['POST'])
    @cross_origin
    def login():
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if username == 'user' and password == 'password':
            session['username'] = username  
            return jsonify(message='Login successful'), 200
        else:
            return jsonify(message='Login failed'), 401
    @app.route('/logout', methods=['POST'])
    def logout():
        session.pop('username', None) 
        return jsonify(message='Logged out'), 200
    @app.route('/protected', methods=['GET'])
    def protected():
        if 'username' in session:
            return jsonify(message='Protected data'), 200
        else:
            return jsonify(message='Unauthorized access'), 401
        
    
users = {
    'user': {
        'password_hash': bcrypt.generate_password_hash('password').decode('utf-8'),
        'id': 1
    }
}

class AuthResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username in users and bcrypt.check_password_hash(users[username]['password_hash'], password):
            session['user_id'] = users[username]['id']
            return jsonify(message='Login successful'), 200
        else:
            return jsonify(message='Login failed'), 401

    def delete(self):
        if 'user_id' in session:
            session.pop('user_id', None)
            return jsonify(message='Logged out'), 200
        else:
            return jsonify(message='No active session'), 401

    def get(self):
        if 'user_id' in session:
            return jsonify(message='Protected data'), 200
        else:
            return jsonify(message='Unauthorized access'), 401

api.add_resource(AuthResource, '/auth')


users = {
    'user': {
        'password_hash': bcrypt.generate_password_hash('password').decode('utf-8'),
        'id': 1
    }
}

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username in users:
            return jsonify(message='Username already exists'), 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users[username] = {'password_hash': hashed_password}

        return jsonify(message='User registered'), 201

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username not in users:
            return jsonify(message='User not found'), 404

        hashed_password = users[username]['password_hash']

        if bcrypt.check_password_hash(hashed_password, password):
            return jsonify(message='Login successful'), 200
        else:
            return jsonify(message='Login failed'), 401

api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True)