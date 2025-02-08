# This file tests if the key generation function works correctly.

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch
from RSA.KeyGen import genkeys

class TestKeyGen(unittest.TestCase):
    def test_keygen(self): # We test if the key generation function works correctly.
        publickey, privkey, p, q = genkeys(bits=16)
        e, _ = publickey
        d, _ = privkey
        phi = (p - 1) * (q - 1) # We calculate the Euler's totient function value.
        self.assertEqual((e * d) % phi, 1) # We check if the public and private keys are correct.

    @patch('RSA.KeyGen.dobigprime')
    def test_sameprimesgenkeys(self, mock_dobigprime): # We simulate that the first two calls to dobigprime return the same prime, then a different prime is returned to break the loop.
        mock_dobigprime.side_effect = [17, 17, 19]
        pubkey, privkey, p, q = genkeys(bits=16)
        self.assertNotEqual(p, q)
    
    @patch("RSA.KeyGen.gcd")
    def test_enocoprimegenkeys(self, mock_gcd): # We simulate that the first call to gcd returns a non-1 value (e.g. 2) and the second call returns 1.
        mock_gcd.side_effect = [2, 1]
        publickey, privkey, p, q = genkeys(bits=16)
        e, _ = publickey # We check if the public key is not 65537.
        self.assertNotEqual(e, 65537)

if __name__ == "__main__":
    unittest.main()  # pragma: no cover