#!/usr/bin/env python
#coding:utf-8
'''
file:client.py
date:9/9/17 3:43 PM
author:lockey
email:lockey@123.com
desc:socket编程服务器端，python3.6.2
'''
from socketserver import BaseRequestHandler,ThreadingTCPServer
import threading
import time

BUF_SIZE=102400

class Handler(BaseRequestHandler):
    def handle(self):
        address,pid = self.client_address
        #print('%s connected!'%address)
        while True:
            data = self.request.recv(BUF_SIZE)
            if len(data)>0:
                print '---------------------------------------------------'
                time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print('Event',address,time_now,data.decode('utf-8'))
                print '---------------------------------------------------'
                cur_thread = threading.current_thread()
                #response = '{}:{}'.format(cur_thread.ident,data)
                #self.request.sendall('response'.encode('utf-8'))
                #print('send:','response')
            else:
               # print('close')
                break

if __name__ == '__main__':
    HOST = sys.argv[1]
    PORT = 8998
    ADDR = (HOST,PORT)
    server = ThreadingTCPServer(ADDR,Handler)  #参数为监听地址和已建立连接的处理类
    print('listening')
    server.serve_forever()  #监听，建立好TCP连接后，为该连接创建新的socket和线程，并由处理类中的handle方法处理
    print(server)
