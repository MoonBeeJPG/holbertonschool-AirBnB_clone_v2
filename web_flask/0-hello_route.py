#!/usr/bin/python3
""" script that starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def route():
        """ Root foulder route """
        return "Hello HBNB!"

    app.run(host='0.0.0.0')
