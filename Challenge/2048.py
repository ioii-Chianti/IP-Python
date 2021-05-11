import sys
import numpy
import random

def initialize():
    ret = numpy.zeros((4, 4), dtype = int)
    while True:
        s, t, x, y = random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)
        if s != x or t != y:
            break
    ret[s, t] = ret[x, y] = 2
    return ret

def rotate(Grid):
    newGrid = numpy.zeros((4, 4), dtype = int)
    for i in range(4):
        for j in range(4):
            newGrid[j, 3 - i] = Grid[i, j]
    for i in range(4):
        Grid[i] = newGrid[i]

def combine(Grid):
    

# 格子、移動步數: 有指令且有變動才算)、分數: 有合併
Grid, Step, Score = initialize(), 0, 0
dic = {'up': 0, 'down': 2, 'left': 1, 'right': 3}

direction = input('up / down / left / right: ')
for i in range(dic[direction]):
    rotate(Grid)
combine(Grid)