<h2> Problem Statement </h2>
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it,
and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

<h2> Information </h2>
Points value: 30
Category: General skills

<h2> Hints </h2>
1.Finding a cheatsheet for bash would be really helpful!

<h2> Solution </h2>
First I connected to the server with ssh ctf-player@venus.picoctf.net -p 51687 and using the password 481e7b14 (your login info might be different. ssh command is 
found under the description after you launch server instance and the password is given to you in the description). Using ls lists 1of3.flag.txt instructions-to-2of3.txt.
With cat 1of3.flag.txt we get first part of the flag 'picoCTF{xxsh_'. cat instructions-to-2of3.txt says Next, go to the root of all things, more succinctly `/`.
I used cd .. to go back a directory. There was a file called cat 3of3.flag.txt. After using cat cat 3of3.flag.txt it gave 3rd part of the flag '5190b070}'. I kept going 
back with cd .. until I found 2of3.flag.txt. It had the 2nd part of the flag '0ut_0f_\/\/4t3r_'. After combining the 3 parts you get the flag.

<h2> Flag </h2>
picoCTF{xxsh_0ut_0f_//4t3r_5190b070}
