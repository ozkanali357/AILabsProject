'''
This file tests if the key generation function works correctly.
'''

import sys
import os
import unittest
from unittest.mock import patch
from RSA.keygen import genkeys

# This is for correct parent directory to path addition, allowing correct import of modules.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestKeyGen(unittest.TestCase):
    '''
    This class has tests for the key generation function.
    '''
    def test_keygen(self): # We test if the key generation function works correctly.
        '''
        This method checks if the generated keys satisfy the RSA properties.
        '''
        publickey, privkey, p, q = genkeys(bits=16)
        e, _ = publickey
        d, _ = privkey
# We calculate the Euler's totient function value.
        phi = (p - 1) * (q - 1)
# We check if the public and private keys are correct.
        self.assertEqual((e * d) % phi, 1)

    @patch('RSA.keygen.dobigprime')
    def test_sameprimesgenkeys(self, mock_dobigprime):
        '''
        We simulate that the first two calls to dobigprime return the same prime,
        then a different prime is returned to break the loop.
        '''
        mock_dobigprime.side_effect = [17, 17, 19]
        _, _, p, q = genkeys(bits=16)
        self.assertNotEqual(p, q)

    @patch("RSA.keygen.gcd")
    def test_enocoprimegenkeys(self, mock_gcd):
        '''
        We simulate that the first call to gcd returns a non-1 value,
        such as 2, and the second call returns 1.
        '''
        mock_gcd.side_effect = [2, 1]
        publickey, _, _, _ = genkeys(bits=16)
        e, _ = publickey
# We check if the public key is not 65537.
        self.assertNotEqual(e, 65537)

# pragma: no cover
if __name__ == "__main__":
    unittest.main()
