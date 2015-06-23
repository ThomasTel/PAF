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
    def __init__(self,i,j,cellI,cellJ,state=0):
        QGraphicsRectItem.__init__(self,
                                   i*(Settings.atomWidth+Settings.atomMargin) + cellI*Settings.cellMargin + Settings.edgeLeftMargin, 
                                   j*(Settings.atomHeight+Settings.atomMargin) + cellJ*Settings.cellMargin + Settings.edgeTopMargin,
                                   Settings.atomWidth,
                                   Settings.atomHeight)
        self.i = i
        self.j = j
        self.state = state
        self.screenI = self.i*(Settings.atomWidth+Settings.atomMargin)
        self.screenJ = self.j*(Settings.atomHeight+Settings.atomMargin)
    
class Grid:
    """
        Class that contains list of atoms and users.
    """
    def __init__(self):
        self.matrix = np.array(Settings.n*[Settings.m*[Atom(0,0,0,0,0)]])
        for i in range(Settings.n):
            for j in range(Settings.m):
                self.matrix[i][j]=Atom(i, j, i//Settings.cellWidthInAtoms, j//Settings.cellHeightInAtoms)
                
