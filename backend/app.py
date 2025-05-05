from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bsyke'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'lax'
    SESSION_COOKIE_SECURE = False
   



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app, 
        origins=["http://localhost:5174"], 
        supports_credentials=True,
        methods=["GET", "POST", "PUT", "DELETE"]
    )
    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from cart import cart_bp
    from auth import auth_bp
    app.register_blueprint(cart_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/')

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=6000, debug=True)