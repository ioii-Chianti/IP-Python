from random import *

class Grid:
    def __init__(self):
        self.grid = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
        self.Max = 2
        self.randomNew()
        self.randomNew()

    def randomNew(self):
        while True:
            x, y = randint(0, 3), randint(0, 3)
            if self.isValid(x, y):
                self.grid[x][y] = 2
                break
    
    def isValid(self, x, y):
        if self.grid[x][y]:
            return False
        return True

    def rotate(self):
        print('Rot')

    def collapse(self):
        print('colla')


class Game:
    def __init__(self, target):
        self.Score = 0
        self.Move = 0
        self.Target = target
        self.Board = Grid()
        self.Result = ''

    @property
    def Score(self):
        return self.Score
    @property
    def Move(self):
        return self.Move

    def Swipe(self, direction):
        while direction:
            self.Board.rotate()
            direction -= 1
        self.Board.collapse()
    
    def View(self):
        for row in self.Board:
            for val in row:
                print(f'{val} ')
            print()
    
    def Finished(self):
        if self.Board.Max == self.Target:
            self.Result = 'You Win!'
            return True

        for row in self.Board:
            for val in row:
                if not val:
                    return False
        self.Result = 'You Lose!'
        return True


target = input("Enter your target value: ")
Game2048 = Game(target)

while True:
    Game2048.View()
    
    
    if Game2048.Finished():
        print(Game2048.Result)