"""
lABEr
=====
The ChatServer for lABEr.
"""
import threading
from time import sleep
import serwork as sw
import socket

#Recive messages
ts = None
def recive(recive_fp):
    global ts
    ts = sw.SWServer(("", 2911))
    ts.run(recive_fp, 2048)

def gettype(message):
    pass #Return message type

#The char server for lABEr
class ChatServer:
    def __init(self):
        pass

    def startchat(self, recive_fp):
        #Start reciving thread
        self.recive_t = threading.Thread(None, recive, None, (recive_fp,))
        self.recive_t.start()

    #Send a message
    def sendmsg(username, message, other_ip, your_ip):
        message = "~:msg:~" + message + "~:msg:~"
        for i in other_ip:
            if i in ['127.0.0.1', your_ip]: #Do not allow sending messages to lo
                continue
            sc = sw.SWClient((i, 2911))
            sc.sendData(username + "~:split:~" + message)

    def sendfile(username, file_path, other_ip, your_ip):
        fp = open(file_path, "r")

        message = "~:file:~" + fp.read() + "~:file:~"
        ChatServer.sendmsg(username, message, other_ip, your_ip)

    def stopchat(self):
        if ts != None:
            try:
                ts.socket.shutdown(socket.SHUT_RDWR)
            except:
                pass
            finally:
                ts.socket.close()
