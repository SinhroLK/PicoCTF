<h2> Problem Statement </h2>
The <a href ='https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png'>numbers</a>... what do they mean?
<h2> Information </h2>
Points value: 50 points<br>
Category: Cryptography
<h2> Hints </h2>
<ol>
<li>The flag is in the format PICOCTF{}</li>
</ol>
<h2> Solution </h2>
In the image you can see a lot of numbers. You can see {} which means it is safe to assume that those numbers represent the ecrypted flag. Since we know that the flag is in the picoCTF{} format, and we see that the third number is 3, it is not hard to conclude that these numbers are just places of letters in the alphabet. Now, you can manually translate the cipher, but I wrote a script to do that for me. The reason I add +96 to the number value is because ascii characters are 96 places ahead of the alphabet because of other characters. When you translate the picture you get the flag.
<h2> Flag </h2>
picoctf{thenumbersmason}

