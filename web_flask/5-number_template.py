#!/usr/bin/python3
"""
starts a flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    displays C followed by the value of <text>
    Args:
        text(string): the text to display
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """displays Python, followed by the value of <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
