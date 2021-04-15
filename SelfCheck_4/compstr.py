str1 = input('Enter a string: ')
str2 = input('Enter another string: ')
lenof1, lenof2 = len(str1), len(str2)
if lenof1 < lenof2:
   print(f'''Shorter string: {str1} (len: {lenof1})
Longer string: {str2} (len: {lenof2})''')
elif lenof1 > lenof2:
   print(f'''Shorter string: {str2} (len: {lenof2})
Longer string: {str1} (len: {lenof1})''')
else:
   print(f'''First string: {str1} (len: {lenof1})
Second string: {str2} (len: {lenof2})''')