from genere_tests import *

def isIn(lin, col, nbLins, nbCols):
   return 0 <= lin and lin < nbLins and 0 <= col and col < nbCols

def vois(i, j):
   return [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1][j-1],[i+1,j],[i+1,j+1]]

def sommeVoisin():
   for x, y in vois(i, j):
      print(i + "," + j)

def but(a, b, nbLinsCell, nbColsCell, t):
   nbLins = len(t)
   nbCols = len(t[0])
   t = [[-1] * nbCol for _ in range(nbLin)]
   for k in range((min(nbLinsCell, nbColsCell)+1)/2):
      for n in range(2):
         for i in range(a+k, a+nbLinsCell-k):
            for j in [b+k, b+nbColsCell-k]:
         a, b = b, a
         nbLinsCell, nbColsCell = nbColsCell, nbLinsCell
   return t

nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = genereDims()
t = genereMat(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell)
afficheMat(nbColsCell, nbLinsCell, t)
a = rand(nbCellsLin)
b = rand(nbCellsCol)
but(a, b, 