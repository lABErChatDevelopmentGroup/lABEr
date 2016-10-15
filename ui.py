#!/usr/bin/python3
from networking import ChatServer
import serwork as sw
import uilib

ui = uilib.ChatUI(ChatServer.send)

def postMsg(msg, data):
    data = msg.split("~:split:~")
    ui.postMessage(data[0], data[1])
    return ""

ChatServer.startchat(postMsg)
ui.show()

#nchat.ChatServer.send(uilib.ChatUI().getuser(), uilib.ChatUI().gettext(), uilib.ChatUI().getotherips(), sw.getMyIP
