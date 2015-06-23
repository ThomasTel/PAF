# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:36:08 2015

@author: Henry
"""

import socket
from settings import Settings

class Client():
    """
        Class that handles connecting to server.
        First connexion : 
            -> Send "Connecting" to server
            -> Server responds with the following parameters after recalculation:
            id, cellWidthInAtoms, cellHeightInAtoms, gridWidthInAtoms, gridHeightInAtoms
            THIS INFORMATION (except id) IS SENT TO ALL PLAYERS SO THAT THEY CAN READJUST THEIR GRIDS
        Other information can only be atom changes or disconnection
        Disconnection :
            -> Send "Disconnecting"
            -> Send id
            And then disable clientSocket
    """
    def __init__(self,port=2323):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = port
        
    def connect(self):
        self.clientSocket.connect((self.host,self.port))
        self.clientSocket.send("Connecting".encode())
        self.id = int(self.clientSocket.recv(1024).decode())
        Settings.cellWidthInAtoms = int(self.clientSocket.recv(1024).decode())
        Settings.cellHeightInAtoms = int(self.clientSocket.recv(1024).decode())
        Settings.gridWidthInCells = int(self.clientSocket.recv(1024).decode())
        Settings.gridHeightInCells = int(self.clientSocket.recv(1024).decode())
        
    def disconnect(self):
        self.clientSocket.send("Disconnecting".encode())
        self.clientSocket.send(str(self.id).encode())
        self.clientSocket.close()
        
    def change(self,i,j):
        self.clientSocket.send("Changing".encode())
        self.clientSocket.send((str(i)+str(j)).encode())



        
    
