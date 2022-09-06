#!/usr/bin/python3
""" script that starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def route():
        """ display Hello HBNB! """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def route1():
        """ display HBNB """
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def route2(text):
        """ display C, followed by the value of the text variable """
        return "C " + text.replace('_', ' ')

    @app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def route3(text):
        """ display Python, followed by the value of the text variable """
        return "Python " + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def route4(n):
        """ display n is a numbe only if n is an integer """
        return str(n) + " is a number"

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def route5(n):
        """ display a HTML page only if n is an integer """
        return render_template('5-number.htmt', n=n)

    app.run(host='0.0.0.0')
