<h2> Problem Statement </h2>
Can you invoke help flags for a tool or binary? <a href="https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm">This program</a> has extraordinarily helpful information...

<h2> Information </h2>
Points value: 10 points
Category: General skills
<h2> Hints </h2>
1. This program will only work in the webshell or another Linux computer. <br>
2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget <a href="https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm">https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm </a><br>
3. Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm<br>
4. -h and --help are the most common arguments to give to programs to get more information from them!<br>
5. Not every program implements help features like -h and --help.<br>
<h2> Solution </h2>
First i downloaded the program using wget in the webshell provided on picoCTF. After that I gave it permission to run using chmod +x. When I ran warm, it suggested I try
using -h for help. After using ./warm -h, the program gave me the flag.
<h2> Flag </h2>
picoCTF{b1scu1ts_4nd_gr4vy_d6969390}

