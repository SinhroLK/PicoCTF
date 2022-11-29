<h2> Problem Statement </h2>
Our flag printing service has started glitching!
$ nc saturn.picoctf.net 65353

<h2> Information </h2>
Points value: 100 points<br>
Category: General skills

<h2> Hints </h2>
<ol>
<li>ASCII is one of the most common encodings used in programming</li>
<li>We know that the glitch output is valid Python, somehow!</li>
<li>Press Ctrl and c on your keyboard to close your connection and return to the command prompt.</li>
</ol>
<h2> Solution </h2>
After running the command given in the problem statement the output I got was 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'. This output had the format which python accepts for ascii characters, so I just used print in python to get the flag.
<h2> Flag </h2>
picoCTF{gl17ch_m3_n07_9c42a45d}
