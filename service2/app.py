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
            return jsonify({"name" : "Monkey"})
        #elif
        #else at the end
        elif year == 1993 or year == 2005 or year == 2017:
            return jsonify({"name" : "Rooster"})

        elif year == 1994 or year == 2006 or year == 2018:
            return jsonify({"name" : "Dog"})

        elif year == 1995 or year == 2007 or year == 2019:
            return jsonify({"name" : "Pig"})

        elif year == 1996 or year == 2008 or year == 2020:
            return jsonify({"name" : "Rat"})

        elif year == 1997 or year == 2009 or year == 2021:
            return jsonify({"name" : "Ox"})
        
        elif year == 1998 or year == 2010 or year == 2022:
            return jsonify({"name" : "Tiger"})

        elif year == 1999 or year == 2011:
            return jsonify({"name" : "Rabbit"})

        elif year == 2000 or year == 2012:
            return jsonify({"name" : "Dragon"})

        elif year == 2001 or year == 2013:
            return jsonify({"name" : "Snake"})

        elif year == 2002 or year == 2014:
            return jsonify({"name" : "Horse"})

        elif year == 2003 or year == 2015:
            return jsonify({"name" : "Sheep"})
        
        else:
            return jsonify({"name" : "You don't seem to match up, you must be an alien"})
        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)