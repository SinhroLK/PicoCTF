<h2> Problem Statement </h2>
Can you find the flag in <a href = 'https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file'>file</a>? This would be really tedious to look through manually, something tells me there is a better way.
<h2> Information </h2>
Points value: 100 points
Category: General Skills
<h2> Hints </h2>
1. grep <a href = 'https://ryanstutorials.net/linuxtutorial/grep.php'>tutorial</a>
<h2> Solution </h2>
I downloaded the file using wget. I tried to read the file using cat, but the file output was only random letters, among which was the flag. 
Instead of manually looking through the file, I used egrep 'picoCTF' file to search the file for picoCTF. Using egrep, I got the file.
<h2> Flag </h2>
picoCTF{grep_is_good_to_find_things_5af9d829}