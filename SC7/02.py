import sys

try:
    fh = open('ExistFile.txt')
except FileNotFoundError:
    sys.stderr.write('There is an exception. It is FileNotFoundError.\n')
else:   # if no error
    print("Hello!\nI'm exist file.")
    fh.close()
finally:
    print("Goodbye!")