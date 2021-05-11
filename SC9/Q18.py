def recCount(L):
    if type(L) == int:
        return 1
    else:
        n = 0
        for i in L:
            n += recCount(i)
        return n

def mapCount(L):
    if type(L) == int:
        return 1
    else:
        n = sum(map(mapCount, L))
        return n

def recCount2(L):
    if type(L) == int:  # first base
        return 1
    if len(L) == 0 :  # second base: empty list
        return 0
    return recCount2(L[0]) + recCount2(L[1:])
        # one recursive call for current element, and 
        # 2nd recursive call for "the rest of the loop"


L = [1, 2, [3, 4, [5, 6, 7], 8,], 9, 10, [11, 12]]
print(recCount(L))
print(mapCount(L))
print(recCount2(L))