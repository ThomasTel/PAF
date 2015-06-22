#à orienter objet
#algo idiot (pas pensé au bord), se contenter d'un simple parcours en largeur
from genere_tests import *

def isIn(lin, col, nbLin, nbCol):
   return 0 <= lin and lin < nbLin and 0 <= col and col < nbCol

def vois(i, j):
   return [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]

def inRect(lin, col, a, b, nbLinsCell, nbColsCell):
   return a <= lin and lin < a + nbLinsCell and b <= col and col < b + nbColsCell

def but(a, b, nbLinsCell, nbColsCell, t):
   nbLin = len(t)
   nbCol = len(t[0])
   r = [[9] * nbCol for _ in range(nbLin)]
   for k in range((min(nbLinsCell, nbColsCell)+1)//2):
      for _ in range(2):
         for i in range(a+k, a+nbLinsCell-k):
            for j in [b+k, b+nbColsCell-k]:
               m = 0
               n = 0
               for x, y in vois(i, j) :
                  if not isIn(x, y, nbLin, nbCol):
                     continue
                  if k == 0:
                     if not inRect(x, y, a, b, nbLinsCell, nbColsCell):
                        m += t[x][y]
                        n += 1
                  elif r[x-(a+k)][y-(b+k)] != -1:
                     m += r[x-(a+k)][y-(b+k)]
                     n += 1
               if n > 0:
                  m = int(m / n + 0.5)
                  r[i-(a+k)][j-(b+k)] = m
         a, b = b, a
         nbLinsCell, nbColsCell = nbColsCell, nbLinsCell
   return r

nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = genereDims()
t = genereMat(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell)
afficheMat(nbColsCell, nbLinsCell, t)
a = rand(nbCellsLin) * nbCellsLin
b = rand(nbCellsCol) * nbCellsCol
r = but(a, b, nbLinsCell, nbColsCell, t)
print()
print(a, b)
for i in range(nbLinsCell):
   for j in range(nbColsCell):
      print(r[i][j], end="")
   print()
   