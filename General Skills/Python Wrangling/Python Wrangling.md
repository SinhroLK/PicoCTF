<h2> Problem Statement </h2>
Python scripts are invoked kind of like programs in the Terminal... Can you run <a href="https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py">this Python script</a> using <a href = "https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/pw.txt"> this password</a> to get <a href = "https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/flag.txt.en">the flag</a>?

<h2> Information </h2>
Points value: 10 points
Category: General Skills

<h2> Hints </h2>
1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py
2. $ man python

<h2> Solution </h2>
I wanted to run the python script in VSCode but it didn't work. Then I tried working in the linux webshell you get see on the picoCTF site. There I downloaded all 3 files using $ wget + link. I tried to run the python script there, but it said permission denied. I used chmod +x ende.py to get permission for executing the file. After that, I used $ python ./ende.py -d flag.txt.en to decrypt the flag file. It wanted a password, which I copied from pw.txt file. 

<h2> Flag </h2>
picoCTF{4p0110_1n_7h3_h0us3_6008014f}

