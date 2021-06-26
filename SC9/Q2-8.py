# 2.
L0 = ['an', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away']
L0.sort(key = lambda x : len(x))
print(L0)

# 3. 
L1 = ['a', 'glass', 'of', 'water', 'is', 'empty', 'or', 'full']
L1.sort(key = lambda x : (len(x), ord(x[0])))
# 將要比較的特性包裝成 tuple，用 tuple 型態去比較
# 長度 (tuple[0]) 相等後會比較 ASCII CODE (tuple[1])
print(L1)

# 4.
ML = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MD = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
L2 = [ 'Apr', 'May', 'Nov', 'Mar', 'Jan', 'Feb', 'Oct','Jun', 'Jul', 'Aug', 'Sep', 'Dec']
L2.sort(key=lambda x: ML.index(x))
L2.sort(key=lambda x: MD[x])

# 8.
prt1 = list(map(max, [1, 7, 2, 8], [5, 6, 3, 0]))
prt2 = [ max(x) for x in zip([1, 7, 2, 8], [5, 6, 3, 0])] 
print(prt1)
print(prt2)