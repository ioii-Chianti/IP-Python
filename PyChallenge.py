from random import *

class Grid:
    def __init__(self):
        self.board = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
        self.newScore = 0
        self.update = False
        self.randomNew()
        self.randomNew()

    def randomNew(self):
        def isValid(r, c):
            if self.board[r][c]:
                return False
            return True

        while True:
            r, c = randint(0, 3), randint(0, 3)
            if isValid(r, c):
                self.board[r][c] = 2
                break
    
    def rotate(self):
        self.board = list(map(list, zip(*self.board)))[::-1]

    def collapse(self):
        Fix, self.newScore, self.update = [-1, -1, -1, -1], 0, False
        def merge(r, c):
            if self.board[r][c]:
                if self.board[r][c-1] == 0:
                    self.board[r][c-1] = self.board[r][c]
                    if c > 1:
                        merge(r, c - 1)
                    self.board[r][c] = 0
                    self.update = True
                elif self.board[r][c-1] == self.board[r][c] and Fix[r] < c - 1:
                    self.board[r][c-1] += self.board[r][c]
                    self.newScore += self.board[r][c-1]
                    self.board[r][c] = 0
                    Fix[r] = c - 1
                    self.update = True

        for row in range(4):
            for col in range(1, 4):
                merge(row, col)
        return self.update
        

class Game:
    def __init__(self, target):
        self.Score = 0
        self.Move = 0
        self.Target = target
        self.GridObj = Grid()
        self.Result = ''

    def Swipe(self, direction):
        times = {'W': 1, 'S': 3, 'A': 0, 'D': 2}
        time = times[direction]
        while time:
            self.GridObj.rotate()
            time -= 1
        needUpdate = self.GridObj.collapse()

        time = 4 - times[direction]
        while time:
            self.GridObj.rotate()
            time -= 1

        if needUpdate:
            self.GridObj.randomNew()
            self.Move += 1
            self.Score += self.GridObj.newScore
        print('shifted, ', end='') if needUpdate else print('not shifted, ', end='')
        print(f'{self.GridObj.newScore} points')
    
    def View(self):
        # 改成呼叫這個物件就 return 容器
        for row in self.GridObj.board:
            for val in row:
                print(f'{val}', end = ' ')
            print()
    
    def Finished(self):
        if self.GridObj.newScore >= self.Target:
            self.Result = 'You Win!'
            return True

        GoOn = False
        for row in range(4):
            for col in range(4):
                val = self.GridObj.board[row][col]
                # still have 0 on the board
                if not val:
                    return False

                # Check all neighbors
                if (row, col) == (0, 0):
                    GoOn = val == self.GridObj.board[row + 1][col] or \
                           val == self.GridObj.board[row][col + 1]
                elif (row, col) == (0, 3):
                    GoOn = val == self.GridObj.board[row + 1][col] or \
                           val == self.GridObj.board[row][col - 1]
                elif (row, col) == (3, 0):
                    GoOn = val == self.GridObj.board[row - 1][col] or \
                           val == self.GridObj.board[row][col + 1]
                elif (row, col) == (3, 3):
                    GoOn = val == self.GridObj.board[row - 1][col] or \
                           val == self.GridObj.board[row][col - 1]
                elif row == 0:
                    GoOn = val == self.GridObj.board[row + 1][col] or \
                           val == self.GridObj.board[row][col - 1] or \
                           val == self.GridObj.board[row][col + 1]
                elif col == 0:
                    GoOn = val == self.GridObj.board[row - 1][col] or \
                           val == self.GridObj.board[row + 1][col] or \
                           val == self.GridObj.board[row][col + 1]
                elif row == 3:
                    GoOn = val == self.GridObj.board[row - 1][col] or \
                           val == self.GridObj.board[row][col - 1] or \
                           val == self.GridObj.board[row][col + 1]
                elif col == 3:
                    GoOn = val == self.GridObj.board[row - 1][col] or \
                           val == self.GridObj.board[row + 1][col] or \
                           val == self.GridObj.board[row][col - 1]
                else:
                    GoOn = val == self.GridObj.board[row - 1][col] or \
                           val == self.GridObj.board[row + 1][col] or \
                           val == self.GridObj.board[row][col - 1] or \
                           val == self.GridObj.board[row][col + 1]
        if (GoOn):
            return False
        self.Result = 'You Lose!'
        return True

target = int(input("Enter your target value: "))
Game2048 = Game(target)

while True:
    print()
    Game2048.View()
    action = input('Up, Down, Left, Right: ')
    Game2048.Swipe(action)
    if Game2048.Finished():
        print(Game2048.Result)
        break