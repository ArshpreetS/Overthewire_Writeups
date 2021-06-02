# Solution

(I had to see the solution for it, I had no clue of what to do in it)

first: `cat /etc/passwd`

It will show: `bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext`

showtext??

`cat /usr/bin/showtext`

```
bandit26@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```
So, it basically *more* a text file in the home directory of bandit26 and exits. Simple enough?
The trick lies in the more command.

What we need to do is to trigger more to go into its command view so that the program doesn’t just exit.

*We can enter into the vim by pressing **v***

Now, vim has certain commands which we can use, one of them is to open another file. 

`:e /etc/bandit_pass/bandit26` --> will give us the password.

But just getting the password won't help you since it will log us off after sshing in.

## to get the shell

Set the shell to /bin/bash
	`:set shell=/bin/bash`
	`:shell`

This will give you the shell! 
password: `5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z`