'''
This file aims to generate public and private keys for RSA encryption and decryption.
'''

import sys
import os
from math import gcd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.primegen import dobigprime

def genkeys(bits=1024):
    """
    The integer bits is 1024 which is the default key size.
    This function generates the public and private keys for RSA encryption and decryption.
    It returns a tuple having the public key, the private key, the primes p and q.
    """
    e = 65537
    difference = 2**(bits // 2 - 100)

    while True:
        p = dobigprime(bits)
        q = dobigprime(bits)
        if p == q or abs(p - q) < difference:
            continue

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            e = 3
            while gcd(e, phi) != 1:
                e += 2
        try:
            d = pow(e, -1, phi)
        except ValueError:
            continue

        break

    pubkey = (e, n)
    privkey = (d, n)
    return pubkey, privkey, p, q
