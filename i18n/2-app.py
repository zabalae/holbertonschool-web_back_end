#!/usr/bin/env python3
"""Simple flask app setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class to set defualt locale and timezone"""
    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello():
    """Return a simple homepage"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Function to determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
