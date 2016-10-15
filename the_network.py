"""
lABEr
=====
The ChatServer for lABEr.
"""
import threading
from time import sleep
import serwork as sw

import the_ui as tui

def send(username, message, other_ip, your_ip):
    sc = sw.SWClient((other_ip, 2911))
    sc.sendData(username + "~:split:~" + message)

UI = tui.ChatUI(send)

def recive():
    ts = sw.SWServer(("", 2911))
    ts.run(msgP, 2048)

def msgP(data, hosts):
    username, message = data.split("~:split:~")
    UI.postMessage(username, message)
    return ""

from serwork import *

class ChatServer:
    "The ChatServer for lABEr"
    def __init(self):
        pass

    def startchat():
        recive_t = threading.Thread(None, recive)

        recive_t.start()

        UI.show()
