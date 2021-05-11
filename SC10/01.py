class Polynomial:
    def __init__(self, *coeff):
        self.coeff = coeff
    def evaluate(self, xvalue):
        Sum = 0
        for pow, coef in enumerate(self.coeff):
            Sum += coef * (xvalue ** pow)
        return Sum
    __call__ = evaluate   # 呼叫物件和參數 等於 直接呼叫這個函數

fx = Polynomial(1, 2, 3, 4)
print(fx(2))