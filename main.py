from flask import Flask, render_template, jsonify, request
from tinydb import TinyDB
import requests

db = TinyDB("obiskovalci.json")
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ApiRegistacija", methods=["POST", "GET"])
def apiprijava():

    if request.method == "POST":
        email = request.form.get("mail")
        geslo = request.form.get("pass")
        ime = request.form.get("name")
        država = request.form.get("country").upper()

        response = requests.get(f"https://api.nationalize.io/?name={ime}").json()

        if response.status_code != 200:
            return ({"message": "Napaka pri Nationalize API."})

        
        countries = [c['country_id'].upper() for c in response.get('country', [])]

        if država in countries:
            db.insert({
                "email": email,
                "password": geslo,
                "name": ime,
                "country": država
            })

        return ({"drzava": država})

    else:
        return render_template("apiRegistacija.html")

app.run(debug=True)