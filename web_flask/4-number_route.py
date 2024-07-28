#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a greeting string."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a given string."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the value of the text variable."""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Display 'Python ' followed by the value of the text variable."""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route('/json', strict_slashes=False)
def json_example():
    """Return a JSON response."""
    data = {
        "message": "This is a JSON response",
        "status": "success"
    }
    return jsonify(data)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors with a custom message."""
    return "404 Not Found", 404


if __name__ == "__main__":
    # Set debug=True to enable debug mode for development purposes
    app.run(host="0.0.0.0", port=5000, debug=True)
