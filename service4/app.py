from flask import Flask, request
import random

app = Flask(__name__)

# animal generator route here
@app.route('/get_fortune', methods=['GET', "POST"])
def get_fortune():

        animal = request.json["name"]
        number = request.json["luck_number"]


        if animal == "Happy Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Happy Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Happy Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Sad Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Sad Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Sad Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Angry Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Angry Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Angry Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Excited Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Excited Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Excited Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Depressed Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Depressed Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Depressed Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Anxious Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Anxious Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Anxious Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Fierce Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Fierce Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Fierce Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Grumpy Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Grumpy Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Grumpy Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Sleepy Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Sleepy Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Sleepy Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Beautiful Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Beautiful Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Beautiful Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Evil Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Evil Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Evil Pigeon" and number < 3:
            return "You will go hungry"
        elif animal == "Hero Pigeon" and number >= 7:
            return "You will get all the seeds you desire this year"
        elif animal == "Hero Pigeon" and number < 7 and number >= 3:
            return "You will have to be moderate in your seed consumption"
        elif animal == "Hero Pigeon" and number < 3:
            return "You will go hungry"
        else:
            return "No fortune detected, you must live in another timezone"
        


   #     if destiny[0] == "Monkey":
   #         return jsonify({"name" : "Monkey"})
   #     else:
   #         return "You are not a monkey"
  

        
    
# animal noise generator route here


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)