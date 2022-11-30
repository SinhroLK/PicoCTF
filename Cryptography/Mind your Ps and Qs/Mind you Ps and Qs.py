from factordb.factordb import FactorDB
from Crypto.Util.number import inverse, long_to_bytes

c=843044897663847841476319711639772861390329326681532977209935413827620909782846667 
n=1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e = 65537
f = FactorDB(n)
f.connect()
p = f.get_factor_list()[0]
q = f.get_factor_list()[1]
phi = (p-1) * (q-1)
d = inverse(e,phi)
x = pow(c,d,n)
print(long_to_bytes(x).decode())