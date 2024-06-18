# Paranoia

> <p>im baby</p>
> <p><a href="attachments/chall"></a>chall</p>

## Path to Flag

I decompiled the program and here's the main function

```
undefined8 main(void)

{
  char cVar1;
  int iVar2;
  time_t tVar3;
  ulong local_20;
  
  tVar3 = time((time_t *)0x0);
  srand((uint)tVar3);
  for (local_20 = 0; local_20 < 0x12; local_20 = local_20 + 1) {
    cVar1 = flag[local_20];
    iVar2 = rand();
    printf("%i ",(ulong)(uint)(iVar2 % 0x100 ^ (int)cVar1));
  }
  putchar(10);
  return 0;
}
```

The main function is sort of a XOR encryption algorithm. First, it gets the current time and use it to seed the random number generator. It then enters a loop that runs 18 times; in each iteration of the loop, the program retrieve each character of the flag, generate a random number, perform a XOR operation on the ASCII value of the flag and the random number. Lastly, it prints out the result.

Hence, we can simply reverse the algorithm.

```
#!/usr/bin/env python3

from pwn import *
import time

from ctypes import CDLL
from ctypes.util import find_library

import string

libc = CDLL(find_library("c"))

time = libc.time(0) - 80000

io = remote("20.80.240.190", 1234)
enc_flag = [int(x) for x in io.recvline().decode("utf-8").strip().split(" ")]

while (True):
    out = ""
    libc.srand(time)
    time += 1
    for c in enc_flag:
        dec_char = chr(c ^ (libc.rand() % 0x100))

        if dec_char not in string.printable:
            break
        else:
            out += dec_char
    else:
        print(out)
        break
```

`akasec{n0t_t00_m4ny_br41nc3lls_l3ft}`