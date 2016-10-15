"""
lABEr
=====
The ChatServer for lABEr.
"""
import threading
from time import sleep
import serwork as sw
import the_ui as tui
from serwork import *

#Recive messages
def recive(recive_fp):
    ts = sw.SWServer(("", 2911))
    ts.run(recive_fp, 2048)

#Split message
def msgS(data, hosts):
    username, message = data.split("~:split:~")
    UI.postMessage(username, message)
    return ""

class ChatServer:
    "The ChatServer for lABEr"
    def __init(self):
        pass

    def startchat(recive_fp):
        #Start reciving thread
        recive_t = threading.Thread(None, recive, (recive_fp))
        recive_t.start()

    #Send a message
    def send(username, message, other_ip, your_ip):
        for i in other_ip:
            if i in ['127.0.0.1', your_ip]: #Do not allow sending messages to lo
                continue
            sc = sw.SWClient((i, 2911))
            sc.sendData(username + "~:split:~" + message)
