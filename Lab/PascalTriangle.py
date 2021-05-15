def pascal(row, col):
    if col == 0 or row == col:
        return 1
    elif 0 < col < row:
        return pascal(row - 1, col - 1) + pascal(row - 1, col)

def print_pascal(n):
    for i in range(n):
        for j in range(i + 1):
            print(f'{pascal(i, j):3d}', end = '')
        print()

# N = int(input())
# print_pascal(N)
exec(input()) # MUST add this line