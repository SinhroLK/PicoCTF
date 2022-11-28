<h2> Problem Statement </h2>
Run the Python script and convert the given number from decimal to binary to get the flag.
<a href = 'https://artifacts.picoctf.net/c/32/convertme.py'>Download Python script</a>
<h2> Information </h2>
Points value: 100 points<br>
Category: General skills

<h2> Hints </h2>
<ol>
<li>Look up a decimal to binary number conversion app on the web or use your computer's calculator! </li>
<li>The str_xor function does not need to be reverse engineered for this challenge.</li>
<li>If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.</li>
<li>To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'</li>
<li>Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!</li>
<li>Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 convertme.py</li>
</ol>
<h2> Solution </h2>
To be honest, the hints really solved this one by themselves. I downloaded the python script and ran it. It asked me to translate the number 83 to binary, which I did by hand(you can also write a script or use an online converter). After answering the question, it outputed the flag.
<h2> Flag </h2>
picoCTF{4ll_y0ur_b4535_722f6b39}
