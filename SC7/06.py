import sys
while True:
    expr = input('Enter an expression: ')
    if expr == 'quit':
        print('Goodbye!')
        sys.exit(0)

    expr = expr.split()
    try:
        x = int(expr[0])   # ValueError may occur
        y = int(expr[2])   # ValueError may occur
        op = expr[1]
        assert op in '+-*/'   # AssertionError may occur
    except (ValueError, IndexError, AssertionError):
        sys.stderr.write('Error: Invalid expression\n')
    else:
        try:
            if op == '+':
                print(f'Answer: {x + y}')
            elif op == '-':
                print(f'Answer: {x - y}')
            elif op == '*':
                print(f'Answer: {x * y}')
            elif op == '/':
                print(f'Answer: {x / y:.2f}')
        except ZeroDivisionError:
            sys.stderr.write('Error: Cannot divide by 0\n')