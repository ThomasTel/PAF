from random import *
from taille import f, affiche

NB_CELLS_MAX = 10
NB_ATOMES_CELLS_MAX = 30

nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = (1, 1, 1, 1)
while nbCellsLin == 1 or nbCellsCol == 1 or nbColsCell == 1 or nbLinsCell == 1:
   nbCells = int(random() * NB_CELLS_MAX)
   nbAtomesCell = int(random() * NB_ATOMES_CELLS_MAX)
   nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = f(nbCells, nbAtomesCell)
affiche(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell)