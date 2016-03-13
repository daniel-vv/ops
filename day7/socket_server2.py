#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

ip_port = ('127.0.0.1',9999)
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
        '''
        try:
            client_data = conn.recv(1024)
            print(str(client_data,'utf8'))
        except Exception:
            print('client closed, break')
            break
        conn.send(client_data)
        '''

        client_data = conn.recv(1024)
        print(str(client_data,'utf8'))
        if not client_data:
            break
        conn.send(client_data)
    conn.close()


