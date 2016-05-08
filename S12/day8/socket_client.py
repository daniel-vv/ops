#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

ip_port = ('127.0.0.1',50001)

sk = socket.socket()
sk.connect(ip_port)

while True:
    msg = input('>>:').strip()
    sk.sendall(bytes(msg,'utf8'))
    server_replay = sk.recv(1024)

    print('server replay:',str(server_replay),'utf8')
sk.close()




