#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)

"""Defines the route"""


@app.route("/", strict_slashes=False)
def hello():
    """return a given string"""
    return render_temlate("10-hbnb_filters.html")


if __name__ == '__main__':
    """Starts the flask development server"""
    app.run(host='0.0.0.0', port=5000)
