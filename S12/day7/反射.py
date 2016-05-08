#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
class WebServer(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
    def start(self):
        print('Server is starting')
    def stop(self):
        print('Server is stopping...')
    def restart(self):
        self.stop()
        self.start()

def test_run(self,name):
    print('running...',name,self.host)

if __name__ == '__main__':
    server = WebServer('localhost',333)
    #server2 = WebServer('10.1.1.102',80)

    #print(sys.argv[1])

    dic_argv = {
        'stop': 'WebServer.stop'
        'start': 'WebServer.start''
        'restart': 'WebServer.restart'
    }
    #if sys.argv[1] in dic_argv:
    #   print(sys.argv[1]())
    #   #sys.argv[1]()
    '''
    if hasattr(server,sys.argv[1]):
        func = getattr(server,sys.argv[1])  #获取server.start的内存地址
        func()
    '''
    #setattr(server,'run',test_run)
    #server.run(server,'woyebuzhidao')

    #delattr(WebServer,'start')
    #print(server.restart)




