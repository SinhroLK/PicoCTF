<h2> Problem Statement </h2>
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 29956.
<h2> Information </h2>
Points value: 200 points<br>
Category: General skills
<h2> Hints </h2>
<ol>
<li>I hear python can convert things.</li>
<li>It might help to have multiple windows open.</li>
</ol>
<h2> Solution </h2>
After connecting using the command given it said:"Please give the 01101100 01101001 01101101 01100101 as a word.
...
you have 45 seconds....." which made me panic a bit so I just used an online converte binary to text which gave me the word 'lime'. After that I had been given another task saying:"Please give me the  143 157 156 164 141 151 156 145 162 as a word." For that one I also used an online converter, just time time from octal to text, since it gad no digits larger than 7. It gave me the word 'container'. The third and last task was:"Please give me the 6368616972 as a word." which could have been either decimal or hex. I went with hex since it is widely used in computer science and I was right. 636816972 is chair in hex. After that I got the flag.
<h2> Flag </h2>
picoCTF{learning_about_converting_values_b375bb16}