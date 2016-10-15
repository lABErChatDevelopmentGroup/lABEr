#Command-line-interface for lABEr
from networking import ChatServer
import serwork as sw
import sys

def printOut(msg, data):
    msg = msg.split("~:split:~")
    print(msg[0] + ": " + msg[1])
    return ""

other_ips = sys.argv[1:]
ip = sw.getMyIp()

print("Your IP: " + ip)
username = input("Your Username: ")
print("--------------------------------------------------------------------------------------------")

CS = ChatServer()
CS.startchat(printOut)
while True:
    inp = input()
    CS.sendmsg(username, inp, other_ips, ip)
