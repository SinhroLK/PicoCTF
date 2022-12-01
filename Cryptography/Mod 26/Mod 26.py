import codecs
string = input()
decoded = codecs.decode(string, 'rot_13')
print(decoded)