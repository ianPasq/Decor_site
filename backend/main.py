from flask import Flask
from __init__ import create_app
import os

app = create_app(os.getenv("CONFIG_MODE", "development"))
 
 
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
    app.run()