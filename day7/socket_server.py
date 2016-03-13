#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

ip_port = ('127.0.0.1',9990)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server wating...')
    conn,addr = sk.accept()
    client_data = conn.recv(1024)
    print(str(client_data,'utf8'))
    conn.sendall(bytes('不要回答,不要回答,不要回答','utf8'))
    while True:
        client_send = sk.recv(1024)
        print(str(client_send,'utf8'))
        respons_to_client = input('>>:').strip()
        sk.send(bytes(respons_to_client,'utf8'))
    conn.close()


