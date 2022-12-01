<h2> Problem Statement </h2>
There's a flag shop selling stuff, can you buy a flag? <a href = 'https://jupiter.challenges.picoctf.org/static/253c4651d852ac6342752ff222cf2a83/store.c'>Source</a>. Connect with nc jupiter.challenges.picoctf.org 9745.
<h2> Information </h2>
Points value:300 points <br>
Category: General skills
<h2> Hints </h2>
<ol>
<li>Two's compliment can do some weird things when numbers get really big!</li>
</ol>
<h2> Solution </h2>
The fake flag costs 900 dollars and it subtracts from out balance. I noticed in the code that total_cost is declared as an int, which means it is an signed integer. Signed integers can't be negative, so techically if we make total_cost "negative enough" we can add the sum to our balance. 
When buying fake flags I said I wante dto buy 4 000 000 flags, and after pressing enter I had a lot of money in my balance. With that money I bought the real flag.
<h2> Flag </h2>
picoCTF{m0n3y_bag5_65d67a74}
