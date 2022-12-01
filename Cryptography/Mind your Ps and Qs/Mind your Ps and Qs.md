<h2> Problem Statement </h2>
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? <a href = 'https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values'>values</a>.
<h2> Information </h2>
Points value: 20 points<br>
Category: Cryptography
<h2> Hints </h2>
<ol>
<li>Bits are expensive, I used only a little bit over 100 to save money</li>
</ol>
<h2> Solution </h2>
c - ciphertext
n - result of multiplying two large prime numbers p and q
e - multiplicative inverse of a private exponent d mod phi
phi = (p-1) * (q-1) [Euler function]
d = e^(-1) mod phi
c = x^e mod n
x = c^d mod n
Factordb is used for solving this problem. I wrote a short python script that solves the problem for me, without me needing to use the factordb database online. After I got the factors I use them to calculate other values I need to calculate x(flag) from the system above. 
<h2> Flag </h2>
picoCTF{sma11_N_n0_g0od_00264570}
