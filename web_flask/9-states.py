#!/usr/bin/python3
"""This module starts a web application"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def reload_session(exception):
    """Reload the DB session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Renders a list of all states"""
    states = storage.all('State')
    # print(states)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Renders the state with given id"""
    states = storage.all('State')
    found = False
    state = None
    for key, value in states.items():
        if (value.id == id):
            state = value
            found = True
    return render_template('9-states.html', states=states, id=id, found=found, state=state)


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
