import sys   # enable to use sys.argv
numberOfArgs = len(sys.argv)

if numberOfArgs < 2:
    sys.stderr.write('Usage: %s inputFile\n' % sys.argv[0])   #[0] current executed file
    sys.exit(1)

num = 0   # line number
for File in sys.argv[1:]:   # access files from parameters
    try:
        fh = open(File, 'r')   # open file to file handler 'fh'
    except:
        sys.stderr.write('cannot open input file %s\n' % File)   # error: cannot open this file
        sys.exit(2)
    for line in fh.readlines():   # put current line into 'line', then read next line repeatly
        print(f'{num} {line}', end = '')
        num += 1
    fh.close()