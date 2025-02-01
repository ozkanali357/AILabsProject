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

    def test_millerrabin(self): # We test the Miller Rabin Primality Test by checking it with 13 and 15.
        self.assertTrue(millerrabin(13)) # 13 is a prime number, so it should return True.
        self.assertFalse(millerrabin(15)) # 15 is not a prime number, so it should return False.       

    def test_dobigprime(self): # We test if the function that generates large prime numbers can make it the specified amount (10 bits).
        prime = dobigprime(10)
        self.assertTrue(millerrabin(prime))

if __name__ == "__main__":
    unittest.main()