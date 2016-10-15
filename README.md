# lABEr
Ein einfacher, dezentraler CHAT-Client


Requirements:
 * python3
 * python3 tkinter

## Clients:
* run ` example/cli.py < ip1 > < ip2 > ... < ipn > ` to run an example Command-line-client
* run ` example/ui.py ` to run an example tkinter based User-Interface
In der UI kann man mehrere IPs durch ein Semikolon( ';' ) angeben

---

## Verwendung im Code:
#### Nötige Dateien im Projekt Ordner:
 * networking.py
 * serwork.py


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

### Aussehen auf unterer Ebene
## lABEr 1.0
"< username >~::~< inhalt >"
 * username: Alias for the user
 * inhalt: Message
