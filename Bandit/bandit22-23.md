# Solution

```
bandit22@bandit:~$ cd /etc/cron.d
bandit22@bandit:/etc/cron.d$ ls
cronjob_bandit15_root  cronjob_bandit17_root  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  cronjob_bandit25_root
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh 
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
*note: check the md5sum command in headquarters repository(linux folder)*

This shows that the password for the bandit23 is saved in a file named with the variable *mytarget*.
If we are able to figure out the value of mytarget then we will be able to figure out the password.


```
root@chief:/home/chief/Documents/gitrepo/Overthewire_Writeups/Bandit# echo I am user bandit22 | md5sum | cut -d ' ' -f 1
8169b67bd894ddbb4412f91573b38db3
```
`md5sum` --> created a hash
`cut -d ' ' -f 1` --> took space as field diliminator and we took the first column from it.


password: `Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI`