# This file has unit tests for PrimeGen.py.

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # This is for correct parent directory to path addition, allowing correct import of modules.

import unittest
from RSA.PrimeGen import eratosieve, millerrabin, dobigprime

class TestPrimeUtils(unittest.TestCase):
    def test_eratosieve(self): # The method tests the sieve of eratosthenes function by calling the argument 30.
        primes = eratosieve(30) # We need to be sure that the returned list of of numbers match the primes up to 30.
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_millerrabin(self): # We test the Miller Rabin Primality Test by checking it with
        self.assertTrue(millerrabin(13))  # 13 is prime, so it should return True.
        self.assertFalse(millerrabin(15))  # 15 isn't prime, so it should return False.
        self.assertFalse(millerrabin(0))  # 0 isn't prime, so it should return False.
        self.assertFalse(millerrabin(1))  # 1 isn't prime, so it should return False.
        self.assertFalse(millerrabin(-5))  # Negative numbers aren't prime, so -5 should return False.
    
    def test_dobigprime(self): # We test if the function that generates large prime numbers can make it the specified amount (10 bits).
        prime = dobigprime(10)
        self.assertTrue(prime % 2 != 0) # We check if the generated number is odd.
        self.assertTrue(millerrabin(prime)) # We check if the generated number is prime.

    def test_large_composite(self): # We test Miller-Rabin with a composite number that is a product of two large primes.
        p = dobigprime(500)
        q = dobigprime(500)
        composite = p * q
        self.assertFalse(millerrabin(composite)) # The composite number should return False.

    def test_large_prime(self): # This test is similar to the one above, it tests Miller-Rabin with a known large prime.
        prime = dobigprime(1024)
        self.assertTrue(millerrabin(prime))

if __name__ == "__main__": # pragma: no cover
    unittest.main()