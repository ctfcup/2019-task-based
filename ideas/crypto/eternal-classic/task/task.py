#!/usr/bin/env python3

import re

from Crypto.Cipher import XOR


def read_file(filename):
    with open(filename, 'rb') as file:
        return file.read().strip()


def encrypt(plaintext, key):
    cipher = XOR.new(key)
    return cipher.encrypt(plaintext)


def strip_format(flag):
    match = re.match(rb'^Cup\{(\w+)\}$', flag)
    return match.group(1)


def main():
    key = read_file('key.txt')
    flag = read_file('flag.txt')
    plaintext = strip_format(flag)
    ciphertext = encrypt(2 * plaintext, key)
    print(ciphertext.hex())


if __name__ == '__main__':
    main()
