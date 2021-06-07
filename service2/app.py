from flask import Flask, request, jsonify
import random


app = Flask(__name__)

# animal generator route here
@app.route('/get_animal', methods=['GET', "POST"])# allow posts)
def get_animal():
        year = request.json["year"]
        month = request.json["month"]
        day = request.json["day"]

        if year == 1992 or year == 2004 or year == 2016:
            return jsonify({"name" : "Happy Pigeon"})
        #elif
        #else at the end
        elif year == 1993 or year == 2005 or year == 2017:
            return jsonify({"name" : "Sad Pigeon"})

        elif year == 1994 or year == 2006 or year == 2018:
            return jsonify({"name" : "Angry Pigeon"})

        elif year == 1995 or year == 2007 or year == 2019:
            return jsonify({"name" : "Excited Pigeon"})

        elif year == 1996 or year == 2008 or year == 2020:
            return jsonify({"name" : "Depressed Pigeon"})

        elif year == 1997 or year == 2009 or year == 2021:
            return jsonify({"name" : "Anxious Pigeon"})
        
        elif year == 1998 or year == 2010 or year == 2022:
            return jsonify({"name" : "Fierce Pigeon"})

        elif year == 1999 or year == 2011:
            return jsonify({"name" : "Grumpy Pigeon"})

        elif year == 2000 or year == 2012:
            return jsonify({"name" : "Sleepy Pigeon"})

        elif year == 2001 or year == 2013:
            return jsonify({"name" : "Beautiful Pigeon"})

        elif year == 2002 or year == 2014:
            return jsonify({"name" : "Evil Pigeon"})

        elif year == 2003 or year == 2015:
            return jsonify({"name" : "Hero Pigeon"})
        
        else:
            return jsonify({"name" : "You don't seem to match up, you must be an alien"})
        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)