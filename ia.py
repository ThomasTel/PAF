#à orienter objet
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
   r = [[0] * nbCol for _ in range(nbLin)]
   vu = [[False] * nbCol for _ in range(nbLin)]
   q = []
   for i in range(nbLinsCell):
      if b != 0:
         q.append((a+i, b))
      if b+nbColsCell != nbCol:
         q.append((a+i, b+nbColsCell-1))
   for j in range(nbColsCell):
      if a != 0:
         q.append((a, b+j))
      if a+nbLinsCell != nbLin:
         q.append((a+nbLinsCell-1, b+j))
   while q:
      nq = []
      for i, j in q:
         if not vu[i-a][j-b]:
            n = 0
            s = 0
            for x, y in vois(i, j):
               if isIn(x, y, nbLin, nbCol):
                  if not inRect(x, y, a, b, nbLinsCell, nbColsCell):
                     s += t[x][y]
                     n += 1
                  elif vu[x-a][y-b]:
                     s += r[x-a][y-b]
                     n += 1
                  else:
                     nq.append((x, y))
            if n != 0: #impossible
               r[i-a][j-b] = int(s / n + 0.5) - (0 if n % 2 == 1 else rand(0))
      for i, j in q:
         vu[i-a][j-b] = True
      q = nq[:]
   return r
   
nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell = genereDims()
t = genereMat(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell)
afficheMat(nbColsCell, nbLinsCell, t)
a = rand(nbCellsLin) * nbLinsCell
b = rand(nbCellsCol) * nbColsCell
print()
print(a//nbLinsCell, b//nbColsCell)
print()
r = but(a, b, nbLinsCell, nbColsCell, t)
for i in range(nbLinsCell):
   for j in range(nbColsCell):
      print(r[i][j], end="")
   print()
   