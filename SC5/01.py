# default input type is string
sentence = input('Enter a sentence: ')
prohibit = input('Enter a prohibited list: ')

# list comprehension
# string is iterable (can be traversed by for loop)
print(f'{[i for i in sentence if i not in prohibit]}')