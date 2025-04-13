l = [None,4,5,5,7,None,None,None,8.54,"nna","reset","la",None]

def a(lst, word, remplace):
    for i in range(len(lst)):
        if lst[i] == word:
            lst[i] = remplace

a(l, 5, "a")
print(l)
