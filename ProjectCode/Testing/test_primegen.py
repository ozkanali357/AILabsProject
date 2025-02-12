"""
This file has unit tests for prime_gen.py.
"""

import sys
import os
import unittest
from rsa.primegen import eratosieve, millerrabin, dobigprime

# This is for correct parent directory to path addition, allowing correct import of modules.
thisdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(thisdir)
sys.path.append(parentdir)

class TestPrimeGen(unittest.TestCase):
    """
    This class tests the prime number generation functions.
    """
    def test_eratosieve(self):
        """
        The method tests the sieve of eratosthenes function by calling the argument 30.
        """
# We need to be sure that the returned list of numbers match the primes up to 30.
        primes = eratosieve(30)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_millerrabin(self):
        """
        We check the Miller Rabin Primality Test.
        """
# 13 is prime, so it should return True.
        self.assertTrue(millerrabin(13))
# 15 isn't prime, so it should return False.
        self.assertFalse(millerrabin(15))
# 0 isn't prime, so it should return False.
        self.assertFalse(millerrabin(0))
# 1 isn't prime, so it should return False.
        self.assertFalse(millerrabin(1))
# Negative numbers aren't prime, so -5 should return False.
        self.assertFalse(millerrabin(-5))

    def test_dobigprime(self):
        """
        We test if the function that generates large prime numbers
        can make it the specified amount (10 bits).
        """
        prime = dobigprime(10)
# We check if the generated number is odd.
        self.assertTrue(prime % 2 != 0)
# We check if the generated number is prime.
        self.assertTrue(millerrabin(prime))

    def test_bigcomposite(self):
        """
        We test Miller-Rabin with a composite number that is a product of two large primes.
        """
        p = dobigprime(500)
        q = dobigprime(500)
        composite = p * q
# The composite number should return False.
        self.assertFalse(millerrabin(composite))

    def test_bigprime(self):
        """
        This test is similar to the one above, it tests Miller-Rabin with a known large prime.
        """
        prime = dobigprime(1024)
        self.assertTrue(millerrabin(prime))

# pragma: no cover
if __name__ == "__main__":
    unittest.main()
