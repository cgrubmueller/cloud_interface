from flask import Flask, g, jsonify, request, render_template
# import requests
import time
import json
import urllib3
import sqlite3 as sql
import hashlib

app = Flask(__name__)


allData = ""

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/loginPost", methods=["POST"])
def loginPost():
    try:
        bname = request.form['bname']
        email = request.form['email']
        passwd = request.form['passwd']

        print("blaskfa")
        print(bname)
        print(email)
        print(passwd)

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute('''INSERT INTO benutzer (bname,email,md5(passwd))
            VALUES (?,?,?)''',(bname,email,passwd))

            con.commit()
            msg = "Record successfully added"

    except:
        con.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        con.close()

@app.route("/register", methods=["POST"])
def signupPOST():
    try:
        bname = request.form['bname']
        email = request.form['email']
        passwd = request.form['passwd']

        with sql.connect("database.db") as con:
            # con.execute("drop table benutzer")
            con.execute('CREATE TABLE IF NOT EXISTS benutzer (email TEXT PRIMARY KEY, bname TEXT, passwd TEXT)')

            con.execute('''INSERT INTO benutzer (bname,email,passwd) VALUES (?,?,?)''', (bname, email,passwd))

            con.commit()
            msg = f"user {bname} successfully added to database"

    except:
        con.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        con.close()


if __name__ == "__main__":
    app.run(debug=True, port=8001)
