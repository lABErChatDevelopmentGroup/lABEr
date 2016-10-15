from ipaddress import IPv4Network
import serwork as sw

#ip = input("Ip: ")
ip = "100.100.247.1"

sc = sw.SWClient((ip, 2911))
sc.sendData(input("Nachricht: "))
