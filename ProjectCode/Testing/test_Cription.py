# This file tests if the encryption and decryption functions work correctly.

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # This is for correct parent directory to path addition, allowing correct import of modules.

import unittest
from RSA.Cription import encrypt, decrypt
from RSA.KeyGen import genkeys

class TestCryption(unittest.TestCase):
    def test_cryption(self):
        pubkey, privkey, _, _ = genkeys(bits=2048) # Generate a pair of RSA keys with 2048 bits.
        message = "Trying close to 256 characters ssadösfkjdslföjdskfnöjdndsfjasdökfndsö fndsfidsofndskncödnödiofhdskjfndsöfidsohf kjdsnvcöoidsfdkjsncldshfiudshfjdsnliuafnjdskljlksadvcj dkvcdslicjvndslibusldbsjvcsubdslivbcjdsildjnbclkjsabdvcldsujvcasöaieufwoö" # Sample message to be encrypted.
        encrypted = encrypt(message, pubkey) # Encrypt the message with the public key.
        decrypted = decrypt(encrypted, privkey) # Decrypt the message with the private key.
        self.assertEqual(message, decrypted) # Check if the decrypted message is the same as the original message.

    def test_decryptunicodeerror(self): # This test's purpose is to get the UnicodeDecodeError in the decrypt function.
        pubkey, privkey, _, _ = genkeys(bits=2048)
        encrypted = encrypt("Hello, RSA!", pubkey)
        invalidencrypted = encrypted + 1 # Here, the encrypted message is changed to make it invalid as UTF-8.
        result = decrypt(invalidencrypted, privkey)
        self.assertEqual(result, "The decryption didn't happen, because the decrypted bytes can't be decoded as UTF-8.")

if __name__ == "__main__": # pragma: no cover
    unittest.main()