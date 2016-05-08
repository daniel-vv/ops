#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver

class MyTCPHandle(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print("New Conn:>",self.client_address)
            data = self.request.recv(1024)
            if not data:break

            print('client says:',data.decode())
            self.request.send(data)

if __name__ == '__main__':
    HOST,PORT = '127.0.0.1',50001
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandle)
    server.serve_forever()


