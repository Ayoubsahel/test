from jeu import jeu




def replace(lst: list, wd, rp):
    for i in range(len(lst)):
        if lst[i] == wd:
            lst[i] = rp

def play():
    game = jeu()
