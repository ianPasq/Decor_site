from flask import Flask
from __init__ import create_app, app
from flask_restful import Api
from flask_cors import CORS, cross_origin
from __init__ import db
import os

app = create_app(os.getenv("CONFIG_MODE", "development"))
api = Api(app)
CORS(app)
 
class Main():
    @app.route('/home')
    def home():
        return "helo" 
    
    @app.route('/about')
    def about():
        return "helo"

    @app.route('/contact')
    def contact():
        return "helo"

    @app.route('/categories')
    def categories():
        return "helo"
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)