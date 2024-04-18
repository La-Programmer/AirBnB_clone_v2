#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB!"


@app.route("/c/<text>")
def print_c(text):
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route("/python/<text>")
def print_c(text):
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
