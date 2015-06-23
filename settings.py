# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:53:38 2015

@author: Henry
"""

class Settings:
    """
        Contains all constant used throughout the project.
    """
    
    nbAtomsPerCell = 4
    nbPlayers = 9
    
    def decomp(self,x):
        b = 1
        i = 2
        while i*i <= x:
            if x % i == 0:
                b = i
            i += 1
        return b, x//b

#    def f(self):
#        return self.decomp(nbPlayers) + self.decomp(nbAtomsPerCell)
        
    
    gridWidth = 571
    gridHeight = 581
    
#    decomposition = f(nbPlayers,nbAtomsPerCell)

#    cellWidthInAtoms = decomp(nbAtomsPerCell)[1]
#    cellHeightInAtoms = decomp(nbAtomsPerCell)[0]
#    gridWidthInCells = decomp(nbPlayers)[1]
#    gridHeightInCells = decomp(nbPlayers)[0]

    cellWidthInAtoms = 2
    cellHeightInAtoms = 2
    gridWidthInCells = 3
    gridHeightInCells = 3
    
    n,m = cellHeightInAtoms*gridHeightInCells, cellWidthInAtoms*gridWidthInCells  # matrix of atoms, dimensions
    
    atomMargin = 4
    cellMargin = 8
    atomWidth = (gridWidth - (m-1)*atomMargin - (gridWidthInCells-1)*cellMargin) // m
    atomHeight = (gridHeight - (n-1)*atomMargin - (gridHeightInCells-1)*cellMargin) // n
    
    edgeLeftMargin = (gridWidth - (atomWidth+atomMargin)*m + atomMargin - (gridWidthInCells-1)*cellMargin ) // 2
    edgeTopMargin = (gridHeight - (atomHeight+atomMargin)*n + atomMargin - (gridHeightInCells-1)*cellMargin ) // 2
