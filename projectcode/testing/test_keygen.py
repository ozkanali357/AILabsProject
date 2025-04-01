'''
This file tests if the key generation function works correctly.
'''

import sys
import unittest
import builtins
from unittest.mock import patch
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.keygen import genkeys

def custom_pow(*args, **kwargs):
    if not hasattr(custom_pow, "called"):
        custom_pow.called = True
        raise ValueError
    return builtins.pow(*args, **kwargs)

class TestKeyGen(unittest.TestCase):
    '''
    This class has tests for the key generation function.
    '''
    def test_keygen(self):
        '''
        This method checks if the generated keys satisfy the RSA properties.
        '''
        publickey, privkey, p, q = genkeys(bits=16)
        e, _ = publickey
        d, _ = privkey
        phi = (p - 1) * (q - 1)
        self.assertEqual((e * d) % phi, 1)

    @patch('projectcode.rsa.keygen.dobigprime')
    def test_sameprimesgenkeys(self, mock_dobigprime):
        '''
        We simulate that the first two calls to dobigprime return the same prime,
        then a different prime is returned to break the loop.
        '''
        mock_dobigprime.side_effect = [17, 17, 19, 23]
        _, _, p, q = genkeys(bits=16)
        self.assertNotEqual(p, q)

    @patch("projectcode.rsa.keygen.euclidgcd")
    def test_enocoprimegenkeys(self, mock_euclidgcd):
        '''
        We simulate that the first call to euclidgcd returns a non-1 value,
        such as 2, and the second call returns 1.
        '''
        mock_euclidgcd.side_effect = [2, 2, 2, 1, 1, 1]
        publickey, _, _, _ = genkeys(bits=16)
        e, _ = publickey
        self.assertNotEqual(e, 65537)

    @patch("projectcode.rsa.keygen.dobigprime")
    @patch("projectcode.rsa.keygen.euclidgcd")
    def test_genkeyseloop(self, mock_euclidgcd, mock_dobigprime):
        '''
        This test forces the genkeys function to loop and change the value of e.
        '''
        mock_euclidgcd.side_effect = [2, 2, 2, 1, 1, 1]
        mock_dobigprime.side_effect = [17, 19, 23, 29, 31, 37]
        publickey, privkey, p, q = genkeys(bits=16)
        e, _ = publickey
        d, _ = privkey
        phi = (p - 1) * (q - 1)
        self.assertEqual((e * d) % phi, 1)

    @patch("projectcode.rsa.keygen.dobigprime")
    def test_genkeysvalerror(self, mock_dobigprime):
        '''
        This test forces the genkeys function to raise a ValueError and continue the loop.
        '''
        mock_dobigprime.side_effect = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        with patch("projectcode.rsa.keygen.pow", side_effect=custom_pow):
            publickey, privkey, p, q = genkeys(bits=16)
            e, _ = publickey
            d, _ = privkey
            phi = (p - 1) * (q - 1)
            self.assertEqual((e * d) % phi, 1)

# pragma: no cover
if __name__ == "__main__":
    unittest.main()
