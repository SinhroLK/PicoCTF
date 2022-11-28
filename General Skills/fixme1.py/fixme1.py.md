<h2> Problem Statement </h2>
Fix the syntax error in this Python script to print the flag.
<a href = 'https://artifacts.picoctf.net/c/37/fixme1.py'>Download Python script</a>
<h2> Information </h2>
Points value: 100 points<br>
Category: General Skills
<h2> Hints </h2>
<ol>
<li>Indentation is very meaningful in Python</li>
<li>To view the file in the webshell, do: $ nano fixme1.py</li>
<li>To exit nano, press Ctrl and x and follow the on-screen prompts.</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
After downloading the file I tried running it, but i gave a syntax error. I used nano fixme1.py to look at the code and saw that the last line was not indeted proprerly. After fixing the indentation and running the script, I got the flag.
<h2> Flag </h2>
picoCTF{1nd3nt1ty_cr1515_6a476c8f}
