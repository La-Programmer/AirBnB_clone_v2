#!/usr/bin/python3
"""This module starts a flask application"""


from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Prints a statement"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints a statement"""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text=None):
    """Prints a statement"""
    new_text = text.replace('_', ' ')
    return "C {}".format(escape(new_text))


@app.route('/python/<text>', strict_slashes=False)
def print_py(text):
    """Prints a statement"""
    new_text = text.replace('_', ' ')
    return "Python {}".format(escape(new_text))


@app.route('/python/', strict_slashes=False)
def print_py_default(text="is cool"):
    """Prints a statement"""
    new_text = text.replace('_', ' ')
    return "Python {}".format(escape(new_text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Prints a statement"""
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
