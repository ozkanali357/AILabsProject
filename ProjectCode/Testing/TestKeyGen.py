# This file tests if the key generation function works correctly.

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # This is for correct parent directory to path addition, allowing correct import of modules.

import unittest
from RSA.KeyGen import genkeys

class TestKeyGen(unittest.TestCase):
    def testkeygen(self): # The key generation function is called and is asked to create a pair of RSA keys (16 bits size) and the prime factors used.
        publickey, privkey, p, q = genkeys(bits=16)
        e, _ = publickey # The public key is expected to be a tuple with exponent e and modulus n (we don't use it here so it's ignored with _).
        d, _ = privkey # The private key is expected to be a tuple containing exponent d and an additional value (which is ignored in this test).
        phi = (p - 1) * (q - 1) # The Euler's totient function is calculated.
        self.assertEqual((e * d) % phi, 1) # We look if the public exponent e and private exponent d  are modular inverses of eachother.

if __name__ == "__main__":
    unittest.main()