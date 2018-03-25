#!/usr/bin/env python
#coding:utf-8
'''
file:client.py
date:9/9/17 3:43 PM
author:lockey
email:lockey@123.com
desc:socket编程客户端，python3.6.2
'''
import socket,sys
HOST = '202.114.6.253'
PORT = 8998
ADDR =(HOST,PORT)
#BUFSIZE = 102400

sock = socket.socket()
try:
    sock.connect(ADDR)
    data = sys.argv[1]
    sock.sendall(data.encode('utf-8')) #不要用send()
    #recv_data = sock.recv(BUFSIZE)
    sock.close()
    sys.exit()
except Exception:
    print('error')
    sock.close()
    sys.exit()
