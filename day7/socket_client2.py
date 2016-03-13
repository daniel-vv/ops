#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('请求占领地球,请求占领地球,请求占领地球','utf8'))

server_relay = sk.recv(1024)
print(str(server_relay,'utf8'))

while True:
    client_input = input('>>:').strip()
    sk.send(bytes(client_input,'utf8'))
    server_relay = sk.recv(1024)
    print(server_relay)
sk.close()



