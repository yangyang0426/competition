# -*- coding: utf-8 -*-
"""
Created on Thu May 07 14:52:18 2015

@author: Liuyang
function：socket通讯函数
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