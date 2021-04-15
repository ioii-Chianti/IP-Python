import sys
numberOfArgs = len(sys.argv)
if numberOfArgs < 2:
    sys.stderr.write('Usage: %s inputFile\n' % sys.argv[0])
    sys.exit(1)
num = 0
for File in sys.argv[1:]:
    try:
        fh = open(File, 'r')
    except:
        sys.stderr.write('cannot open input file %s\n' % File)
        sys.exit(2)
    for line in fh.readlines():
        print(f'{num} {line}', end='')
        num += 1
    fh.close()