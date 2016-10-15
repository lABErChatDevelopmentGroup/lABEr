"""
lABEr
=====
The ChatServer for lABEr.
"""
import threading
import serwork as sw

def send(server_ip):
    while True:
        sc = sw.SWClient((server_ip, 2911))
        sc.sendData(input("Nachricht: "))

def recive():
    ip = sw.getMyIp()
    print("launching server on " + ip)
    ts = sw.SWServer((ip, 2911))
    ts.run(msgP, 1024)

def msgP(data, hosts):
    print(data)
    return ""

from serwork import *

class ChatServer:
    "The ChatServer for lABEr"
    def __init(self):
        pass

    def startchat(server_ip):
        recive_t = threading.Thread(None, recive)
        send_t = threading.Thread(None, send, None, (server_ip,))

        recive_t.start()
        send_t.start()
