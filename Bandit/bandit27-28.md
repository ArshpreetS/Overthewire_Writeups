# Solution

Mistake: 
	* I was cloning the repository in the home directory where I have no permission to create a file or folder*

Go to the /tmp/ directory:
```
bandit27@bandit:/tmp$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo passwd_dede
Cloning into 'passwd_dede'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
```

Mistake: 
	We have to give a name because there already exists a folder by the name of repo

password: `0ef186ac70e04ea33b4c1853d2526fa2`