from flask import Flask, make_response, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return make_response(jsonify({"message": 'Hello World!'}),200)



if __name__ == '__main__':
    app.run()