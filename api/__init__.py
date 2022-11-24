from flask import Flask, make_response, jsonify
from flask.cli import FlaskGroup


app = Flask(__name__)
@app.route('/')
def index():
    return make_response(jsonify({"message": 'Hello World!'}),200)


