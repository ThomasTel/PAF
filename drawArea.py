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
    def __init__(self,settings,parent,scene,client=None):
        QGraphicsView.__init__(self,parent)
        self.scene = scene
        self.settings = settings
        self.client = client
        self.setScene(scene)
        self.setGeometry(QtCore.QRect(10, 10,settings.gridWidth,settings.gridHeight)) # 571 581 for width and height.
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            
    def changeAtom(self,i,j):
        print("Change Atom called: " + str(i) + " " + str(j))
        atom = self.scene.grid.matrix[i][j]
        atom.state = 1 - atom.state
        if atom.state == 1:
            atom.setBrush(QBrush(Qt.black))
        else:
            atom.setBrush(QBrush(Qt.white))
                
    def mousePressEvent(self,event):
        pos = event.pos()
        item = self.itemAt(pos)
        if item is not None and self.client is not None:
            if self.client.cellI == item.i // self.settings.cellHeightInAtoms and self.client.cellJ == item.j // self.settings.cellWidthInAtoms:
                self.currentAtom = item
                self.client.change(item.i,item.j)
            
    def mouseMoveEvent(self,event):
        pos = event.pos()
        item = self.itemAt(pos)
        if item is not None and self.client is not None:
            if self.client.cellI == item.i // self.settings.cellHeightInAtoms and self.client.cellJ == item.j // self.settings.cellWidthInAtoms:
                if item != self.currentAtom:
                    self.currentAtom = item
                    self.client.change(item.i,item.j)
                
    def drawGrid(self):
        self.scene.reset()     
        for i in range(self.settings.n):
            for j in range(self.settings.m):
                self.scene.addItem(self.scene.grid.matrix[i][j])
        self.show()
        

class GridArea(QGraphicsScene):
    """
        Class used to draw the grid in a GridView.
    """
    def __init__(self,settings,grid):
        self.grid = grid
        QGraphicsScene.__init__(self,0,0,settings.gridWidth,settings.gridHeight)
    
    def reset(self):
        print("reset function called")
        self.clear()
        self.grid.createGrid()

        
        
    