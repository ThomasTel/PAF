# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:59:14 2015

@author: Henry
"""

from PyQt4 import QtCore
from PyQt4.QtGui import QGraphicsView, QGraphicsScene, QBrush
from PyQt4.QtCore import Qt
from settings import Settings
from elements import Atom
import numpy as np

class GridView(QGraphicsView):
    """
        Class that handles the GraphicsView Widget used to draw the grid.
    """
    def __init__(self,parent,scene,client=None):
        QGraphicsView.__init__(self,parent)
        self.scene = scene
        self.client = client
        self.setScene(scene)
        self.setGeometry(QtCore.QRect(10, 10,Settings.gridWidth,Settings.gridHeight)) # 571 581 for width and height.
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
    def changeState(self,item):
        item.state = 1 - item.state
        if item.state == 1:
            item.setBrush(QBrush(Qt.black))
        else:
            item.setBrush(QBrush(Qt.white))
        self.currentAtom = item
        self.client.change(item.i,item.j)
                
    def mousePressEvent(self,event):
        pos = event.pos()
        item = self.itemAt(pos)
        if item is not None:
            self.changeState(item)
            
    def mouseMoveEvent(self,event):
        pos = event.pos()
        item = self.itemAt(pos)
        if item is not None:
            if item != self.currentAtom:
                self.changeState(item)
                
    def drawGrid(self):
        for i in range(Settings.n):
            for j in range(Settings.m):
                #atom = self.grid.matrix[i][j]
                #print(str(Settings.atomWidth) + " " + str(Settings.atomHeight) + " ")
                #self.addRect(atom.i+1,atom.j+1,Settings.atomWidth,Settings.atomHeight)
                self.scene.addItem(self.scene.grid.matrix[i][j])
        self.show()
        

class GridArea(QGraphicsScene):
    """
        Class used to draw the grid in a GridView.
    """
    def __init__(self,grid):
        self.grid = grid
        QGraphicsScene.__init__(self,0,0,Settings.gridWidth,Settings.gridHeight)

        
        
    