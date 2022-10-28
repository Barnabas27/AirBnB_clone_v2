#!/usr/bin/python3
"""start flask and set a route"""

from flask import Flask, render_template
from models import storage
from models.state import State
import os

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")