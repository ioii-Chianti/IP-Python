fh = open('file.txt')
for line in filter(lambda ln : ln != '\n', fh.readlines()):
    print(line, end = '')
fh.close()