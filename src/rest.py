from flask import Flask, g, jsonify, request, render_template
# import requests
import time
import json
import urllib3
import sqlite3 as sql

app = Flask(__name__)


allData = ""

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('database.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET"])
def loginGET():
    return '''
        <form action="/loginPost">
          <label for="bname">Benutzername:</label>
          <input type="text" id="bname" name="bname"><br><br>
          <label for="email">E-Mail:</label>
          <input type="email" id="email" name="email"><br><br>
          <label for="passwd">Passwort:</label>
          <input type="password" id="passwd" name="passwd"><br><br>
          <input type="submit" value="Submit">
        </form>
    '''

@app.route("/loginPost", methods=["POST"])
def loginPost():
    try:
        bname = request.form['bname']
        email = request.form['email']
        passwd = request.form['passwd']

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute('CREATE TABLE IF NOT EXISTS user (email TEXT PRIMARY KEY, name TEXT, passwd TEXT)')

            cur.execute('''INSERT INTO benutzer (bname,email,passwd)
            VALUES (?,?,?),(bname,email,passwd)''')

            con.commit()
            msg = "Record successfully added"

    except:
        con.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        con.close()

@app.route("/signup", methods=["POST"])
def signupPOST():
    return

@app.route("/signup", methods=["GET"])
def signupGET():
    return


if __name__ == "__main__":
    app.run(debug=True, port=8001)
