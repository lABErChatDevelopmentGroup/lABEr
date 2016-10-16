#Command-line-interface for lABEr
from networking import ChatServer
import serwork as sw
import sys, json

def printOut(msg, data):
    msg = json.loads(msg)
    if msg['type'] == 'message':
        print(msg['username'] + ": " + msg['value'])
    else:
        print("Cannot find command " + msg['type'])
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
