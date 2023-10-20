#!/usr/bin/python3
"""
starts a Flask web application
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """After each request, remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    display a HTML page with a list of all state objects
    in DBStorage
    """
    state_objs = []
    for s in storage.all(State).values():
        state_objs.append(s)
    return render_template("7-states_list.html", state_objs=state_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
