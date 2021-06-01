from flask import Flask, request
import random
from flask_sqlalchemy import SQLAlchemy

from service1 import LoginForm

app = Flask(__name__)

# animal generator route here
@app.route('/get_animal', methods=['GET', "POST"])# allow posts)
def get_animal():
        if request.data == "1992-04-23":
            return "Monkey"
        else:
            return "You are not a monkey"
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)