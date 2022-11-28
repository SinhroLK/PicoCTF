<h2> Problem Statement </h2>
Run the Python script code.py in the same directory as codebook.txt.
<ul>
<li><a href = 'https://artifacts.picoctf.net/c/100/code.py'>Download code.py</a></li>
<li><a href = 'https://artifacts.picoctf.net/c/100/codebook.txt'>Download codebook.txt</a></li>
</ul>
<h2> Information </h2>
Points value: 100 points
Category: General Skills
<h2> Hints </h2>
<ol>
<li>On the webshell, use ls to see if both files are in the directory you are in</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
Using wget I downloaded both files. I ran the .py file(python script) by typing python code.py. It ran, and as output I got the flag.
<h2> Flag </h2>
picoCTF{c0d3b00k_455157_d9aa2df2}