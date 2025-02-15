'''
This file aims the generation of large prime numbers for RSA encryption.
The Sieve of Eratosthenes algorithm generates small prime numbers.
The Miller-Rabin probabilistic primality test generates large prime numbers.
'''

import random

# In our argument, the limit is the upper bound integer for prime number generation.
def eratosieve(limit):
    '''
    We use the Sieve of Eratosthenes algorithm to find all prime numbers up to the limit we give.
    In this file, the main use of it is to generate small prime numbers.
    '''
# In the index of the sieve list, each index shows
# the prime numbers as true and the non-prime numbers as false.
    sieve = [True] * (limit + 1)
# 0 and 1 are not prime numbers.
    sieve[0] = sieve[1] = False
    for num, isprime in enumerate(sieve):
        if isprime:
# It marks the multiples of the prime numbers as non-prime
# and returns the numbers still marked as prime.
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
# In return, we get the list of prime numbers up to the limit.
    return [num for num, isprime in enumerate(sieve) if isprime]

# We set the limit to 3571, which is the 500th prime number.
# This generates all prime numbers up to 3571,
# which are going to be used in quick divisibility checks.
smallprime = eratosieve(3571)

# In our argument, the integer n is the number that we want to test of its primality.
# The integer k is the number of tests (iterations) we want to run.
# Higher k values increase the accuracy of the test.
# We chose 40 as a common (default) value.
def millerrabin(n, k=40):
    '''
    Here, the Miller-Rabin Probabilistic Primality Test looks at
    the probability of a number being prime.
    '''
# This check is because negative nubers, 0, and 1 are not prime numbers.
    if n < 2:
        return False
# This is to check if n is divisible by the first 500 prime numbers
# (small primes) or if it is already one of the small primes.
    for p in smallprime:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
# This test is repeated 40 times with random a values between 2 and n - 2.
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
# In the boolean value return of the object,
# if we get a True after all the tests, n is likely to be a prime number.
    return True

# In the argument, the integer bits are the number of bits of the prime number we want to generate.
def dobigprime(bits):
    '''
    We use the Miller-Rabin Primality Test to generate large prime numbers.
    '''
    while True:
        num = random.getrandbits(bits)
# We want the the modulus to be close to 2048 bits to be more secure.
# For this, the primes will be 1024 bits each.
# We set the most significant bit to 1 to make sure the number is 1024 bits.
        num |= (1 << (bits - 1))
# We check if the number is odd
        num |= 1
# We then send it to the Miller-Rabin test.
# If it passes, then the number is a large prime.
        if millerrabin(num):
# We return the large prime number as an integer.
            return num
