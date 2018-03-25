#!/bin/bash

time apt-get install gcc make nmap nasm vim python -y

time git clone https://github.com/lizhi16/dirtycow.git

time sleep 55s

time nmap -A -T4 127.0.0.1

time sleep 20s

cd dirtycow && make 
