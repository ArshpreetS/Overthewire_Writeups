# Solution

There is folder *inhere*.
	enter the folder: `cd inhere`

There are around 9 files in the directory
	- by the name -file0(1-9)

Now we are told that the file which contains the password is human readable. There are two ways of tackling this problem
	- Brute force: Open every file till you find the password
	- Use the command: `file ./*`
		This command will tell you something about the content in each file.
		![result](./screenshots/bandit4-5)

Use the command: `cat ./-file08`

password: `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`