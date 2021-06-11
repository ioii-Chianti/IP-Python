import sys
from random import *

class Grid:
    def __init__(self):
        ''' Constructor: init board and new 2 '''
        self.board = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
        self.shifted = [False, 0]    # [0] shifted ot not [1] score in this round
        self.Max = 2
        self.randNew(0)
        self.randNew(0)

    def randNew(self, mode=1):
        ''' Find valid position to new a num from (2, 4, 8) randomly
            Parameter: [int] mode: decide whether it's init or not '''
        while True:
            r, c = randint(0, 3), randint(0, 3)
            if not self.board[r][c]:
                # if mode is 0 then just init 2
                self.board[r][c] = sample([2, 4], k=1, counts=[8, 1])[0] if mode else 2
                break            # sample returns a list
    
    def rotate(self):
        ''' Counterclockwise rotation'''
        self.board = list(map(list, zip(*self.board)))[::-1]

    def collapse(self):
        ''' Merge numbers based on the rule
            Return: [bool] updated or not '''
        # Fix: the index of block which is already merged and can't be merged again in this round
        Fix, self.shifted = [-1, -1, -1, -1], [False, 0]

        def merge(r, c):
            if self.board[r][c]:    # not sero
                # previous block is zero
                if self.board[r][c-1] == 0:
                    # move to previous block
                    self.board[r][c-1], self.board[r][c] = self.board[r][c], 0
                    if c > 1:
                        merge(r, c - 1)     # check pervious blocks recursively 
                    self.shifted[0] = True
                # previous block is the same as current, and meet the rules
                elif self.board[r][c-1] == self.board[r][c] and Fix[r] < c - 1:
                    # sum up with previous block
                    self.board[r][c-1], self.board[r][c] = self.board[r][c-1] + self.board[r][c], 0
                    # set flag and update score
                    self.shifted = [True, self.shifted[1] + self.board[r][c-1]]
                    self.Max = max(self.Max, self.board[r][c-1])
                    Fix[r] = c - 1   # important !!!

        for row in range(4):
            for col in range(1, 4):
                merge(row, col)
        return self.shifted[0]   # return updated or not
        

class Game:
    def __init__(self, target):
        ''' Constructor: init target value and new Grid object '''
        self.Target = target
        self.GridObj = Grid()

    def Swipe(self, direction):
        ''' Process of a swiping:
            1. Rotate matrix and change to left swiping
            2. Collapse and see whether the board changed or not
            3. Rotate back to right direction  '''

        # times needed for roatation
        times = {'up': 1, 'down': 3, 'left': 0, 'right': 2, 'W': 1, 'S': 3, 'A': 0, 'D': 2}
        time = times[direction]

        # 1
        while time:
            self.GridObj.rotate()
            time -= 1
        # 2
        updated = self.GridObj.collapse()
        # 3
        time = 4 - times[direction]
        while time:
            self.GridObj.rotate()
            time -= 1
            
        if updated:
            self.GridObj.randNew()
            print(f'shifted, {self.GridObj.shifted[1]} points')
        else:
            print(f'not shifted, 0 points')
    
    def View(self):
        ''' Print out the board '''
        for row in self.GridObj.board:
            for val in row:
                print(f'{val:>3d}', end = ' ')
            print('\n')
    
    def Finished(self):
        ''' Check if finished 
            Returns [str/bool] return False if not finished, or the result of game '''
        if self.GridObj.Max >= self.Target:
            return 'You Win!'

        cont, mx = False, self.GridObj.board
        for row in range(4):
            for col in range(4):
                val = mx[row][col]
                # still have 0 on the board
                if not val:
                    return False
                # Check neighbors
                if (row, col) == (3, 3):
                    pass
                elif row == 3:
                    cont = val == mx[row][col + 1]
                elif col == 3:
                    cont = val == mx[row + 1][col]
                else:
                    cont = (val == mx[row][col + 1] or val == mx[row + 1][col])
                # whether to continue playing
                if cont:
                    return False
        return 'You Lose!'

target = int(input("Enter your target value: "))
Game2048 = Game(target)

while True:
    print()
    Game2048.View()
    actions = {'up', 'down', 'left', 'right', 'W', 'A', 'S', 'D'}
    print("Enter up, down, left, right or W, A, S, D")
    try:
        action = input('Command: ')
        assert action in actions, f'# Invalid Command #\n'
    except AssertionError as errmsg:
        sys.stderr.write(str(errmsg))
    else:
        Game2048.Swipe(action)
        if Game2048.Finished():
            print(Game2048.Finished())
            break
