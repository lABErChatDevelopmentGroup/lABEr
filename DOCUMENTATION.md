# lABEr Documentation

### Nötige Dateien im Projekt Ordner:
 * networking.py
 * serwork.py

---

### Verwendung im code:
#### Import:
 * from networking import ChatServer
 * import serwork as sw

#### Verwendung:
 * ChatServer.startchat(fp)
  * Empfängt alle Nachrichten und gibt diese an Funktion fp weiter
  * Bekommt empfangene Nachrichten al String



 * ChatServer.send(username, message, other_ip, your_ip)
  * Sendet nachrichten an IPs
  * username: Name der Benutzers (string)
  * message: Nachricht (string)
  * other_ip: Empfänger IPs als Array
  * your_ip: eigene IP (Kann man mit sw.getMyIp() bekommen
----

### Textübertragung
## lABEr 1.0
"< username >~::~< inhalt >"
 * username: Alias for the user
 * inhalt: Message
