from ticX import X
from ticO import O
from fonct import replace
from tic import tic
import numpy as np

class board:
    
    a = np.array([[None, None, None],
                  [None, None, None],
                  [None, None, None]])

    def __init__(self):
        self.bd = board.a

    def __str__(self):
        rep = None
        l = []    
        for i in self.bd:
            for j in self.bd:
                l.append(j)
        replace(l,None," ")

        rep = f"{str(l[0])}|{str(l[1])}|{str(l[2])}", "---------------", f"{str(l[3])}|{str(l[4])}|{str(l[5])}", "---------------", f"{str(l[6])}|{str(l[7])}|{str(l[8])}"
              
        return rep
            

    def add(self, lig: int, col: int, signe: tic):
        if self.bd[lig][col] == None:
            self.bd[lig][col] = signe()
            print(str(self))
            return True
        else:
            print("case deja prise")
            return False
    
    def checkline(self, line: int):
        return self.bd[line]
    
    def checkcolone(self, colone:  int):
        for i in self.bd:
            a = np.array(i[colone])
        return a 
        
    def checkdiag(self, diag: int):
        if diag == 0:
            rep = np.array([self.bd[0][0], self[1][1], self.bd[2][2]])
        elif diag == 1:
            rep = np.array([self.bd[0][2], self[1][1], self.bd[2][0]])
        return rep
