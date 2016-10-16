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
#### lABEr 0.1
"< username > ~:split:~ ~:split:~ < type > ~:split:~ < inhalt >"
 * username: Alias for the user
 * type: ~:msg:~ = message ~:file:~ = file
 * inhalt: Message

#### lABEr 0.2 (Development) (evtl. JSON)
"< lABEr version > ~:split:~ < ip address> ~:split:~ < username > ~:split:~ < typ > ~:split:~ < inhalt >"
 * lABEr version: Version des Protokolls
 * ip address: IP des Absenders
 * username: User alias
 * typ: Dateityp (bsp: text/plain, text/html, file/pdf, file/png)
 * inhalt: Datei/Text
