number = [16, 9, 3, 15, 3,20, 6, 20, 8,5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
n = []
for num in number:
    n.append(chr(num + 96))
print(''.join(n))
