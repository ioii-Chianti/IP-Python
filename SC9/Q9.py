import operator
# 用 map 把後面的參數放進 lambda 的參數列
L0 = list(map(lambda x, y: x + y, [1, 7, 2, 8], [5, 6, 3, 0]))
L1 = list(map(operator.add, [1, 7, 2, 8], [5, 6, 3, 0]))

from operator import add
# 使用普通函數不用括號，函數指標的觀念
L2 = list(map(add, [1, 7, 2, 8], [5, 6, 3, 0]))
print(f'{L0}, {L1}, {L2}')