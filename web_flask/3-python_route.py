#!/usr/bin/env python3

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text=None):
    new_text = text.replace('_', ' ')
    return "C {}".format(escape(new_text))


@app.route('/python/<text>', strict_slashes=False)
def print_py(text):
    new_text = text.replace('_', ' ')
    return "Python {}".format(escape(new_text))


@app.route('/python/', strict_slashes=False)
def print_py_default(text="is cool"):
    new_text = text.replace('_', ' ')
    return "Python {}".format(escape(new_text))

if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
