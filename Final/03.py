class Polynomial:
    def __init__(self, *coeff):
        self._coeff = list(coeff)

    def evaluate(self, xvalue):
        Sum = 0
        for pow, coeff in enumerate(self._coeff):
            Sum += coeff * (xvalue ** pow)
        return Sum

    def change_coeff(self, i, coeff):
        self._coeff[i] = coeff

# f = Polynomial(3, 5, 4, 7, 1)
# f.change_coeff(0, 10)
# print(f.evaluate(3))

instantiate_statement = input()
exec(instantiate_statement)
change_coeff_call = input()
exec(change_coeff_call)
print_evaluate = input()
exec(print_evaluate)