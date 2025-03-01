"""
This file has unit tests for prime_gen.py.
"""

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.primegen import eratosieve, millerrabin, dobigprime

class TestPrimeGen(unittest.TestCase):
    """
    This class tests the prime number generation functions.
    """
    def test_eratosieve(self):
        """
        The method tests the sieve of eratosthenes function by calling the argument 30.
        """
        primes = eratosieve(30)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_millerrabin(self):
        """
        We check the Miller Rabin Primality Test.
        """
        self.assertTrue(millerrabin(13))
        self.assertFalse(millerrabin(15))
        self.assertFalse(millerrabin(0))
        self.assertFalse(millerrabin(1))
        self.assertFalse(millerrabin(-5))

    def test_dobigprime(self):
        """
        We test if the function that generates large prime numbers
        can make it the specified amount (10 bits).
        """
        prime = dobigprime(10)
        self.assertTrue(prime % 2 != 0)
        self.assertTrue(millerrabin(prime))

    def test_bigcomposite(self):
        """
        We test Miller-Rabin with a composite number that is a product of two large primes.
        """
        p = dobigprime(500)
        q = dobigprime(500)
        composite = p * q
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
