#!/usr/bin/python3
"""start flask and set a route"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """main route return"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return in other route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns  in c"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns in python"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display the number"""
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a html file """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")