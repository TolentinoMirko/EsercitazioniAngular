from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

# Stringa di connessione al DB
app.config["MONGO_URI"] = "mongodb+srv://tolentinomirko:EQkZAx6z4OEE8jyO@cluster0.igeu7sc.mongodb.net/Relab" #Importante qui va specificato il nome del DB

mongo = PyMongo(app)
# Per rispondere alle chiamate cross origin
CORS(app)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"

# Questa route effettua una find() su tutto il DB (si limita ai primi 100 risultati)
@app.route('/addresses', methods=['GET'])
def get_all_addresses():
    mil4326WKT = mongo.db.MilWKT4326
    output = []
    for s in mil4326WKT.find().limit(100):
        output.append(s['INDIRIZZO'])
        
    return jsonify({'result': output})


@app.route('/ci_vettore/<foglio>', methods=['GET'])
def get_vettore(foglio):
    foglio = int(foglio)
    mil4326WKT = mongo.db.MilWKT4326
    output = []
    query = {"FOGLIO" : foglio}
    for s in mil4326WKT.find(query).limit(100):
        output.append({
            "INDIRIZZO":s['INDIRIZZO'],
            "WGS84_X":s["WGS84_X"],
            "WGS84_Y":s["WGS84_Y"],
            "CLASSE_ENE":s["CLASSE_ENE"],
            "EP_H_ND":s["EP_H_ND"],
            "FOGLIO":s["FOGLIO"],
            "CI_VETTORE":s['CI_VETTORE'],
            "SEZ":s['SEZ']})
    return jsonify({'result': output})



if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()