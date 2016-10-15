import serwork as sw
ts = sw.SWServer((sw.getMyIp(), 2911))
def msgP(data, hosts):
    print(data)
    return ""
ts.run(msgP, 1024)
