#!/usr/bin/python3
"""A script that starts a Flask"""

from flask import Flask

app = Flask(__name__)

"""Defines the route"""


@app.route("/", strict_slashes=False)
def hello_world():
    """return a given string"""
    return("hbnb")


if __name__ == '__main__':
    """Starts the flask development server"""
    app.run(host='0.0.0.0', port=5000)
