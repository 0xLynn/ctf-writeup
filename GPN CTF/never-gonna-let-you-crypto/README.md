# Never gonna let you crypto

> <p>You read the title and thought Blockchain? You were successfully baited. Like the people before you, you now have to solve this challenge.</p>
> <p><a href="attachments/never-gonna-let-you-crypto.tar.gz">never-gonna-let-you-crypto.tar.gz</a></p>

## Path to Flag

We are given an encryption algorithm that uses XOR operation to encrypt a message with a repeating key

```
import os
def encrypt(message,key):
    message = message.encode()
    out = []
    for i in range(len(message)):
        out+= [message[i]^key[i%len(key)]]
    return bytes(out).hex()
FLAG = "GPNCTF{fake_flag}"
key = os.urandom(5)

print(encrypt(FLAG,key))
#d24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d
```

Therefore, I used a script to decode the encrypted flag based on the encryption algorithm.

```
#!/usr/bin/env python3

import binascii

def decrypt(enc, key):
    enc_bytes = bytes.fromhex(enc)
    flag = []
    for i in range(len(enc_bytes)):
        flag += [enc_bytes[i] ^ key[i % len(key)]]
    return bytes(flag).decode()

enc = "d24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d"
prefix = "GPNCTF{"

enc_bytes = bytes.fromhex(enc)
prefix_bytes = prefix.encode()

key = bytes([enc_bytes[i] ^ prefix_bytes[i] for i in range(5)])

flag = decrypt(enc, key)
print("flag:", flag)
```

`GPNCTF{One_T1me_p4ds_m4y_n3v3r_b3_r3u53d!!!}`