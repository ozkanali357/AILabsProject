# This file aims to generate public and private keys for RSA encryption with functions.

from math import gcd
from .PrimeGen import dobigprime # We use the large prime numbers generated by PrimeGen.py.

def genkeys(bits=1024): # The integer bits is 1024 which is the default key size for the key generation done with prime numbers.
    p = dobigprime(bits) # Two large prime numbers are generated.
    q = dobigprime(bits)
    n = p * q # n is the modulus for the public and private keys. The security of the RSA algorithm depends on the fact that it is difficult to factorize the modulus n to its components p and q.
    phi = (p - 1) * (q - 1) # phi is Euler's totient function (the totient of n). It symbolises the number of integers up to n that are coprime (two numbers having only 1 as their common factor) with n. 
    # The totient function is used to calculate the public and private exponents. Therefore, it mathematically links the encryption and decryption processes.
    
    # e should be 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # e is the public exponent. 65537 is a common choice for e, because it is a prime number and it has properties that make the encryption faster.
    while gcd(e, phi) != 1: # The while loop is there to make sure that e is coprime with phi. If not, it increases the value of e by 2 (to make it stay odd) until it is coprime with phi.
        e += 2
    
    # d is the private exponent. We compute it as the modular multiplicate inverse of e modulo phi. (d * e) % phi = 1
    d = pow(e, -1, phi) # The pow function with three arguments computes this accurately.
    
    pubkey = (e, n)
    privkey = (d, n)
    return pubkey, privkey # It returns a tuple having the public key and the private key.