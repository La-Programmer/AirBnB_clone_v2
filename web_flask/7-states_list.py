#!/usr/bin/python3
"""This module starts a web application"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def reload_session(exception):
    """Reload the DB session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders a list of states"""
    states = storage.all('State')
    # print(states)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
