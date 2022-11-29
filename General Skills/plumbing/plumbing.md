<h2> Problem Statement </h2>
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 4427.
<h2> Information </h2>
Points value: 200 points<br>
Category: General skills
<h2> Hints </h2>
<ol>
<li>Remember the flag format is picoCTF{XXXX}</li>
<li>What's a pipe? No not that kind of pipe... This <a href ='http://www.linfo.org/pipes.html'>kind</a></li>
</ol>
<h2> Solution </h2>
After using the command given in the problem statement I got a really long pile of strings. I guess the flag is somwhere there, but there is no way I am going through all that. Instead I used a pipe which lets me output one command into some other command. I wrote nc jupiter.challenges.picoctf.org 4427 | grep "picoCTF" which searched for picoCTF in that pile of text. And lo and behold, I found it.
<h2> Flag </h2>
picoCTF{digital_plumb3r_5ea1fbd7}