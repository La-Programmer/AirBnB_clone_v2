#!/usr/bin/python3
"""This module starts a flask application"""


from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Prints a statement"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Prints a statement"""
    if (n % 2 == 0):
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
