from flask import Flask
from flask import render_template
from datetime import datetime
import re
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():
    #catfactsURl = "https://cat-fact.herokuapp.com/facts/"
    #webUrl = urllib.request.urlopen(catfactsURl)
    #if(webUrl.getcode() == 200):
        #data = json.loads(webUrl.read())
        #return render_template("index.html", data=data['all'])
    #else:
        #print("Received error, cannot parse results")
    
    return render_template("index.html")

@app.route("/results/")
def results():
    catfactsURl = "https://cat-fact.herokuapp.com/facts/"
    webUrl = urllib.request.urlopen(catfactsURl)
    if(webUrl.getcode() == 200):
        data = json.loads(webUrl.read())
        return render_template("results.html", data=data['all'])
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