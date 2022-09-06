#!/usr/bin/python3
""" script that starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask
    from flask import render_template

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """ display Hello HBNB """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb_route():
        """ display HBNB """
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def c_route(text):
        """ display C, followed by the value of the text varuable """
        return "C " + text.replace('_', ' ')

    @app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
    @app.route('/python/(<text>', strict_slashes=False)
    def python_route(text):
        """ display Python, followed by the value of the text varuable """
        return "Python " + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def n_route(n):
        """ display n is a number only is n is an integer """
        return str(n) + " is a number"

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_templates(n):
        """ display a HTML page only if n is an integer """
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<n>', strict_slashes=False)
    def odd_or_even(n):
        """ display a HTML page only if n is an integer """
        if n % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"
        return render_template('5-number.html', n=n, even_odd=even_odd)

    app.run(host='0.0.0.0')
