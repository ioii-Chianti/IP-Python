sentence = list(input('Enter a sentence: '))
prohibit = input('Enter a prohibited list: ')
print(f'{[i for i in sentence if i not in prohibit]}')