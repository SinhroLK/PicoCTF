<h2> Problem Statement </h2>
Unzip this archive and find the flag.
<a href = 'https://artifacts.picoctf.net/c/553/big-zip-files.zip'>Download zip file</a>
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills
<h2> Hints </h2>
<ol>
<li>Can grep be instructed to look at every file in a directory and its subdirectories?</li>
</ol>
<h2> Solution </h2>
I unzipped the file I downloaded. After that I used grep -R "picoCTF" in order to see all the files that have picoCTF in them, since that is the format of the flag. Output of that command gave me the flag.   
<h2> Flag </h2>
picoCTF{gr3p_15_m4g1c_ef8790dc}