# Solution

After cloning(refer to the last 2 writeups)

```
bandit29@bandit:/tmp/pass_dedo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

```
Here we go again?! 

So there was nothing in the logs this time. lets check the branches using the `-a` tag (it shows all the used branches too)

```
bandit29@bandit:/tmp/pass_dedo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
```
Lets try the **dev** branch.

```
bandit29@bandit:/tmp/pass_dedo$ git checkout dev
Switched to branch 'dev'
Your branch is up-to-date with 'origin/dev'.
bandit29@bandit:/tmp/pass_dedo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: 5b90576bedb2cc04c86a9e924ce42faf
``` 
There we go!

password: `5b90576bedb2cc04c86a9e924ce42faf`