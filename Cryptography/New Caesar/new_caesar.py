import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
encrypted_flag = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
#assert all([k in ALPHABET for k in key])
#assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)

def b16_decode(plain):
    dec = ""

    for i in range(0, len(plain), 2):
        i1 = ALPHABET.index(plain[i])
        i2 = ALPHABET.index(plain[i+1])
        b1 = bin(i1)[2:].zfill(4)
        b2 = bin(i2)[2:].zfill(4)
        b = b1 + b2
        d = int(b, 2)
    
        dec += chr(d)
    return dec

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % 16]

for key in ALPHABET:
    dec = ""
    for i, c in enumerate(encrypted_flag):
        dec += unshift(c, key)
    print(b16_decode(dec))
