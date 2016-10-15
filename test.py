from ipaddress import IPv4Network
import serwork as sw
ip_ =  sw.getMyIp()
ip = IPv4Network(ip_)
brad = str(ip.broadcast_address)
print(brad)

sc = sw.SWClient((brad, 2911))
sc.sendData("Hallo!")
