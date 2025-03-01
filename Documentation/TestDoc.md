# Testing Document

There is also a 10/10 pylint code quality in all of the project's projectcode files. The terminal output of pylint is in the Documentation directory. You can check it using this command: pylint projectcode/rsa/*.py

## Coverage Report of the Unit Tests
### Algorithms Coverage Summary (Without Interfaces)
- Overall Coverage: 100%
- Files Covered:
  - primegen.py: 100%
  - keygen.py: 100%
  - cription.py: 100%

## What Have Been Tested and How?

### primegen.py
- eratosieve(limit): Generates small prime numbers up to a given limit using the Sieve of Eratosthenes. Checked using a given value and ensuring that it is generated correctly up to it.
- millerrabin(n, k=40): Checks a number's primality using Miller-Rabin Primality Test. Checked using known composite and prime numbers. It's also composite numbers.
- dobigprime(bits): Generates big prime numbers using Miller-Rabin Primality Test. Checked using a known large prime.

### keygen.py
- genkeys(bits=1024): Generates public and private keys to be used in RSA encryption.
- Added unit tests to verify that generated keys satisfy RSA properties. Mocking was used to simulate different scenarios such as generating same primes and ensuring that the public exponent is coprime to Euler's totient function.

### cription.py
- encrypt(message, pubkey): Encrypts a message using RSA's public key.
- decrypt(ciphertext, privkey): Decrypts a ciphertext using RSA's private key.
- The unit tests were created to verify that a message can be encrypted and decrypted correctly. Edge cases, such as invalid UTF-8 sequence, were tried to verify that it is handled correctly.

## What Kind of Inputs Were Used for the Testing?

- Prime Generation: Eratosthenes Sieve small integers, composite and prime for Miller-Rabin, and bit sizes for dobigprime.
- Key Generation: Bit length default of 1024 and mocked scenarios for edge cases.
- Encryption and Decryption: Sample message like string of large characters and special characters, to check encryption and decryption function.

## How to Repeat the Tests?

- Install unittest: pip install coverage
- Move to Testing directory of projectcode: export PYTHONPATH=where_the_project_is_downloaded/projectcode
- Execute the unit tests: cd where_the_project_is_downloaded/projectcode/Testing
coverage run --source=./rsa --omit=./rsa/clinterface.py,./rsa/guinterface.py -m unittest discover
- In case of covarage report: coverage html
- Open report: xdg-open htmlcov/index.html

or this:
- export PYTHONPATH=$(pwd)/projectcode
- coverage run -m unittest discover -s projectcode/testing -p "test_*.py"
- coverage report -m

## Presentations of the Empirical Testing Results

### Prime Generation
- Eratosthenes Sieve: Calculated up to 30 primes were [2, 3, 5, 7, 11, 13, 17, 19, 23, 29].
- Miller-Rabin Primality Test: Identified correctly the primes and composite.
- Generation of Large Primes: Successfully generated large primes of given sizes.

### Generation of Keys
- Generated Keys: Checked that keys generated meet RSA properties.
- Mocked Scenarios: Checked that program is working in cases of edge cases.

### Encryption and Decryption
- Sample Message: Successfully encrypted and decrypted message without loss of information.
- Edge Cases: Successfully handled invalid UTF-8 sequence and other edge cases.

### Graphical Representation
The report of files and function coverage is in the Documentation directory.