'''
This file tests if the encryption and decryption functions work correctly.
'''

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.cription import encrypt, decrypt
from projectcode.rsa.keygen import genkeys

class TestCryption(unittest.TestCase):
    '''
    This class has unit tests for the encryption and decryption functions.
    '''
    def test_cryption(self):
        '''
        This method checks if a message can be encrypted and decrypted correctly.
        '''
        pubkey, privkey, _, _ = genkeys(bits=2048)
        message = ("Trying close to 256 characters ssadösfkjdslföjdskfnöjdndsfjasdökfndsö"
                "fndsfidsofndskncödnödiofhdskjfndsöfidsohf kjdsnvcöoidsfdkjsncldshfiudshfjdsnliuafnjdskljlksadvcj"
                "dkvcdslicjvndslibusldbsjvcsubdslivbcjdsildjnbclkjsabdvcldsujvcasöaieufwoö")
        encrypted = encrypt(message, pubkey)
        decrypted = decrypt(encrypted, privkey)
        self.assertEqual(message, decrypted)

    def test_decryptunicodeerror(self):
        '''
        This test's purpose is to get the UnicodeDecodeError in the decrypt function.
        '''
        pubkey, privkey, _, _ = genkeys(bits=2048)
        encrypted = encrypt("Hello, RSA!", pubkey)
        invalidencrypted = encrypted + 1
        result = decrypt(invalidencrypted, privkey)
        self.assertEqual(result, "The decryption didn't happen, because the decrypted bytes can't be decoded as UTF-8.")

    def test_encryptmsglong(self):
        '''
        This test checks if the encrypt function raises a ValueError when the message is too long.
        '''
        pubkey, _, _, _ = genkeys(bits=16)
        message = "A" * 1000
        with self.assertRaises(ValueError) as context:
            encrypt(message, pubkey)
        self.assertEqual(str(context.exception), "For this key size, the message is long.")

# pragma: no cover
if __name__ == "__main__":
    unittest.main()
