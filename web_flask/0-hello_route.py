#!/usr/bin/python3
"""This module starts a flask application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This function prints a statement"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
