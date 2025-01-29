# This file aims the generation of large prime numbers for RSA encryption.

import random

# We use the Sieve of Eratosthenes algorithm to find all prime numbers up to the limit we give. In this file, the main use of it is to generate small prime numbers.

def eratosieve(limit): # In our argument, the limit is the upper bound integer for prime number generation.
    sieve = [True] * (limit + 1) # In the index of the sieve list, each index shows the prime numbers as true and the non-prime numbers as false.
    sieve[0] = sieve[1] = False # 0 and 1 are not prime numbers.
    for num, isprime in enumerate(sieve):
        if isprime:
            for multiple in range(num * num, limit + 1, num): # It marks the multiples of the prime numbers as non-prime and returns the numbers still marked as prime.
                sieve[multiple] = False
    return [num for num, isprime in enumerate(sieve) if isprime] # In return, we get the list of prime numbers up to the limit.

# We set the limit to 3571, which is the 500th prime number. This generates all prime numbers up to 3571, which are going to be used in quick divisibility checks.

smallprime = eratosieve(3571)

# Here, the Miller-Rabin Probabilistic Primality Test looks at the probability of a number being prime.

def millerrabin(n, k=40): # In our argument, the integer n is the number that we want to test of its primality. The integer k is the number of tests (iterations) we want to run. Higher k values increase the accuracy of the test. We chose 40 as a common (default) value.
    if n < 2: # This check is becayuse 0 and 1 are not prime numbers.
        return False
    for p in smallprime: # This is to check if n is divisible by the first 500 prime numbers (small primes) or if it is already one of the small primes.
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2) # This test is repeated 40 times with random a values between 2 and n - 2.
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True # In the boolean value return of the object, if we get a True after all the tests, n is likely to be a prime number.

# We use the Miller-Rabin Primality Test to generate large prime numbers.

def dobigprime(bits): # In the argument, the integer bits are the number of bits of the prime number we want to generate.
    while True:
        num = random.getrandbits(bits)
        if num % 2 != 0 and millerrabin(num): # We check if the number is odd, then send it to the Miller-Rabin test. If it passes, then the number is a large prime.
            return num # We return the large prime number as an integer.