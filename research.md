Research

Christian Grubmüller

07.10.2021

- Welche grundlegenden Elemente müssen bei einer REST Schnittstelle zur Verfügung gestellt werden? [^1]

  - einheitliche Schnittstelle: Die verwendeten Ressourcen sollen durch eine einzige URL eindeutig identifizierbar sein. Diese Ressourcen kann man dann mit den Methoden der Netzwerkprotokolle verändern. (Bei HTTP zum Beispiel DELETE, PUT, GET und POST)
  - Client: Der Client ist zuständig für die Benutzeroberfläche und das Sammeln von Anfragen.
  - Server: Der Server kümmert sich um die Datenzugriffe, das Workload-Management und die Sicherheit.
  - lose Kopplung: Durch die Schnittstelle sind Server und Client lose gekoppelt. Das ermöglicht das individuelle weiterentwickeln der beiden.
  - Zustandslose Operation: Eine Operation zwischen Server und Client sollte zustandslos sein. Das heißt der Client speichert seinen eigenen Zustand ab und der Server weiß nichts von diesem.
  - mehrschichtiges System: Durch REST wird eine Architektur ermöglicht, die aus mehreren Schichten besteht.

  Wenn man will, das Daten persistent abgespeichert werden, muss man eine Datenbank (SQLite, MongoDB, etc.) verwenden.

  

- Wie stehen diese mit den HTTP-Befehlen in Verbindung? [^2]

  Durch REST wird die Entwicklung einer Applikationen mit allen möglichen CURD (create, update, retrieve, delete) Funktionen unterstützt. Diese werden meistens mit den HTTP-Methoden umgesetzt.

  - **GET**: Die GET-Methode wird verwendet, um Informationen/Ressourcen abzurufen. Weil GET die Ressourcen nicht verändert, gilt diese Methode als sicher und sollte immer der gleiche Ergebnis zurück liefern, bis eine andere HTTP-Methode den Zustand ändert.

  - **POST**: POST wird dafür verwendet neue Ressourcen (z.B ein neues File oder einen neuen Eintrag in einer Datenbank) zu erstellen. Weil POST die Ressourcen verändert, ist diese Methode nicht sicher. Wenn ein POST-Request zweimal ausgeführt wird, werden zwei Ressourcen erstellt, die sich lediglich durch die Ressourcen-ID unterscheiden.

  - **PUT**: PUT wird dafür verwendet eine Ressource zu updaten. Wenn diese Ressource noch nicht existiert, wird entweder die Ressource erstellt, oder die Anfrage verworfen.

  - **DELTE**: DELETE löscht eine Ressource.

  - **PATCH**: Mit der PATCH-Methode kann man einen Teil einer Ressource updaten. Eigentlich ist das im Gegensatz zu PUT der korrekte Weg eine Ressource zu updaten, wenn man sie nicht komplett ersetzten will, allerdings unterstützen viele Framworks diese Methode nicht ganz oder nur fehlerhaft.

    

- Welche Datenbasis bietet sich für einen solchen Use-Case an?

  In diesem Use-Case bietet sich eine dokumentenbasierte Datenbank an, weil sich das Schema später ändern kann (z.B. Geburtsdatum, Präferenzen hinzufügen). Außerdem wird wesentlich häufiger auf die Daten lesen zugegriffen, als Daten geändert werden.

  Aufgrund des Problems mit dem Schema kommt eine relationale Datenbank(MySQL) nicht in Frage. Ich würde hier MongoDB verwenden.

  

- Welche Erfordernisse bezüglich der Datenbasis sollten hier bedacht werden?
  
  Dabei sollte beachtet werden, dass die Datenbank, die eine gute Schnittstelle hat, und man mithilfe einer API darauf zugreifen kann. 
  
  Weil die Daten der REST-Schnittstelle entweder als XML oder JSON zurückgegeben werden, sollte die Datenbank mit diesen Formaten umgehen können, damit das Programm vereinfacht werden kann. 
  
  Weiters ist es wichtig das CAP-Theorem zu beachten, und dass immer nur zwei der drei Eigenschaften erfüllt sein können. [^5]
  
  
  
  ![CAP Theorem](images/research/CAP-Theorem-last.jpg.webp)
  
  
  
- Verschiedene Frameworks bieten schnelle Umsetzungsmöglichkeiten,  welche Eckpunkte müssen jedoch bei einer öffentlichen Bereitstellung  (Production) von solchen Services beachtet werden?
  

## Quellen

[^1]: Computerweekly: [www.computerweekly.com](https://www.computerweekly.com/de/definition/RESTful-API) (15.12.2021)
[^2]: HTTP Methods: [restfulapi.net](https://restfulapi.net/http-methods/) (15.12.2021)

[^3]: CAP-Theorem: [www.educba.com](https://www.educba.com/cap-theorem/) (15.12.2021)

