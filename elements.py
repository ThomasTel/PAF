# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:38:20 2015

@author: Henry
"""

from settings import Settings
from PyQt4.QtGui import QGraphicsRectItem
import numpy as np

class Atom(QGraphicsRectItem):
    """
        Class that represents the smallest object a player or bot can act upon.
    """
    def __init__(self,settings,i,j,cellI,cellJ,state=0):
        QGraphicsRectItem.__init__(self,
                                   j*(settings.atomWidth+settings.atomMargin) + cellJ*settings.cellMargin + settings.edgeLeftMargin,
                                   i*(settings.atomHeight+settings.atomMargin) + cellI*settings.cellMargin + settings.edgeTopMargin,
                                   settings.atomWidth,
                                   settings.atomHeight)
        self.settings = settings
        self.i = i
        self.j = j
        self.state = state
    
class Grid:
    """
        Class that contains list of atoms and users.
    """
    def __init__(self,settings):
        self.settings = settings
        self.createGrid()
                
    def createGrid(self):
        self.matrix = np.array(self.settings.n*[self.settings.m*[Atom(self.settings,0,0,0,0,0)]])
        for i in range(self.settings.n):
            for j in range(self.settings.m):
                self.matrix[i][j]=Atom(self.settings,i, j, i//self.settings.cellHeightInAtoms, j//self.settings.cellWidthInAtoms)     
