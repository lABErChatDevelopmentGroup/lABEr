#!/usr/bin/python3
from networking import ChatServer
import serwork as sw
import uilib, json

CS = ChatServer()
ui = uilib.ChatUI(CS)

def postMsg(msg, data):
    msg = json.loads(msg)
    if msg['type'] == 'message':
        ui.postMessage(msg['username'],msg['value'])
    else:
        ui.postMessage("System", "Cannot find command " + msg['type'])
    return ""

CS.startchat(postMsg)
ui.show()

#nchat.ChatServer.send(uilib.ChatUI().getuser(), uilib.ChatUI().gettext(), uilib.ChatUI().getotherips(), sw.getMyIP
