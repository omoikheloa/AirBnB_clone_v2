#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """

    """
    return 'Hello HBNB!'


if __name___ == '__main__':
    app.run(host='0.0.0.0', port=5000)
