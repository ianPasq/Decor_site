from flask import Flask
from __init__ import create_app
import os

app = create_app(os.getenv("CONFIG_MODE", "development"))
 
@app.route('/')
def yo():
    return "helo" 
 
 

if __name__ == "__main__":
    app.run()