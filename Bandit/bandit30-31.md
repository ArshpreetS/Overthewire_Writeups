# Solution

After cloning the repo. 

The message we got!

```
bandit30@bandit:/tmp/pass_bandit30$ cat README.md 
just an epmty file... muahaha
```
There wasn't anything in the branches or commits. Lets check the tags 

``` 
bandit30@bandit:/tmp/pass_bandit30$ git tag -l
secret
```

Ohh! There is tag by the name secret. This must be our password!

Use *git show command* to get the contents of that tag

```
bandit30@bandit:/tmp/pass_bandit30$ git show secret
47e603bb428404d265f59c42920d81e5
```

password: `47e603bb428404d265f59c42920d81e5`

