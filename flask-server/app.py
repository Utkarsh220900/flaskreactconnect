from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)


movie = [{"movie_name": 'A'}, {"movie_name": 'B'}, {"movie_name": 'C'}]


@app.route('/')
def hellowWorld():
    return "Hello World"


@app.route("/movies", methods=['GET'])
def movies():
    return jsonify({'movies': movie})
