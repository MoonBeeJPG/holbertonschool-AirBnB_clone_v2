#!/usr/bin/python3
""" script that starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def route():
        """ Root folder route """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def route1():
        """ /hbnb folder route """
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def route2(text):
        """ /c/<text> folder route """
        return "C " + text.replace('_', ' ')

    @app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def route3(text):
        """ /python/(<text>) folder route """
        return "Python " + text.replace('_', ' ')

    app.run(host='0.0.0.0')
