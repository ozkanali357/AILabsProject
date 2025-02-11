'''
This file tests if the encryption and decryption functions work correctly.
'''

import sys
import os
import unittest
from RSA.cription import encrypt, decrypt
from RSA.keygen import genkeys

# This is for correct parent directory to path addition, allowing correct import of modules.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestCryption(unittest.TestCase):
    '''
    This class has unit tests for the encryption and decryption functions.
    '''
    def test_cryption(self):
        '''
        This method checks if a message can be encrypted and decrypted correctly.
        '''
# Generate a pair of RSA keys with 2048 bits.
        pubkey, privkey, _, _ = genkeys(bits=2048)
# Sample message to be encrypted.
        message = ("Trying close to 256 characters ssadösfkjdslföjdskfnöjdndsfjasdökfndsö"
                "fndsfidsofndskncödnödiofhdskjfndsöfidsohf kjdsnvcöoidsfdkjsncldshfiudshfjdsnliuafnjdskljlksadvcj"
                "dkvcdslicjvndslibusldbsjvcsubdslivbcjdsildjnbclkjsabdvcldsujvcasöaieufwoö")
# Encrypt the message with the public key.
        encrypted = encrypt(message, pubkey)
# Decrypt the message with the private key.
        decrypted = decrypt(encrypted, privkey)
# Check if the decrypted message is the same as the original message.
        self.assertEqual(message, decrypted)

    def test_decryptunicodeerror(self):
        '''
        This test's purpose is to get the UnicodeDecodeError in the decrypt function.
        '''
        pubkey, privkey, _, _ = genkeys(bits=2048)
        encrypted = encrypt("Hello, RSA!", pubkey)
# Here, the encrypted message is changed to make it invalid as UTF-8.
        invalidencrypted = encrypted + 1
        result = decrypt(invalidencrypted, privkey)
        self.assertEqual(result, "The decryption didn't happen, because the decrypted bytes can't be decoded as UTF-8.")

# pragma: no cover
if __name__ == "__main__":
    unittest.main()
