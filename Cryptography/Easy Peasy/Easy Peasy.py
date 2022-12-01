from pwn import *
#print('a' * (50000 - 32))
#print('a' * 32)
ef = bytes.fromhex('51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57')
pa = b'a'*32
ea = bytes.fromhex('3d1958023d1958563d190002523d1907033d1951503d1905023d1950033d1950')
key = xor(ea,pa)
print(xor(ef,key).decode())
