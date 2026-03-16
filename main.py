from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ApiRegistacija", method=["POST", "GET"])
def apiprijava():

    if request.method="POST":
        

    return render_template("apiRegi9stracija.html")    

app.run(debug=True)