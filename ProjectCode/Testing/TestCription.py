# This file tests if the encryption and decryption functions work correctly.

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from RSA.Cription import encrypt, decrypt
from RSA.KeyGen import genkeys

class TestCryption(unittest.TestCase):
    def test_cryption(self):
        pubkey, privkey, _, _ = genkeys(bits=2048) # Generate a pair of RSA keys with 2048 bits.
        message = "Hello, RSA!" # Sample message to be encrypted.
        encrypted = encrypt(message, pubkey) # Encrypt the message with the public key.
        decrypted = decrypt(encrypted, privkey) # Decrypt the message with the private key.
        self.assertEqual(message, decrypted) # Check if the decrypted message is the same as the original message.

if __name__ == "__main__":
    unittest.main()