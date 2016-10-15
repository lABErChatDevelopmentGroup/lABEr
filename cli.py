#Command-line-interface for lABEr
from networking import ChatServer
import serwork as sw
import sys

other_ips = sys.argv[1:]
ip = sw.getMyIp()

print("Your IP: " + ip)
username = input("Your Username: ")
print("--------------------------------------------------------------------------------------------")
def printOut(msg):
    print(msg)
ChatServer.startchat(printOut)
while True:
    inp = input("")
    ChatServer.send(username, inp, other_ips, ip)
