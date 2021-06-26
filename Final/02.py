def pascal(row, col):
    if col == 0 or row == col:
        return 1
    elif 0 < col < row:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)

def print_pascal(n):
    for r in range(n):
        for c in range(r + 1):
            print(f'{pascal(r, c):3d}', end='')
        print()

function_call = input()
exec(function_call)
# print_pascal(7)