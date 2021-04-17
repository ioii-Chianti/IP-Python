import sys

if len(sys.argv) != 4:
    sys.stderr.write(f'Usage: {sys.argv[0]} num_a num_b inputFile.txt\n')
    sys.exit(0)

try:
    num_a, num_b = int(sys.argv[1]), int(sys.argv[2])
    List = [ (i + 1) * (j + 1) for i in range(num_a) for j  in range(num_b) ]

    # rewrite this file everytime
    with open(str(sys.argv[3]), 'w') as fh:
        for idx, cur in enumerate(List):
            fh.write(str(cur))   # write() should be str format
            fh.write('\n') if (idx % num_b == num_b - 1) else fh.write(' ')
except Exception as err:   # catch all types of exceptions
    sys.stderr.write(f'{str(err)}\n')