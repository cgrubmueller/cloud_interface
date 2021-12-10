from flask import Flask, request
import sqlite3 as sql
import re

# Regex-Pattern für E-Mail
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

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

        # checking if the email is valid
        if re.fullmatch(email_regex, email):
            # connecting to the database
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("SELECT bname, email, passwd FROM benutzer WHERE email = ? AND passwd = ?", (email, hash(passwd)))
                users = cur.fetchall()
                if (len(users) == 1):
                    msg = "\nWelcome!"
                elif (len(users) > 1):
                    msg = "\nInternal error: multiple users with the same email???"
                else:
                    msg = "\nUsername or password was not correct!"
        else:
            msg= f"\nThe email {email} is invalid. Try again with a valid email."

    except:
        con.rollback()
        msg = "\nAn error occured while logging you in!"
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

        #checking if the email is valid
        if re.fullmatch(email_regex, email):
            #connecting to the databse
            with sql.connect("database.db") as con:
                con.execute("CREATE TABLE IF NOT EXISTS benutzer (email TEXT PRIMARY KEY, bname TEXT, passwd TEXT)")

                con.execute("INSERT INTO benutzer (bname,email,passwd) VALUES (?,?,?)", (bname, email,hash(passwd)))

                con.commit()
                msg = f"\nUser {bname} successfully added to database."
        else:
            msg= f"\nThe email {email} is invalid. Try again with a valid email."

    except:
        con.rollback()
        msg = "\nAn user with this email is already registered!"
    finally:
        return msg
        con.close()

@app.route("/reset", methods=["POST"])
def reset():
    try:
        with sql.connect("database.db") as con:
            con.execute("DROP TABLE benutzer")
        msg = "Database was successfully reset!"
    except:
        con.rollback()
        msg = "\nError while resetting the Database!"
    finally:
        return msg
        con.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)
