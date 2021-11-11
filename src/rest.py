from flask import Flask, request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def loginPost():
    credentials = request.json
    try:
        bname = credentials['bname']
        email = credentials['email']
        passwd = credentials['passwd']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT bname, email, passwd FROM benutzer WHERE email = ? AND passwd = ?", (email, hash(passwd)))
            users = cur.fetchall()
            if (len(users) == 1):
                msg = "\nWillkommen!"
            elif (len(users) > 1):
                msg = "\nFehler"
            else:
                msg = "\nBenutzername oder Passwort ist nicht korrekt"

    except:
        con.rollback()
        msg = "\nerror beim einloggen"
    finally:
        return msg
        con.close()

@app.route("/register", methods=["POST"])
def signupPOST():
    credentials = request.json
    try:
        bname = credentials['bname']
        email = credentials['email']
        passwd = credentials['passwd']

        with sql.connect("database.db") as con:
            con.execute("drop table benutzer")
            con.execute("CREATE TABLE IF NOT EXISTS benutzer (email TEXT PRIMARY KEY, bname TEXT, passwd TEXT)")

            con.execute("INSERT INTO benutzer (bname,email,passwd) VALUES (?,?,?)", (bname, email,hash(passwd)))

            con.commit()
            msg = f"\nuser {bname} successfully added to database"

    except:
        con.rollback()
        msg = "\nerror in insert operation"
    finally:
        return msg
        con.close()


if __name__ == "__main__":
    app.run(debug=True, port=8001)
