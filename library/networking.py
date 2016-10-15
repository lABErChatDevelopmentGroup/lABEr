"""
lABEr
=====
The ChatServer for lABEr.
"""
import threading
from time import sleep
import serwork as sw
import uilib as tui
from serwork import *

#Recive messages
def recive(recive_fp):
    ts = sw.SWServer(("", 2911))
    ts.run(recive_fp, 2048)

#The char server for lABEr
class ChatServer:
    def __init(self):
        pass

    def startchat(recive_fp):
        #Start reciving thread
        recive_t = threading.Thread(None, recive, None, (recive_fp,))
        recive_t.start()

    #Send a message
    def send(username, message, other_ip, your_ip):
        for i in other_ip:
            if i in ['127.0.0.1', your_ip]: #Do not allow sending messages to lo
                continue
            sc = sw.SWClient((i, 2911))
            sc.sendData(username + "~:split:~" + message)
