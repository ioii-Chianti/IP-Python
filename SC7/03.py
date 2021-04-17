import sys

if len(sys.argv) != 2:
    sys.stderr.write(f'Usage: {sys.argv[0]} inputFile\n')
    sys.exit(1)

try:
    with open(sys.argv[1], 'w') as fh:
        while True:
            text = input('Enter your text or quit: ')
            if text == 'quit':
                break
            fh.write(f'{text}\n')
except OSError as err:
    print(f'Error Msg: {str(err)}')
else:   # if quit w/o errors
    print("File is updated. Enter 'cat filename.txt' to check!")