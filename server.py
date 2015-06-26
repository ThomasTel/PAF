# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:34:41 2015

@author: Henry
"""
import socket
from threading import Thread
import time
import math
import random
from settings import Settings
from PyQt4.QtCore import SIGNAL, QObject

class ClientThread(Thread):
    """
        Thread class that handles one connection to the server.
        Sends to its client all changes that occur.
    """
    def __init__(self,settings, server, socket, address, id):
        Thread.__init__(self)
        self.setDaemon(True)
        self.socket = socket
        self.addr = address
        self.settings = settings
        self.id = id
        self.server = server
        self.start()
        
    def run(self):
        while 1:
            data = self.socket.recv(1024).decode().split()
            if data[0] == "Connecting":
                response = "New " + str(self.server.numClients)                
                self.server.sendToAll(response)
                print("Client connected and grid data sent to all.")
                self.server.emit(SIGNAL("redraw"))
                
            if data[0] == "Disconnecting":
                print("A client is disconnecting")
                self.server.removeClient(self)
                response = "New " + str(self.server.numClients)
                self.server.sendToAll(response)
                self.server.emit(SIGNAL("redraw"))
                break
            if data[0] == "Changing":
                response = "Changing " + data[1] + " " + data[2]
                self.server.sendToAll(response)
                self.server.emit(SIGNAL("change"),int(data[1]),int(data[2]))
            
    def send(self,message):
        self.socket.send((message + " " + str(self.id)).encode())

class AIThread(Thread):
    def __init__(self,settings,server,gridView,id):
        Thread.__init__(self)
        self.id = id
        self.settings = settings
        self.cellI = id // self.settings.gridWidthInCells
        self.cellJ = id % self.settings.gridWidthInCells
        self.gridView = gridView
        self.server = server
        self.setDaemon(True)
        self.period = random.uniform(0.5,2.0)
        self.matrix = self.gridView.scene.grid.matrix
        
    def doShit(self):
#        c1, c2 = self.complexity(0), self.complexity(1)
#        print("Complexity : " + str(self.id) + " " +str(c1) + " " +str(c2))
#        matrix = self.gridView.scene.grid.matrix
#        
#        if (c1 < c2 and matrix[self.cellI][self.cellJ].state == 1)\
#        or (c2 < c1 and matrix[self.cellI][self.cellJ].state == 0):
#            self.server.sendToAll("Changing +" + str(self.cellI) + " " + str(self.cellJ))
#            self.gridView.changeAtom(self.cellI,self.cellJ)       
    
        i = self.cellI * self.settings.cellHeightInAtoms
        j = self.cellJ * self.settings.cellWidthInAtoms
        cells = [(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
        
        for p,q in cells:
            neighbours = self.neighbours(self,p,q)
            for r,s in neighbours:
                if self.isIn(r,s):
                    c1,c2 = self.complexity(0), self.complexity(1)
             
        
    def complexity(self,p,q,state):
#        matrix = self.gridView.scene.grid.matrix
#        nState = 1
#        for i in range(self.settings.n):
#            for j in range(self.settings.m):
#                if i//self.settings.cellHeightInAtoms != self.cellI and j//self.settings.cellWidthInAtoms != self.cellJ:
#                    if matrix[i][j].state == state:
#                        nState += 1
#        return 1 + math.floor(math.log(nState,2))
        matrix = self.gridView.scene.grid.matrix
        nState = 1
        neighbours = self.neighbours(p,q)
        
        for i,j in neighbours:
            if self.isIn(i,j):
                if matrix[i][j].state == state:
                    nState += 1
        
        return 1 + nState
        
    def isIn(self,i,j):
        return i>=0 and i<self.settings.n and j>=0 and j<self.settings.m
        
    def neighbours(self,i,j):
        return [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
#        p = i*self.settings.cellHeightInAtoms
#        q = j*self.settings.cellWidthInAtoms
#        return [(p-1,q-1),(p-1,q),(p-1,q+1),(p-1,q+2),(p,q-1),(p,q+2),(p+1,q-1),(p+1,q+2),(p+2,q-1),(p+2,q),(p+2,q+1),(p+2,q+2)]
    
        
    def run(self):
        self.doShit()
        while 1:
            time.sleep(self.period)
            self.doShit()
            
    def send(self,message):
        pass
#        data = message.split()
#        if data[0] == "New":
#            self.settings.update(int(data[1]))
    
    def updateId(self):
        self.cellI = self.id // self.settings.gridWidthInCells
        self.cellJ = self.id % self.settings.gridWidthInCells

class Server(Thread,QObject):
    def __init__(self,settings,parent,port=2323):
        Thread.__init__(self)
        QObject.__init__(self)
        self.host = "localhost"
        self.port = port
        self.settings = settings
        self.parent = parent
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.numClients = 0
        self.serverSocket.bind((self.host,self.port))
        self.clientList = []
        self.serverSocket.listen(5)
        print("Server started listening")
        
    def run(self):
        print("Server Thread started")
        self.startAIs()
        while 1:
            clientSocket,address = self.serverSocket.accept()
            self.addClient(clientSocket,address)
        
    def sendToAll(self,message):
        for client in self.clientList:
            client.send(message)
            
    def addClient(self,clientSocket,address):
        self.numClients += 1
        self.settings.update(self.numClients)
        client = ClientThread(self.settings,self,clientSocket, address, self.numClients-1)
        self.clientList.append(client)
        print("Connection found! Client number " + str(self.numClients))
        self.updateAIPermissions()
        
    def addAI(self):
        self.numClients+=1
        self.settings.update(self.numClients)
        ai = AIThread(self.settings,self, self.parent.gridView, self.numClients-1)
        self.clientList.append(ai)
        print("AI added! number: " + str(self.numClients))
        
        response = "New " + str(self.numClients)                
        self.sendToAll(response)
        print("AI added and grid data sent to all.")
        self.emit(SIGNAL("redraw"))
        self.updateAIPermissions()
        
    def updateAIPermissions(self):
        for ai in self.clientList:
            if isinstance(ai,AIThread):
                ai.updateId()
                
    def startAIs(self):
        for ai in self.clientList:
            if isinstance(ai,AIThread):
                ai.start()
            
    def removeClient(self,client):
        self.clientList.remove(client)
        self.numClients -= 1
        self.settings.update(self.numClients)
        id = 0
        for client in self.clientList:
            client.id = id
            id+=1
