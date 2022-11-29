<h2> Problem Statement </h2>
Can you crack the password to get the flag?
Download the password checker <a href = 'https://artifacts.picoctf.net/c/81/level5.py'>here</a> and you'll need the encrypted <a href = 'https://artifacts.picoctf.net/c/81/level5.flag.txt.enc'>flag</a> and the <a href = 'https://artifacts.picoctf.net/c/81/level5.hash.bin'>hash</a> in the same directory too. Here's a <a href = 'https://artifacts.picoctf.net/c/81/dictionary.txt'>dictionary</a> with all possible passwords based on the password conventions we've seen so far.
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills
<h2> Hints </h2>
<ol>
<li>Opening a file in Python is crucial to using the provided dictionary.</li>
<li>You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
Similar solution to the previous two challs. Here you need to open the dictionary and extract passwords from it. After that you iterate over the extracted passwords and let the script check which is the right one.
<h2> Flag </h2>
picoCTF{h45h_sl1ng1ng_fffcda23}
