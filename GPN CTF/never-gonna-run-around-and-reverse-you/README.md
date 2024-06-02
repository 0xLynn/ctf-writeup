# Never gonna run around and reverse you

> <p>I thought of this really cool collision free hash function and hashed the flag with it. Theoretically you shouldn't be able to reverse it...</p>
> <p><a href="attachments/never-gonna-run-around-and-reverse-you.tar.gz">never-gonna-run-around-and-reverse-you.tar.gz</a></p>

## Path to Flag

We are given a hash

`4717591a4e08732410215579264e7e0956320367384171045b28187402316e1a7243300f501946325a6a1f7810643b0a7e21566257083c63043404603f5763563e43`

We are also given an executable that is used to hash the flag, so I used `Ghidra` to check out how the program works

This is the `main` function of the program written in C

```
void processEntry entry(undefined8 param_1,undefined8 param_2)

{
  undefined auStack_8 [8];
  
  __libc_start_main(FUN_001011e9,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

Based on the main function of the program, it calls out the `FUN_001011e9` function.

```
undefined8 FUN_001011e9(int param_1,long param_2)

{
  char *__s;
  size_t sVar1;
  void *pvVar2;
  int local_20;
  
  if (param_1 < 2) {
    printf("Please provide a flag as an argument");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  __s = *(char **)(param_2 + 8);
  sVar1 = strlen(__s);
  pvVar2 = malloc((long)((int)sVar1 + 2));
  strcpy((char *)((long)pvVar2 + 1),__s);
  for (local_20 = 1; local_20 <= (int)sVar1; local_20 = local_20 + 1) {
    *(byte *)((long)pvVar2 + (long)local_20) =
         *(byte *)((long)pvVar2 + (long)local_20) ^ *(byte *)((long)pvVar2 + (long)local_20 + -1);
    printf("%02x",(ulong)(uint)(int)*(char *)((long)pvVar2 + (long)local_20));
  }
  putchar(10);
  return 0;
}
```
This function accepts input and encrypt the string using a progressive XOR algorithm, that means, each byte is XORed with the previous byte, then it prints out the result in hexadecimal format.

Therefore, I used a script to decrypt the hashed flag

```
#!/usr/bin/env python3

def decrypt(enc):
    enc_bytes = bytes.fromhex(enc)
    flag = bytearray(len(enc_bytes))
    flag[0] = enc_bytes[0]

    for i in range(1, len(enc_bytes)):
        flag[i] = enc_bytes[i] ^ enc_bytes[i - 1]

    return flag.decode('utf-8')

enc = "4717591a4e08732410215579264e7e0956320367384171045b28187402316e1a7243300f501946325a6a1f7810643b0a7e21566257083c63043404603f5763563e43"
flag = decrypt(enc)
print("flag:", flag)
```

`GPNCTF{W41t,_h0w_d1d_y0u_s0lv3_th1s?_I_th0ught_1t_w45_4_g00d_h45h}`