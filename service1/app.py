from flask import Flask, render_template, request
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
import requests
import os

from os import getenv
from sqlalchemy import desc
from wtforms.fields.html5 import DateField
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
SECRET_KEY = os.urandom(32)

app.config["SECRET_KEY"] = SECRET_KEY

db = SQLAlchemy(app)

class LoginForm(Form):
    birthdate = DateField('birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('What is my destiny?')

#type now equals name
class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    luck_rating = db.Column(db.Integer)
    fortune = db.Column(db.String(200), nullable=False)   

@app.route('/', methods=['GET', "POST"])
#@app.route('/home')
def home():
    form = LoginForm()

    if request.method == "POST":

        if form.validate_on_submit():
            year = form.birthdate.data.year
            month = form.birthdate.data.month
            day = form.birthdate.data.day

            
            name = requests.post('http://which_animal_am_i_name_api:5000/get_animal', json={"year": year, "month": month, "day":day})
            
            luck_number = requests.get('http://which_animal_am_i_luck_api:5000/get_number') 
            #raise ValueError(luck_number.text)

            result = {**name.json(), **luck_number.json()}
            
            fortune = requests.post('http://which_animal_am_i_fortune_api:5000/get_fortune', json=result)
            #db.session.add(animal.text)
            db.session.commit()
            #return redirect(url_for("fortune"))
        return render_template('fortune.html', name=name.json()["name"], luck_number=luck_number.json()["luck_number"], fortune=fortune.text)
 
    else:
            
        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)