password = input()
bias = int(input())
origin = []

for ch in password:
    ch = ord(ch) - bias
    if ch < ord('A'):
        ch += 26
    ch = chr(ch)
    origin.append(ch)

print(''.join(origin))