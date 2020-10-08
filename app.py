from flask import Flask
from flask import render_template
from datetime import datetime
import re
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/random/")
def randomPage():
    catfactsURl = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5"
    webUrl = urllib.request.urlopen(catfactsURl)
    if(webUrl.getcode() == 200):
        data = json.loads(webUrl.read())
        return render_template("random.html", data=data, title="Random")
    else:
        print("Received error, cannot parse results")

@app.route("/results/")
def results():
    catfactsURl = "https://cat-fact.herokuapp.com/facts/"
    webUrl = urllib.request.urlopen(catfactsURl)
    if(webUrl.getcode() == 200):
        data = json.loads(webUrl.read())
        return render_template("results.html", data=data['all'], title="Results")
    else:
        print("Received error, cannot parse results")


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello")
@app.route("/hello/<name>")
def hello_there(name = None):
    
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    """
    docstring
    """
    return app.send_static_file("data.json")