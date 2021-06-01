from flask import Flask, request
import random

app = Flask(__name__)

# animal generator route here
@app.route('/get_number', methods=['GET'])
def get_number():

    # There will be a bunch of if statements here:
    #if date this year and between this date and this date
    # return this animal
    #This will be a random number generator
    number = str(random.randint(1,100))
    return number
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)