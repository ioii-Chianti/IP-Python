def withNewTax(price, rate=input('enter a rate: ')):
    return price * (1 + float(rate))

def withNewerTax(price, rates=[0.01, 0.02, 0.03]):
    ans = price * (1 + rates[-1])
    rates.pop()
    return ans

price = 1
def withNewestTax(price, rate=price):
    return price * (1 + rate)
    
print(withNewTax(10))
print(withNewTax(10))
print(withNewTax(10))
print(withNewerTax(10))
print(withNewerTax(10))
print(withNewerTax(10))
print(withNewestTax(10))
print(withNewestTax(10))
print(withNewestTax(10))