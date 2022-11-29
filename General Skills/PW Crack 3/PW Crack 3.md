<h2> Problem Statement </h2>
Can you crack the password to get the flag?
Download the password checker <a href = 'https://artifacts.picoctf.net/c/25/level3.py'>here</a> and you'll need the encrypted <a href = 'https://artifacts.picoctf.net/c/25/level3.flag.txt.enc'>flag</a> and the <a href = 'https://artifacts.picoctf.net/c/25/level3.hash.bin'>hash</a> in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills

<h2> Hints </h2>
<ol>
<li>To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin</li>
<li>To exit bvi type :q and press enter.</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
Using nano I looked at the python script. Since all the passwords are stored as a list inside the script, I iterated over the list, making the script try every password from the script. One of the passwords gave me the flag.
<h2> Flag </h2>
picoCTF{m45h_fl1ng1ng_6f98a49f}
