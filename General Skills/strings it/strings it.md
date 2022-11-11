<h2> Problem Statement </h2>
Can you find the flag in <a href="https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings">file</a> without running it?
<h2> Information </h2>
Points value: 100 points
Category: General skills
<h2> Hints </h2>
1. <a href="https://linux.die.net/man/1/strings"> strings </a>
<h2> Solution </h2>
First I downloaded the file using wget. Then i used strings strings but the command gave a lot of plain text and there was no way I got through all that. After searching a bit I found that we can use grep to find specific words. Since we know that the flag always has picoCTF in it, we can use strings strings | grep picoCTF to find the flag. 
<h2> Flag </h2>
picoCTF{5tRIng5_1T_7f766a23}
