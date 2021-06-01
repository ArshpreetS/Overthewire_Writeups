# Solution

To brute force the pin, we had to create the wordlist using the following script

```
#!/bin/bash

declare p
p="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in {1..9999}
do
   echo $p $i >> wordlist.txt
done

```
this will create a *wordlist.txt* file. To brute force with that file, use the following command:
`cat wordlist.txt | nc localhost 30002`

password: `uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG`