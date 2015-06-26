# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:36:08 2015

@author: Henry
"""

import socket
from settings import Settings
from threading import Thread
from PyQt4.QtCore import SIGNAL, QObject

class ListenThread(Thread):
    def __init__(self,settings,client):
        Thread.__init__(self)
        self.setDaemon(True)
        self.client = client
        self.settings = settings
        self.on = True
        self.start()
    
    def run(self):
        while 1:
            if self.on:
                data = self.client.clientSocket.recv(1024).decode().split()
                if data[0] == "Changing":
                    print("Received change message: " + data[1] + " " + data[2])
                    self.client.emit(SIGNAL("change"),int(data[1]),int(data[2]))
                    #change atom in question
                if data[0] == "New":
                    self.settings.update(int(data[1]))
                    self.client.updateId(int(data[2]))
                    #redraw
                    self.client.emit(SIGNAL("redraw"))
            else:
                print("Closing socket")
                self.client.clientSocket.close()
                break     
                

class Client(QObject):
    """
        Class that handles connecting to server.
        First connexion : 
            -> Send "Connecting" to server
            -> Server responds with the number of players.
                Instance of settings recalculates params for redraw
            THIS INFORMATION (except id) IS SENT TO ALL PLAYERS SO THAT THEY CAN READJUST THEIR GRIDS
        Other information can only be atom changes or disconnection
        Disconnection :
            -> Send "Disconnecting"
            -> Send id
            And then disable clientSocket
    """
    def __init__(self,settings,parent,port=2323):
        QObject.__init__(self)
        self.host = "localhost"
        self.port = port
        self.parent = parent
        self.settings = settings
        self.connected = False
        self.id = 0 #default
        
    def connect(self):
        if not self.connected:
            print("Connecting")
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((self.host,self.port))
            self.clientSocket.send("Connecting".encode())
            data = self.clientSocket.recv(1024).decode()
            print("Received data : " + data)
            data = data.split()
            if data[0] == "New":
                self.settings.update(int(data[1]))
                self.updateId(int(data[2]))
                self.parent.gridView.drawGrid()
            self.listenThread = ListenThread(self.settings,self)
            self.connected = True
        
    def disconnect(self):
        if self.connected:
            print("Disconnecting")
            self.clientSocket.send("Disconnecting ".encode())
            self.listenThread.on = False
            self.parent.gridView.scene.reset()
            self.connected = False
        
    def change(self,i,j):
        response = "Changing " + str(i) + " " + str(j)
        self.clientSocket.send(response.encode())
    
    def updateId(self,id):
        print("Id updated. New id: " + str(id))
        self.id = id
        self.cellI = id // self.settings.gridWidthInCells
        self.cellJ = id % self.settings.gridWidthInCells
        


        
    
