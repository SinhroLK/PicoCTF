<h2> Problem Statement </h2>
Can you crack the password to get the flag?
Download the password checker <a href = 'https://artifacts.picoctf.net/c/53/level1.py'>here</a> and you'll need the encrypted <a href='https://artifacts.picoctf.net/c/53/level1.flag.txt.enc'>flag</a>in the same directory too.
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills
<h2> Hints </h2>
<ol>
<li>To view the file in the webshell, do: $ nano level1.py</li>
<li>To exit nano, press Ctrl and x and follow the on-screen prompts.</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
Using python level1.py I ran the python passwork checker. It asked for my password. I ran nano level1.py and in the code saw that the correct password is 8713. I again ran the script, typed in the password and got the flag.
<h2> Flag </h2>
picoCTF{545h_r1ng1ng_1b2fd683}
