#!/usr/bin/python3
"""start flask and set a route"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns states and id"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")