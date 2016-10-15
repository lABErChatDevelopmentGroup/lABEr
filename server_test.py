import serwork as sw
ip = sw.getMyIp()
print("launching on " + ip)
ts = sw.SWServer((ip, 2911))
def msgP(data, hosts):
    print(data)
    return ""
ts.run(msgP, 1024)
