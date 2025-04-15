from ticX import X
from ticO import O
from fonct import replace
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

        rep = f"{l[0]}|{l[1]}|{l[2]}", "---------------", f"{l[3]}|{l[4]}|{l[5]}", "---------------", f"{l[6]}|{l[7]}|{l[8]}"
              
        return rep
            

    def add(self,lig,col,signe):
        if self.bd[lig][col] == None:
            self.bd[lig][col] = signe()
        else:
            print("case deja prise")
    

        