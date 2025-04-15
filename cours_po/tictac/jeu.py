from board import board
from ticX import X
from ticO import O

class jeu:
    def __init__(self):
        self.game = board()
        self.coup = 0
    
    def win(self):
        for i in range(3):
            a = self.game.checkline(i)
            if a[0] == a[1] == a[2]:
                print(a[0], " win the game")
                return True
            else:
                pass
        for j in range(3):
            b = self.game.checkcolone(j)
            if b[0] == b[1] == b[2]:
                print(b[0]," win the game")
                return True
            else:
                pass
        for k in range(2):
            c = self.game.checkdiag(k)
            if c[0] == c[1] == c[2]:
                print(c[0]," win the game")
                return True
            else:
                pass
        return  False

    def draw(self):
        if self.coup >= 9 and self.win() == 0:
            print("match null")
            return True

    def turn(self):
        while True:
            self.coup += 1
            if self.draw():
                self.draw
            elif self.coup % 2 == 1 and not self.win():
                lig = input("")
                col = input("")
                self.game.add(lig, col, X)
            elif self.coup % 2 == 0 and not self.win():
                while True:    
                    lig = input("")
                    col = input("")
                    if self.game.add(lig, col, O):
                        break
                    else:
                        continue
            