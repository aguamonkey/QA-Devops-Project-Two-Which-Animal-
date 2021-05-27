from flask import Flask, request
import random

app = Flask(__name__)

# animal generator route here
@app.route('/get_fortune', methods=['GET'])
def get_animal():

    # There will be a bunch of if statements here:
    #if date this year and between this date and this date
    # return this animal
    # if this animal:
        #if luck_number => 75:
        # if luck number between 45-75
        #if luck number < 45
    return random.choice(['cow', 'pig', 'horse'])
    
# animal noise generator route here
@app.route('/get_noise', methods=['POST'])
def get_noise():
    noises = {
        "cow" : "moo",
        "pig" : "oink",
        "horse" : "neigh"
    }
    return noises[request.data.decode('utf-8')]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)