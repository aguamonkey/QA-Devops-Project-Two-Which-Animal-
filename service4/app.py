from flask import Flask, request
import random

app = Flask(__name__)

# animal generator route here
@app.route('/get_fortune', methods=['GET', "POST"])
def get_fortune():

        animal = request.json["name"]
        number = request.json["luck_number"]


        if animal = "Monkey" and luck_number > 75:
            return "This is going to be a great year in which all of your dreams come true"
        elif animal = "Monkey" and luck_number < 75 or luck_number > 45:
            return "This is going to be a year of ups and downs but in the end it will be a good one"
        elif animal = "Monkey" and luck_number < 45:
            return "THis will be a hard year but will make you stronger"
        


   #     if destiny[0] == "Monkey":
   #         return jsonify({"name" : "Monkey"})
   #     else:
   #         return "You are not a monkey"
  

    return "This is going to be a great year in which all of your dreams come true"

        
    
# animal noise generator route here


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)