"""
lABEr
=====
The ChatServer for lABEr.
"""
import threading
from time import sleep
import serwork as sw
import uilib as tui
import socket, json

#Recive messages
ts = None
def recive(recive_fp):
    global ts
    ts = sw.SWServer(("", 2911))
    ts.run(recive_fp, 2048)

#The char server for lABEr
class ChatServer:
    def __init(self):
        pass

    def startchat(self, recive_fp):
        #Start reciving thread
        self.recive_t = threading.Thread(None, recive, None, (recive_fp,))
        self.recive_t.start()

    #Send a message
    def sendmsg(self, username, message, other_ip, your_ip):
        for i in other_ip:
            if i in ['127.0.0.1', your_ip]: #Do not allow sending messages to lo
                continue
            sc = sw.SWClient((i, 2911))
            data = {
                'username': username,
                'ip': your_ip,
                'type': 'message',
                'value': message
            }
            sc.sendData(json.dumps(data))

    def stopchat(self):
        if ts != None:
            try:
                ts.socket.shutdown(socket.SHUT_RDWR)
            except:
                pass
            finally:
                ts.socket.close()
