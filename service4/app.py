from flask import Flask, request
import random

app = Flask(__name__)

# animal generator route here
@app.route('/get_fortune', methods=['GET', "POST"])
def get_fortune():

        animal = request.json["name"]
        number = request.json["luck_number"]


        if animal == "Monkey" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Monkey" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Monkey" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Rooster" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Rooster" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Rooster" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Dog" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Dog" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Dog" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Pig" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Pig" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Pig" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Rat" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Rat" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Rat" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Ox" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Ox" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Ox" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Tiger" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Tiger" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Tiger" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Rabbit" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Rabbit" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Rabbit" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Dragon" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Dragon" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Dragon" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Snake" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Snake" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Snake" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Horse" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Horse" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Horse" and number < 45:
            return "This will be a hard year but will make you stronger"
        elif animal == "Sheep" and number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal == "Sheep" and number < 75 and number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal == "Sheep" and number < 45:
            return "This will be a hard year but will make you stronger"
        else:
            return "No fortune detected, you must live in another timezone"
        


   #     if destiny[0] == "Monkey":
   #         return jsonify({"name" : "Monkey"})
   #     else:
   #         return "You are not a monkey"
  

        
    
# animal noise generator route here


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)