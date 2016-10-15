#!/usr/bin/python3
import networking as nchat
import uilib
nchat.ChatServer.startchat(uilib.ChatUI.postMessage)
