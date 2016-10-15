import socket

def getMyName():
    "Returns your local Hostname"
    return socket.gethostname()
def getMyIp():
    "Returns your local Ip"
    return name2Ip(socket.gethostname())

def name2Ip(name):
    "Converts Hostname to Ip"
    return socket.gethostbyname(name)

def ip2Name(ip):
    "Converts Ip to Hostname"
    return socket.gethostbyaddr(ip)[0]

def string2bytes(string, charset="utf-8"):
    "Converts <string> to send-able bytestring with charset <charset>"
    return bytes(string, charset)

def bytes2string(bytes_, charset="utf-8"):
    "Converts <bytes> to use-able string with charset <charset>"
    return str(bytes_, charset)

class ServerAdress:
    "Shortcut for some Serverops"
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def getAddrTuple(self):
        return (self.hostname, self.port)

    def getHostname(self):
        return self.hostname

    def getPort(self):
        return self.port

    def getIP(self):
        return name2Ip(self.hostname)


class SWClient:
    "UDP-Client"
    def __init__(self, server):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if type(server) == ServerAdress:
            server = server.getAddrTuple()
        self.server = server

    def sendData(self, string, length=2048):
        self.socket.connect(self.server)
        self.socket.sendall(string2bytes(string))
        data = self.socket.recv(length)
        return bytes2string(data)

    def getData(self, length=2048):
        self.socket.connect(self.server)
        data, addr = self.socket.recvfrom(length)
        return bytes2string(data)

    def __del__(self):
        self.socket.close()

class SWServer:
    "UDP-Server"
    def __init__(self, server):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if server.__class__ == ServerAdress:
            server = server.getAddrTuple()
        self.server = server
        self.socket.bind(self.server)
        self.running = True

    def run(self, cbfunc, length):
        while self.running:
            self.socket.listen(5)
            server, addr = self.socket.accept()
            if not self.running:
                break
            data = bytes2string(server.recv(length))
            retdata = cbfunc(data, {'adress':addr, 'self':self.server})
            retdata = string2bytes(retdata)
            server.send(retdata)
            server.close()
        self.server_socket.close()

    def stop(self):
        self.running = False
