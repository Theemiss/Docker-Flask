from flask.cli import FlaskGroup

from flask import Flask, make_response, jsonify
from flask.cli import FlaskGroup


app = Flask(__name__)
@app.route('/')
def index():
    return make_response(jsonify({"message": 'Hello World!'}),200)





cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()