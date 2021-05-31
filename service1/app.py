from flask import Flask, render_template
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc
from wtforms.fields.html5 import DateField


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class LoginForm(Form):
    birthdate = DateField('birthdate', format='%Y-%m-%d')

#type now equals name
class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    luck_rating = db.Integer(db.Integer)
    fortune = db.Column(db.String(200), nullable=False)   

@app.route('/')
def home():
    animal = requests.get('http://which_animal_am_i_name_api:5000/get_animal')
    luck_number = requests.post('http://which_animal_am_i_luck_api:5000/get_number', data=animal.text)
    fortune = requests.post('http://which_animal_am_i_fortune_api:5000/get_fortune', data=animal.text)


    last_five_animals = Animals.query.order_by(desc(Animals.id)).limit(5).all()
    db.session.add(
        Animals(
            name = animal.text,
            noise = noise.text
        )
    )
    db.session.commit()

    return render_template('index.html', animal=animal.text, noise=noise.text, last_five_animals=last_five_animals)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)