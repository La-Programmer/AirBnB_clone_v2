#!/usr/bin/python3
"""This module starts a flask application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Prints a statement"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints a statement"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
