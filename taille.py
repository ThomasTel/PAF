"""à partir de (nbCells, nbAtomesCells) on vise une matrice de sqrt(nbCells) par sqrt(nbCells)
 avec des cellules de sqrt(nbAtomesCells) par sqrt(nbAtomesCells)"""
def decomp(x):
   b = 1
   i = 2
   while i*i <= x:
      if x % i == 0:
         b = i
      i += 1
   return b, x//b

def f(nbCells, nbAtomesCells):
   return decomp(nbCells) + decomp(nbAtomesCells)

def affiche(nbCellsLin, nbCellsCol, nbColsCell, nbLinsCell):
   for i in range(nbCellsLin*nbLinsCell):
      if i % nbLinsCell == 0:
         print("")
      for j in range(nbCellsCol*nbColsCell):
         if j % nbColsCell == 0:
            print(" ", end="")
         print("x", end="")
      print("")

def main():
   nbCells = int(input())
   nbAtomesCells = int(input())
   affiche(*f(nbCells, nbAtomesCells))