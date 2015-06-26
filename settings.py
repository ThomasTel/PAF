# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:53:38 2015

@author: Henry
"""

class Settings:
    """
        Contains all constant used throughout the project.
    """
    def __init__(self):
        self.nbAtomsPerCell = 4
        self.nbPlayers = 1
        self.gridWidth = 571
        self.gridHeight = 581
        self.atomMargin = 4
        self.cellMargin = 8
        self.update(self.nbPlayers)
        
    
    def decomp(self,x):
        b = 1
        i = 2
        while i*i <= x:
            if x % i == 0:
                b = i
            i += 1
        return b, x//b

    def update(self,nbPlayers):
        if nbPlayers == 0:
            nbPlayers = 1
        self.nbPlayers = nbPlayers
        self.cellWidthInAtoms = self.decomp(self.nbAtomsPerCell)[1]
        self.cellHeightInAtoms = self.decomp(self.nbAtomsPerCell)[0]
        self.gridWidthInCells = self.decomp(nbPlayers)[1]
        self.gridHeightInCells = self.decomp(nbPlayers)[0]
        print("Settings updated : nbPlayers = " + str(self.nbPlayers))
        print("\t New dimensions : " + str(self.cellWidthInAtoms) + " " + str(self.cellHeightInAtoms) + " " + str(self.gridWidthInCells) + " " + str(self.gridHeightInCells))
        
        self.n = self.cellHeightInAtoms*self.gridHeightInCells  # matrix of atoms, dimensions
        self.m = self.cellWidthInAtoms*self.gridWidthInCells
        
        self.atomWidth = (self.gridWidth - (self.m-1)*self.atomMargin - (self.gridWidthInCells-1)*self.cellMargin) // self.m
        self.atomHeight = (self.gridHeight - (self.n-1)*self.atomMargin - (self.gridHeightInCells-1)*self.cellMargin) // self.n
        
        self.edgeLeftMargin = (self.gridWidth - (self.atomWidth+self.atomMargin)*self.m + self.atomMargin - (self.gridWidthInCells-1)*self.cellMargin ) // 2
        self.edgeTopMargin = (self.gridHeight - (self.atomHeight+self.atomMargin)*self.n + self.atomMargin - (self.gridHeightInCells-1)*self.cellMargin ) // 2
    
 
