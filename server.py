#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time
host = '172.16.51.14'
port = 9090
clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit = False

while not quit:
    try:
        (data, addr) = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)
        itsatime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
        print( '[' + addr[0] + ']=[' + str(addr[1]) + ']=[' + itsatime \
            + ']/')
        print (data.decode('utf-8'))
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:

        quit = True
s.close()
