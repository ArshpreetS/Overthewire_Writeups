# Solution

This question made my day! 

Well, we just have to play around to figure out the bug in the command and also a bit of bash.. hmpp! xD

![image](./capture.jpg)

The command that is executing is: `grep -i $key $dictionary.txt`
- `-i` is simply removing case sensitive restrictions 
- `dictionary.txt` is a file in the server containing a lot of words
- `grep` is a unix command used to search around

This command is simply searching words(provided by us in $key) in the dictionary.txt

We have to use idk_the_name-injection vulnerability in this command.

We can make this command into: `grep -i   || cat /etc/natas_webpass/natas10 # $dictionary.txt`

This command says, find " " or show the file /etc/natas_webpass/natas10(password) and what comes after `#` acts as a comment

password: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`