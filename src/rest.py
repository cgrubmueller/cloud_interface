from flask import Flask, g, jsonify, request
# import requests
import time
import json
import urllib3
import sqlite3

allData = ""
DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

global app
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET"])
def loginGET():
    return

@app.route("/signup", methods=["POST"])
def signupPOST():
    return

@app.route("/signup", methods=["GET"])
def signupGET():
    return


if __name__ == "__main__":
    app.run(debug=True, port=8001)
