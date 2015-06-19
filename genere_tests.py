from random import *
from taille import f, afficheMat

def rand(n):
   return int(random() * n)

def genereDims():
   NB_CELLS_MAX = 10
   NB_ATOMES_CELLS_MAX = 30
   nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = (1, 1, 1, 1)
   while nbCellsLin == 1 or nbCellsCol == 1 or nbColsCell == 1 or nbLinsCell == 1:
      nbCells = rand(NB_CELLS_MAX)
      nbAtomesCell = rand(NB_ATOMES_CELLS_MAX)
      nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = f(nbCells, nbAtomesCell)
   return nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell

def genereMat(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell):
   nbLin = nbCellsLin * nbLinsCell
   nbCol = nbCellsCol * nbColsCell
   t = [[0] * nbCol for _ in range(nbLin)]
   for _ in range(rand(1.5 * nbLin * nbCol)):
      t[rand(nbLin)][rand(nbCol)] = 1
   return t
   
def main():
   #affiche(2, 2, 1, 1, [[0, 1], [1, 0]])
   nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = genereDims()
   t = genereMat(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell)
   afficheMat(nbColsCell, nbLinsCell, t)