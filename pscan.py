import socket
from netaddr import IPNetwork
import sys


if len(sys.argv) < 3:
    print("Usage: portscanner.py IP -port(s)-")
else:
    port = sys.argv[2]
    port = port.replace('-', ' ').split(' ')
    if (len(port) > 1):
        range_start = int(port[0])
        range_end = int(port[1]) + 1
        port_range = range(range_start, range_end)
    else:
        range_start = int(port[0])
        range_end = int(port[0]) + 1
        port_range = range(range_start, range_end)
    
    
    for ip in IPNetwork(sys.argv[1]):
        for port in port_range:
            s = socket.socket()
            try:
                s.connect((str(ip), port))
                print("[+]Port %d is open on %s" % (port, str(ip)))
                s.close()
            except Exception as e:
                s.close()
