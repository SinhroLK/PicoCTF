h2> Problem Statement </h2>
Can you look at the data in this binary:<a href="https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/static">static</a>? This <a href="https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/ltdis.sh">BASH script </a> might help!
<h2> Information </h2>
Points value: 20 points
Category: General skills
<h2> Hints </h2>
None
<h2> Solution </h2>
After downloading two files using wget, I tried running the bash script and static file. First I had to use chmod +x on both. After running the static file, I got
a message saying "Oh hai! Wait what? A flag? Yes, it's around here somewhere!", and after running the bash script i got "Attempting disassembly of  ...<br>
objdump: 'a.out': No such file<br>
objdump: section '.text' mentioned in a -j option, but not found in any input file<br>
Disassembly failed!<br>
Usage: ltdis.sh <program-file><br>
Bye!"<br>
One of the ways i got the solution is just using cat static, and then looking for the flag among the noise. <br>
The other way, probably the one intended by the devs, is using ./ltdis.sh static. This command disassebles static file and writes the content is "static.ltdis.strings.txt"
After opening the file with cat static.ltdis.strings.txt you will get the flag.
<h2> Flag </h2>
picoCTF{d15a5m_t34s3r_98d35619}
