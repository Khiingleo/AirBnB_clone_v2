#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_context
def tear_down(self):
    """remove current session after each request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """displays a html page"""
    state_objs = []
    for s in storage.all(State).values():
        state_objs.append(s)
    return render_template("8-cities_by_states.html", state_objs=state_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
