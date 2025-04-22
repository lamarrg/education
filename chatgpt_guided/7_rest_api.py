"""
 Create a small Flask API with two endpoints: /ping (returns pong) and /reverse (takes a string and returns it reversed).
"""

import flask

from flask import Flask

app = Flask(__name__)

@app.route("/ping")
def hello_world():
    return "<p>Pong</p>"


@app.route("/reverse/<string:the_word>")
def reverse(the_word):
    return f"Your original word is... {the_word}<br><br>Your reversed word is... {the_word[::-1]}"


if __name__ == '__main__':  
   app.run(debug=True)