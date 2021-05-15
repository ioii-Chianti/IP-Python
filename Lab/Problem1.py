sentence = input()
prohibit = input()
outList = [i for i in sentence if i not in prohibit]
print('%s', % str(outList))