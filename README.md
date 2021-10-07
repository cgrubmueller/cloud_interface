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
python -m venv
```

Aktivieren mit **Linux**:

```
source myvenv/bin/activate
```

Aktivieren mit **Windows**:

```
env\Scripts\activate.bat
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
curl -X POST -F 'bname=linuxize' -F 'email=linuxize@example.com' -F 'passwd=12345' http://127.0.0.1:8001/register
```

### Einloggen

```
curl -X POST -F 'bname=linuxize' -F 'email=linuxize@example.com' -F 'passwd=12345' http://127.0.0.1:8001/login
```



## Implementierung

### Webserver starten

Mit folgendem Code wird das Programm und der Flask Server gestartet.

```python
if __name__ == "__main__":
    app.run(debug=True, port=8001)
```

