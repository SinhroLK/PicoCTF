import hashlib
str2hash = input("Input the string you want hashed: ")
result = hashlib.md5(str2hash.encode())
print(result.hexdigest())