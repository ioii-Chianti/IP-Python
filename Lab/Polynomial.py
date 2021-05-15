class Polynomial:
    def __init__(self, *coeff):
        self.coeff = list(coeff)

    def evaluate(self, xvalue):
        Sum = 0
        for pow, coe in enumerate(self.coeff):
            PowerX = 1
            for i in range(pow):
                PowerX *= xvalue
            Sum += coe * PowerX
        return Sum

    def change_coefficient(self, i, coeff):
        self.coeff[i] = coeff

 # MUST add the 6 lines below
instantiate_statement = input()
exec(instantiate_statement)
change_coeff_call = input()
exec(change_coeff_call)
print_evaluate = input()
exec(print_evaluate)

# f = Polynomial(3, 5, 4, 7, 1)
# f.change_coefficient(0, 10)
# print(f.evaluate(3))