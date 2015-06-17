from random import *
from taille import f, affiche

def rand(n):
   return int(random() * n)

def genereDimensions():
   NB_CELLS_MAX = 10
   NB_ATOMES_CELLS_MAX = 30
   nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = (1, 1, 1, 1)
   while nbCellsLin == 1 or nbCellsCol == 1 or nbColsCell == 1 or nbLinsCell == 1:
      nbCells = rand(NB_CELLS_MAX)
      nbAtomesCell = rand(NB_ATOMES_CELLS_MAX)
      nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = f(nbCells, nbAtomesCell)
   return nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell

nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = genereDimensions()
nbLin = nbCellsLin * nbLinsCell
nbCol = nbCellsCol * nbColsCell
t = [[0] * nbCol for _ in range(nbLin)]
n = rand(nbLin * nbCol)
for _ in range(n):
   t[rand(nbLin)][rand(nbCol)] = 1
#affiche(2, 2, 1, 1, [[0, 1], [1, 0]])
affiche(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell, t)