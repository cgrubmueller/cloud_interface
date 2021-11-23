# README

Christian Grubmüller

07.10.2021

## Ausführen

Zuerst muss man das Repository klonen. Das macht man mit folgendem Befehl.

```
git clone https://github.com/TGM-HIT/syt5-gk961-cloud-datenmanagement-cgrubmueller.git
```

Anschließend muss man eine *venv* erstellen und aktivieren.

```
python -m venv venv
```

Aktivieren mit **Linux**:

```
source venv/bin/activate
```

Aktivieren mit **Windows**:

```
venv\Scripts\activate.bat
```

Dann muss man das requirements.txt installieren.

```
pip install -r requirements.txt
```

Anschließend kann man mit folgendem Befehl das Programm ausführen.

```
python ./src/rest.py
```

Nachdem dann der Server läuft kann man mit den nachfolgenden Befehlen einen Benutzer registrieren bzw einloggen.

### Registrieren

```
curl -X POST -F 'bname=username' -F 'email=email@example.com' -F 'passwd=123456' http://127.0.0.1:8001/register
```

### Einloggen

```
curl -X POST -F 'bname=username' -F 'email=email@example.com' -F 'passwd=123456' http://127.0.0.1:8001/login
```



## Implementierung [3]

Die Aufgabe habe ich mit Flask und mit SQLite umgesetzt. SQLite habe ich verwendet, weil MongoDB für diese Aufgabe zu aufwändig wäre.

#### Flask

*Flask is a lightweight [WSGI](https://wsgi.readthedocs.io/) web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around [Werkzeug](https://werkzeug.palletsprojects.com/) and [Jinja](https://jinja.palletsprojects.com/) and has become one of the most popular Python web application frameworks.*

*Flask offers suggestions, but doesn’t enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.* [1]

#### SQLite

*SQLite is a C-language library that implements a [small](https://sqlite.org/footprint.html), [fast](https://sqlite.org/fasterthanfs.html), [self-contained](https://sqlite.org/selfcontained.html),  [high-reliability](https://sqlite.org/hirely.html), [full-featured](https://sqlite.org/fullsql.html), SQL database engine. SQLite is the [most used](https://sqlite.org/mostdeployed.html) database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.* [2]

### Webserver starten

Mit folgendem Code wird das Programm und der Flask Server gestartet.

```python
if __name__ == "__main__":
    app.run(debug=True, port=8001)
```

Folgender Code ist ein Beispiel für das einloggen.

`@app.route("/login", methods=["POST"])` definiert, dass man mit `/login` darauf zugreift/diese Methode ausführt und dabei die Methode Post verwendet.

Mit `request.form['bname']` kann man auf die übergebenen Parameter zugreifen.

Mit `with sql.connect("database.db") as con:` verbindet man sich zu der Datenbank und `cur = con.cursor()` definiert einen Cursor.

Mit `cur.execute()` kann man mit SQL in der Datenbank ausführen.

```python
@app.route("/login", methods=["POST"])
def loginPost():
    try:
        bname = request.form['bname']
        email = request.form['email']
        passwd = request.form['passwd']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT bname, email, passwd FROM benutzer WHERE email = ? AND passwd = ?", (email, hash(passwd)))
            users = cur.fetchall()
            if (len(users) == 1):
                msg = "Willkommen!"
            elif (len(users) > 1):
                msg = "Fehler"
            else:
                msg = "Benutzername oder Passwort ist nicht korrekt"
```

## Deployment mit Docker

Image builden:
```bash
docker build --tag rest .
```
Image runnen:
```bash
docker run --name rest -p 8001:8001 rest
```

## Docker ohne sudo
```bash
# Docker-Gruppe erstellen falls sie nicht vorhanden ist.
sudo groupadd docker
# Momentanen User zu der Docker-Gruppe hinzufügen
sudo gpasswd -a $USER docker
```

## Quellen

[1] https://pypi.org/project/Flask/ (07.10.2021)

[2] https://sqlite.org/index.html (07.10.2021)

[3] https://python.land/virtual-environments/virtualenv (07.10.2021)