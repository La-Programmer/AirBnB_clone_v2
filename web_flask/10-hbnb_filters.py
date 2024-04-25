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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Renders hbnb homepage"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(debug='true', host='0.0.0.0')
