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
    """After each request remove the current SQLAlchemy Session"""
    storage.close()

@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    displays a HTML page with a list of all state objects
    in DBStorage
    """
    state_objs = []
    for s in storage.all(State).values():
        state_objs.append(s)
    return render_template("7-states_list.html", state_objs=state_objs)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """displays an HTML page with info about <id>"""
    state_obj = None
    for state in storage.all(State).values():
        if state.id == id:
            state_obj = state
    return render_template("9-states.html", state_obj=state_obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
