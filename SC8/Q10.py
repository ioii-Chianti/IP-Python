def totalTax(rate, *priceTags):
    print(rate)
    print(priceTags)

totalTax(0.05, 10, 20, 23, 18)
totalTax(0.05, *(10, 20, 23, 18))
totalTax(*(0.05, 10, 20, 23, 18))
# 0.05
# (10, 20, 23, 18)
# 星號和 Tuple 抵銷
totalTax(0.05)
# 0.05
# ()
totalTax(0.05, (10, 20, 23, 18))
# 0.05
# ((10, 20, 23, 18),)
totalTax(0.05, 10)
# 0.05
# (10,)