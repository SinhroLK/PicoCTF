<h2> Problem Statement </h2>
Can you crack the password to get the flag?
Download the password checker <a href='https://artifacts.picoctf.net/c/16/level2.py'>here</a> and you'll need the encrypted <a href = 'https://artifacts.picoctf.net/c/16/level2.flag.txt.enc'>flag</a> in the same directory too.
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills

<h2> Hints </h2>
<ol>
<li>Does that encoding look familiar?</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
Using nano I looked at the code of level2.py and there I found that the password was written in ascii encoding. I copied the password into python and printed it, which gave me the password in plain text. Using that password I got the flag
<h2> Flag </h2>
picoCTF{tr45h_51ng1ng_489dea9a}
