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


@app.route('/cities_by_states', strict_slashes=False)
def state_id():
    """states and cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
    