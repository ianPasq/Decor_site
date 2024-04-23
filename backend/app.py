from flask import Flask, render_template
from __init__ import app, db
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__, static_url_path='', static_folder='frontend--')

@app.route('/')
def index():
    return render_template('index.html')

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