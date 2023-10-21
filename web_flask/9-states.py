#!/usr/bin/python3
"""
starts a flask web application
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """remove running sqlalchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """displays a html page with a list of all states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """displays a html page with info about <id>"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=states)
    return render_template("9-states.html")
