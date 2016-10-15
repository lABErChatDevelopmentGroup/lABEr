from ipaddress import IPv4Network
import serwork as sw

ip = input("Ip: ")

sc = sw.SWClient((ip, 2911))
sc.sendData("Hallo!")
