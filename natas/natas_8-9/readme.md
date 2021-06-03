# Solution

![image](./capture.jpg)

So we have the encrypted message and we know how it was encrypted.
If we go in the reverse direction and decrypt it then we will get the secret key and hence get the password:

Steps:
1. hex to ascii
2. reverse the string
3. base64 decode

Did it in the script.py

password: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`