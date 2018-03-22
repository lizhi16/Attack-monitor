#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: client.py
socket client
"""

import socket
import sys


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('211.69.198.169', 6666))
    except socket.error as msg:
        print msg
        sys.exit(1)
    data = sys.argv[1]
    s.send(data)
    s.close()


if __name__ == '__main__':
    socket_client()
