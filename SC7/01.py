import sys

try:
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    quo = A / B
except ValueError:
    quo = -1.
    sys.stderr.write("There is an exception. It's ValueError.\n")
except ZeroDivisionError:
    quo = -1.
    sys.stderr.write("There is an exception. It's ZeroDivisionError.\n")
finally:
    print(f'quo = {quo:.6f}')