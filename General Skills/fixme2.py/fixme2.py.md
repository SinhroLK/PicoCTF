<h2> Problem Statement </h2>
Fix the syntax error in the Python script to print the flag.
<a href = 'https://artifacts.picoctf.net/c/66/fixme2.py'>Download Python script</a>
<h2> Information </h2>
Points value: 100 points<br>
Category: General Skills
<h2> Hints </h2>
<ol>
<li>Are equality and assignment the same symbol?</li>
<li>To view the file in the webshell, do: $ nano fixme2.py</li>
<li>To exit nano, press Ctrl and x and follow the on-screen prompts.</li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
</ol>
<h2> Solution </h2>
After downloading the python script I tried running it but got a syntax error. Using nano to see the code I noticed that the code near the end of the script had = instead of == in the if statement. After fixing the mistake, I again ran the script and got the flag.
<h2> Flag </h2>
picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}

