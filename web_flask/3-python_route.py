#!/usr/bin/python3
"""
starts a flask web application
"""
from flask import Flask

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


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """displays Python followed by <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
