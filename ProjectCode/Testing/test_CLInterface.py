# This file tests if the CLI functionality works correctly.

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # This is for correct parent directory to path addition, allowing correct import of modules.

import unittest
from unittest.mock import patch
from io import StringIO
from RSA.CLInterface import main

class TestCLI(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"]) # This is to simulate the user input of 1.
    def test_keygen(self, mockinput):
        with patch("sys.stdout", new=StringIO()) as fakeoutput: # This is to capture the output of the function.
            main()
            output = fakeoutput.getvalue().strip()
            self.assertIn("Public Key (e, n):", output) # These are to see if we got the expected key generations.
            self.assertIn("Private Key (d, n):", output)

    @patch("builtins.input", side_effect=["2", "Hello, RSA!", "65537", "3233"]) # This is to simulate the user input of 2. Then the message and public key parts.
    def test_encrypt(self, mockinput):
        with patch("sys.stdout", new=StringIO()) as fakeoutput: # This is to capture the output of the function.
            main()
            output = fakeoutput.getvalue().strip()
            self.assertIn("Encrypted Message:", output) # This is to see if we got the expected encrypted message.

    @patch("builtins.input", side_effect=["3", "1234", "2753", "3233"]) # This is to simulate the user input of 3. Then the message and private key parts.
    def test_decrypt(self, mockinput):
        with patch("sys.stdout", new=StringIO()) as fakeoutput: # The similar explanations apply to this part as well.
            main()
            output = fakeoutput.getvalue().strip()
            self.assertIn("Decrypted Message:", output)

    @patch("builtins.input", side_effect=["4"])  # This is to simulate the user input of 4 and the error message.
    def test_invalidchoice(self, mockinput):
        with patch("sys.stdout", new=StringIO()) as fakeoutput: # The similar explanations apply to this part as well.
            main()
            output = fakeoutput.getvalue().strip()
            self.assertIn("Invalid choice.", output)

if __name__ == "__main__":
    unittest.main()