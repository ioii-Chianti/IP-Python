import sys

if len(sys.argv) != 4:
    sys.stderr.write(f'Usage: {sys.argv[0]} digit digit inputFile.txt\n')
    sys.exit(0)

errNum = 0   # record the number of errors
try:
    num_a, num_b = int(sys.argv[1]), int(sys.argv[2])
    with open(sys.argv[3]) as fh:
        for i, curLine in enumerate(fh.readlines()):
            for j in range(num_b):
                try:
                    correct = (i + 1) * (j + 1)
                    term = int(curLine.split()[j])   # ValueError may occur due to non-digit char
                    assert term == correct           # check value
                except ValueError:
                    sys.stderr.write(f'{i+1} x {j+1} = {curLine.split()[j]} badly formatted; should be {correct}\n')
                    errNum += 1
                except AssertionError:
                    sys.stderr.write(f'{i+1} x {j+1} = {term} is incorrect; should be {correct}\n')
                    errNum += 1
except ValueError as err:   # about system arguments
    sys.stderr.write(f'ValueError: {str(err)}')
except OSError as err:      # about file open
    sys.stderr.write(f'OSError: {str(err)}')
except Exception as err:
    sys.stderr.write(f'Other Exception: {str(err)}')
else:
    if errNum == 0: 
        print(f'Multiplication table in file {sys.argv[3]} is correct.')
    elif errNum == 1:
        print(f'Multiplication table in file {sys.argv[3]} contains 1 error.')
    else:
        print(f'Multiplication table in file {sys.argv[3]} contains {errNum} errors.')