from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL") or 'sqlite:///development.db'
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("STAGING_DATABASE_URL")
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
        
    app.config['SECRET_KEY'] = 'bsyke'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    return app

app = create_app('development')
CORS(app)


class Main():
    @app.route('/home', methods=['GET'])
    def home():
        return "helloWORDL"
    
    @app.route('/about', methods=['POST', 'GET'])
    def about():
        return "hello"

    @app.route('/contact', methods=['GET'])
    def contact():
        return "heloworlding"

    @app.route('/categories', methods=['POST', 'GET'])
    def categories():
        return "helo"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
    