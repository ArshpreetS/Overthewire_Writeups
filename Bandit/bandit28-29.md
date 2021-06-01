# Solution

So First, we have to repeat the same process of getting the git clone

```
1. cd /tmp
2. git clone <link> lend_me_pass
3. cd lend_me_pass
```

But the contents in README.md is:

```
bandit28@bandit:/tmp/lend_me_pass$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```
hmm? this is odd, the password is hidden. Though, since this was done in git repository maybe there is something in the commits

## TO see the commit logs

`git log`

```
bandit28@bandit:/tmp/lend_me_pass$ git log
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

commit c086d11a00c0648d095d04c089786efef5e01264
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    add missing data

commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    initial commit of README.md
```

lets check the last commit

## To see the detailed info of the commit

`git show <commit id>` (if commit id is blank then it will show the last commit)

```
bandit28@bandit:/tmp/lend_me_pass$ git show
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

diff --git a/README.md b/README.md
index 3f7cee8..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: bbc96594b4e001778eee9975372716b2
+- password: xxxxxxxxxx
```

There we go!

password: `bbc96594b4e001778eee9975372716b2`