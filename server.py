# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:34:41 2015

@author: Henry
"""
import socket
from threading import Thread

class Client(Thread):
    def __init__(self, socket, address, numClients):
        Thread.__init__(self)
        self.socket = socket
        self.addr = address
        self.id = numClients
        self.start()
        
    def run(self):
        while 1:
            data = self.socket.recv(1024).decode()
            print("Client n."+str(self.id)+": "+data)
            if data=='stop':
                break
            self.socket.send("Cheers mate".encode())

class Server():
    def __init__(self,port=2323):
        self.host = "localhost"
        self.port = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.numClients = 0
        self.serverSocket.bind((self.host,self.port))
        


serversocket.listen(5)
print("Server started listening")

while 1:
    clientsocket, address = serversocket.accept()
    numClients += 1
    client = Client(clientsocket, address, numClients)
    print("Connection found! Client number " + str(numClients))

#while 1:
#    data = clientsocket.recv(1024).decode()
#    print(data)
#    if data=="stop":
#        serversocket.close()
#        break
#    r="receive"
#    clientsocket.send(r.encode())