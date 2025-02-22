'''
This file aims the generation of large prime numbers for RSA encryption.
The Sieve of Eratosthenes algorithm generates small prime numbers.
The Miller-Rabin probabilistic primality test generates large prime numbers.
'''

import random

def eratosieve(limit):
    '''
    In our argument, the limit is the upper bound integer for prime number generation.
    We use the Sieve of Eratosthenes algorithm to find all prime numbers up to the limit we give.
    In this file, the main use of it is to generate small prime numbers.
    In return, we get the list of prime numbers up to the limit.
    '''
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num, isprime in enumerate(sieve):
        if isprime:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return [num for num, isprime in enumerate(sieve) if isprime]

smallprime = eratosieve(3571)

def millerrabin(n, k=40):
    '''
    In our argument, the integer n is the number that we want to test of its primality.
    Here, the Miller-Rabin Probabilistic Primality Test looks at
    the probability of a number being prime.
    If we get a True after all the tests, n is likely to be a prime number.
    '''
    if n < 2:
        return False
    for p in smallprime:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def dobigprime(bits):
    '''
    In the argument, the integer bits are the number of bits of the prime number we want to generate.
    We use the Miller-Rabin Primality Test to generate large prime numbers.
    We return the large prime number as an integer.
    '''
    while True:
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1))
        num |= 1
        if millerrabin(num):
            return num
