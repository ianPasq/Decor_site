from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bsyke'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from cart import cart_bp
    app.register_blueprint(cart_bp)

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=4000, debug=True)