<h2> Problem Statement </h2>
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 22342, but it doesn't speak English...

<h2> Information </h2>
Points value: 15 points
Category: General skills

<h2> Hints </h2>
1. You can practice using netcat with this picoGym problem: <a href ="https://play.picoctf.org/practice/challenge/34">what's a netcat?</a> <br>
2. You can practice reading and writing ASCII with this picoGym problem: <a href ="https://play.picoctf.org/practice/challenge/22">Let's Warm Up</a><br>
<h2> Solution </h2>
Problem statement gave me a command which I ran in webshell and it game methe following string of numbers:
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
53 
102 
98 
53 
101 
53 
49 
100 
125 
10 
After running the numbers through an ASCII to text converter I got the flag.
<h2> Flag </h2>
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}

