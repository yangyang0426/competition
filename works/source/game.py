# -*- coding: utf-8 -*-
"""
Created on Thu May 07 17:24:16 2015

@author: Administrator
"""
import socket  
import sys 
def game_socket(serverIp,serverPort):
    address = (serverIp, serverPort)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect(address)  
    data = s.recv(512)
    while 1:
        print 'the data received is',data  
        msg = sys.stdin.readline()
        s.send(msg)    
        data = s.recv(512)
    s.close()  
print(__name__)

game_socket('127.0.0.1',8888)
