import serwork as sw
print("launching on " + sw.getMyIp())
ts = sw.SWServer((sw.getMyIp(), 2911))
def msgP(data, hosts):
    print(data)
    return ""
ts.run(msgP, 1024)
