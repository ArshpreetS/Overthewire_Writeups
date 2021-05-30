# Solution

You can find stuff about crontabs in the Headquarters repository (linux folder)

After checking the cron.d folder, I found a file cronjob_bandit22

```
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```
It can be clearly seen that the password for bandit22 is stored in a file in the tmp directory. Just `cat` that file to get the password

password: `Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI`
