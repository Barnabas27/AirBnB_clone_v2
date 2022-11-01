#!/usr/bin/python3
"""start flask and set a route"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    """states by id"""
    state = None
    states = storage.all(State)
    if id:
        _id = "State." + id
        if _id in states.keys():
            state = states[_id]
    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")