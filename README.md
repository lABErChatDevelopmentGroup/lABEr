# lABEr
Ein einfacher, dezentraler CHAT-Client


###Voraussetzungen:
 * python3
 * python3 tkinter

## Clients:
* `example/cli.py < ip1 > < ip2 > ... < ipn >` führt das Beispielprogramm aus
* `example/ui.py` startet das grafische Beispiel
In der UI kann man mehrere IPs durch ein Semikolon( ';' ) getrennt angeben.

---

## Verwendung im Code:
#### Nötige Dateien im Projekt Ordner:
 * networking.py
 * serwork.py


#### Import:
 * `from networking import ChatServer`
 * `import serwork as sw`

#### Verwendung:
`ChatServer.startchat(fp)`
  * Empfängt alle Nachrichten und gibt diese an Funktion `fp` weiter
  * Bekommt empfangene Nachrichten als String


`ChatServer.send(username, message, other_ip, your_ip)`
  * Sendet nachrichten an IPs
  * `username`: Name der Benutzers (string)
  * `message`: Nachricht (string)
  * `other_ip`: Empfänger IPs als Array
  * `your_ip`: eigene IP (Kann man mit `sw.getMyIp()` bekommen
  
`ChatServer.stopchat()`
  * Chat-Server beenden

----

### Aussehen auf unterer Ebene
#### lABEr 0.1
`< username >~:split:~< inhalt >`
 * `username`: Pseudonym
 * `inhalt`: Nachricht

#### lABEr 0.2 (Development) (evtl. JSON)
`< lABEr version > ~:split:~ < ip address> ~:split:~ < username > ~:split:~ < typ > ~:split:~ < inhalt >`
 * `lABEr version`: Version des Protokolls
 * `ip address`: IP des Absenders
 * `username`: Pseudonym
 * `type`: Dateityp (Bsp.: text/plain, text/html, file/pdf, file/png)
 * `inhalt`: Datei/Text
