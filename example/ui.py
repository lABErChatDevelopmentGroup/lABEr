#!/usr/bin/python3
from networking import ChatServer
import serwork as sw
import uilib

CS = ChatServer()
ui = uilib.ChatUI(CS)

def postMsg(msg, data):
    data = msg.split("~:split:~")
    ui.postMessage(data[0], data[1])
    return ""

CS.startchat(postMsg)
ui.show()

#nchat.ChatServer.send(uilib.ChatUI().getuser(), uilib.ChatUI().gettext(), uilib.ChatUI().getotherips(), sw.getMyIP
