#!/usr/bin/python3
"""
run a simple flask web app
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbtn():
    """
    print hello hbtn
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    print hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    print text
    """
    x = text.replace('_', ' ')
    return "C " + x


@app.route("/python", strict_slashes=False)
def py():
    """
    print text
    """
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def pytxt(text="is cool"):
    """
    print text
    """
    x = text.replace('_', ' ')
    return "Python " + x


@app.route("/number/<int:n>", strict_slashes=False)
def isnum(n):
    """
    is num
    """
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def numtmp(n):
    """
    is num
    """
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddOrEven(n):
    """
    is odd or even
    """
    t = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', num=n, typ=t)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
