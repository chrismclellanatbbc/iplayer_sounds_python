from flask import Flask
from flask import render_template
from datetime import datetime
import re
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():
    companyNumber = '08528493'
    companyNumberSearchUrl = "https://api.opencorporates.com/companies/gb/" + str(companyNumber)
    webUrl = urllib.request.urlopen(companyNumberSearchUrl)
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        json_data = json.loads(data)

        #return data
        return render_template("index.html", data=json_data)
    else:
        print("Received error, cannot parse results")
    #return render_template("index.html")

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