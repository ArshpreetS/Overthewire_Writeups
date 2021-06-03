# Solution

![image](./capture1)

So this is what is given to us. It looks like a password thing, like if I will provide the right key they will give me the password for the next level. After trying some pity attempts. I decided to go to the *View Source*

![image](./capture2)

Cool, so there is some php! This is a simple program to check the authentication of the key I provide.

But We can see from the script that they have included a file and maybe we can access that file. 

Thats odd, there is sure a file *includes/secret.inc* but it is blank. Lets check the source.

![image](./capture3)

Found the key!

password: `7z3hEENjQtflzgnT29q7wAvMNfZdh0i9`