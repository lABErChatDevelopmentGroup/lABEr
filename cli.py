#!/usr/bin/python3
import the_network as nchat
import sys

if len(sys.argv) <= 1:
    print("Usage: " + sys.argv[0] + " <ip>")
    exit()

nchat.ChatServer.startchat(sys.argv[1])
