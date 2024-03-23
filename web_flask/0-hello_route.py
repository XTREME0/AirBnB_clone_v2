#!/usr/bin/python3
""" run a simple flask web app """

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)  
def hello_hbtn():
    return "Hello HBTN!"

app.run(host='0.0.0.0', port=5000)
