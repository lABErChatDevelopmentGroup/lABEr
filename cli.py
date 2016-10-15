#Command-line-interface for lABEr
from networking import ChatServer
import serwork as sw
import sys

other_ips = sys.argv[1:]
ip = sw.getMyIp()

print("Your IP: " + ip)
username = input("Your Username: ")
print("--------------------------------------------------------------------------------------------")
ChatServer.startchat(print)
while True:
    inp = input("")
    ChatServer.send(username, inp, other_ips, ip)
