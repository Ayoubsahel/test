from tes2 import tes2
class tes1:
    
    a = {1: None, 2: None, 3: None, 
     4: None, 5: None, 6: None,
     7: None, 8: None, 9: None}

    
    def __init__(self):
        self.abc = tes1.a
    def add(self,ind,sig):
        self.abc[ind] = str(sig())


a =tes1()

for i in range(1,9,2):
    a.add(i,tes2)

print(a.abc)