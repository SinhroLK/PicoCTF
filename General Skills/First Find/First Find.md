<h2> Problem Statement </h2>
Unzip this archive and find the file named 'uber-secret.txt'
<a href = 'https://artifacts.picoctf.net/c/550/files.zip'>Download zip file</a>
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills

<h2> Hints </h2>
None
<h2> Solution </h2>
I unzipped the .zip file using unzip files.zip. After it unzipped I entered the files folder usind cd files. While there I used the find command to find the uber-secret.txt. The exact command is find -name uber-secret.txt. As an output I got the path to the text file. After using the cd command once more, this time with the path to the file, I got in the right directory. There I used cat uber-secret.txt to see its content, and got the flag.
<h2> Flag </h2>
picoCTF{f1nd_15_f457_ab443fd1}