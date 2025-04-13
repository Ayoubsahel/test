from tes2 import tes2
import numpy as np
class tes1:
    
    a = np.array([[None, None, None],
                  [None, None, None],
                  [None, None, None]])

    def __init__(self):
        self.abc = tes1.a
    def add(self,ind,col,sig):
        self.abc[ind][col] = str(sig())

a = tes1()

for i in range(1,3,2):
    for j in range(1,3):
        a.add(i,j,tes2)

print(a.abc)