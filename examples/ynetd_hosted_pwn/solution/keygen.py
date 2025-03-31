"""
The second portion (key generation) part of Alien Portal.
Player is to deduce the encyption algorithm via static analysis using ghidra/ida, shouldn't be too difficult

"""
import random
import sys
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
            sys.exit(1)
            