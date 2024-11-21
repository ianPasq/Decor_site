from flask import Flask, render_template, jsonify
from . import create_app, db
from flask_cors import CORS


app = create_app('development')
CORS(app)
 
class Main():
    @app.route('/home', methods=['GET'])
    def home():
        return "hello"
    
    @app.route('/about', methods=['POST'])
    def about():
        return "hello"

    @app.route('/contact', methods=['POST'])
    def contact():
        return "helo"

    @app.route('/categories', methods=['POST'])
    def categories():
        return "helo"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
    